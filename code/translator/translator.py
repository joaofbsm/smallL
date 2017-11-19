#!/usr/bin/env python3

"""Translates Three Address Code(TAC) to Java bytecodes with Jasmin syntax"""

__author__ = "João Francisco B. S. Martins and Pedro Dalla Vechia Chaves"
__email__ = "joaofbsm@dcc.ufmg.br, pedrodallav@dcc.ufmg.br"
__license__ = "GPL"
__version__ = "3.0"

import re
import sys
from variable import Variable
from operation import Operation
from opbuilder import OpBuilder


def parse_labels(file_path):
    """Parse the labels in the file and generate two dictionaries.
    
    Arguments:
        file_path -- Path to intermediate code file.
    """

    label_eq = {}  # Label equivalency dictionary
    label_line = {}  # Label per line number
    with open(file_path, 'r') as f:
        for i, line in enumerate(f):
            labels = line.split(':')
            for label in labels[0:-1]:
                label_eq[label] = labels[0]
                label_line[i] = labels[0]

    return label_eq, label_line


def is_variable(name):
    """Check if name is a valid variable name using regex
    
    Arguments:
        name -- Name to be matched.
    """

    variable_pattern = re.compile("^[a-zA-Z_$][a-zA-Z_$0-9]*")
    if name == "if" or name == "iffalse" or name == "goto" or name == "print":
        return False
    else:
        return bool(variable_pattern.match(name))


def add_variable(variable_name, symbol_table, is_array):
    """Add variable to symbol table.
    
    Involves declaration of variables and also updates the list of JVM's local
    variables.
    
    Arguments:
        variable_name -- Variable name.
        symbol_table -- Dictionary describing the symbol table.
        is_array -- Flag specifying if variable is an array.
    """

    _type = "double_arr" if is_array else "double"
    pos = (len(symbol_table) * 2) + 1
    symbol_table[variable_name] = Variable(variable_name, _type, pos)


def get_quadruple(line, symbol_table, label_eq, op_builder):
    """State Machine that identifies the type of operation and its operands
    
    Arguments:
        line -- Parsed line of code that contains the quadruple.
        symbol_table -- Dictionary describing the symbol table.
        label_eq -- Dictionary describing the label equivalency.
        op_builder -- Operation builder object.
    """

    operator = None
    op1 = None  # Operand 1
    op2 = None  # Operand 2
    op3 = None  # Operand 3
    arith_op = None  # For arith_attrib
    goto = None  # For if and iffalse

    arr_declaration = ""  # Array declaration 

    if len(line) < 2:  # Line is empty
        return arr_declaration, Operation("empty", op1, op2, op3, arith_op, goto)

    if is_variable(line[0]):
        if line[1] == '[': # Operation is attributing to array(arr_attrib)
            if line[0] not in symbol_table:
                add_variable(line[0], symbol_table, is_array=True)
                arr_declaration = op_builder.declare_arr(symbol_table[line[0]])

            operator = "arr_attrib"
            op1 = line[0]  # Array variable
            op2 = line[2]  # Index of array
            op3 = line[5]  # Const/Var on the right side

        else:  # First variable is not an array
            if line[0] not in symbol_table:
                add_variable(line[0], symbol_table, is_array=False) 

            op1 = line[0]

            if len(line) <= 3:  # Operation is a normal attribution(attrib)
                operator = "attrib"
                op2 = line[2]
            else:
                if line[3] == '[':  # Operation is attributing array pos to variable(attrib_arr)
                    operator = "attrib_arr"
                    op2 = line[2]  # Array variable
                    op3 = line[4]  # Index of array

                else:  # Operation is an attribution of arithmetic operation(arith_attrib)
                    operator = "arith_attrib"
                    op2 = line[2]
                    arith_op = line[3]
                    op3 = line[4]

    elif line[0] == "goto":  # goto operation
        operator = line[0]
        op1 = label_eq[line[1]]  # goto equivalent label

    elif line[0] == "print":  # print variable
        if len(line) <= 2:
            operator = "print_var"
            op1 = line[1]  # Variable to be printed
        else:
            op1 = line[1]  # Array to be printed
            op2 = line[3]  # Index of array
            if is_variable(op2):
                operator = "print_arr_var"
            else:
                operator = "print_arr_int"
            
    else:  # if or iffalse
        operator = line[0]
        op1 = line[1]
        op2 = line[2]
        op3 = line[3]
        goto = label_eq[line[5]]  # GOTO equivalent label

    return arr_declaration, Operation(operator, op1, op2, op3, arith_op, goto)


def translate_code(file_path, label_eq, label_line):
    """Parses the code translating the operations
    
    Arguments:
        file_path -- Path to intermediate code file.
        label_eq -- Label equivalence dictionary.
        label_line -- Lines of code related to label declarations.
    """

    symbol_table = {}
    op_builder = OpBuilder()  # Operation builder
    translated = ""

    with open(file_path, 'r') as f:

        for i, line in enumerate(f):
            line = line.split(':')[-1].split()
            arr_declaration, operation = get_quadruple(line, symbol_table, 
                                                       label_eq, op_builder)

            # Build Jasmin equivalent of the operation     
            op_translated = op_builder.methods[operation.operator](operation, 
                                                                  symbol_table) 

            if arr_declaration:
                op_translated = arr_declaration + "\t\t" + op_translated

            if i in label_line:  # Print line label if it exists
                if len(label_line[i]) <= 2:
                    translated += ("{}:\t\t{}".format(label_line[i], 
                                                      op_translated))
                else:
                    translated += ("{}:\t{}".format(label_line[i], 
                                                    op_translated))
            else:
                translated += ("\t\t{}".format(op_translated)) 

    n_locals = (len(symbol_table) * 2) + 1

    return n_locals, translated


def build_header():
    """Builds the unchanging header"""

    print(
""".version 50 0 
.class public super Main 
.super java/lang/Object 

.method public <init> : ()V 
\t.code stack 1 locals 1 
L0:\t\taload_0 
L1:\t\tinvokespecial Method java/lang/Object <init> ()V 
L4:\t\treturn 
L5:     
\t.end code 
.end method 

.method public static main : ([Ljava/lang/String;)V""")


def build_footer():
    """Builds the unchanging footer"""

    print(
"""\t.end code 
.end method 
.sourcefile 'Main.java' 
.end class""")


def main(args):
    file_path = args[1]
    stack_size = 4  # Max stack size

    label_eq, label_line = parse_labels(file_path)

    build_header()

    n_locals, translated_code = translate_code(file_path, label_eq, label_line)

    print(("\t.code stack {} locals {}\n").format(stack_size, n_locals))
    print("{}".format(translated_code))
    
    build_footer()
    

if __name__ == "__main__":
    main(sys.argv)