import re
import sys
from variable import Variable
from operation import Operation
from opbuilder import OpBuilder


def parse_labels(file_path):
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
    variable_pattern = re.compile("^[a-zA-Z_$][a-zA-Z_$0-9]*")
    if name == "if" or name == "iffalse" or name == "goto":
        return False
    else:
        return bool(variable_pattern.match(name))


def add_variable(variable_name, symbol_table, is_array):
    _type = "double_arr" if is_array else "double"
    pos = (len(symbol_table) * 2) + 1
    symbol_table[variable_name] = Variable(variable_name, _type, pos)


def get_quadruple(line, symbol_table, label_eq, opbuilder):
    operator = None
    op1 = None  # Operand 1
    op2 = None  # Operand 2
    op3 = None  # Operand 3
    arith_op = None  # For arith_attrib
    goto = None  # For if and iffalse

    if len(line) < 2:  # Line is empty
        return Operation("empty", op1, op2, op3, arith_op, goto)

    if is_variable(line[0]):
        if line[1] == '[': # Operation is attributing to array(arr_attrib)
            if line[0] not in symbol_table:
                add_variable(line[0], symbol_table, is_array=True)
                opbuilder.declare_arr(symbol_table[line[0]])

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
                    op3 = line[4] # Index of array

                else:  # Operation is an attribution of arithmetic operation(arith_attrib)
                    operator = "arith_attrib"
                    op2 = line[2]
                    arith_op = line[3]
                    op3 = line[4]

    elif line[0] == "goto":  # goto operation
        operator = line[0]
        op1 = label_eq[line[1]]  # goto equivalent label

    else:  # if or iffalse
        operator = line[0]
        op1 = line[1]
        op2 = line[2]
        op3 = line[3]
        goto = label_eq[line[5]]  # GOTO equivalent label

    return Operation(operator, op1, op2, op3, arith_op, goto)


def parse_code(file_path, label_eq, label_line):
    symbol_table = {}
    opbuilder = OpBuilder()  # Operation builder

    with open(file_path, 'r') as f:
        #last_len = 0  # TODO: DELETE

        for i, line in enumerate(f):
            line = line.split(':')[-1].split()
            operation = get_quadruple(line, symbol_table, label_eq, opbuilder)

            if i in label_line:  # Print line label if it exists
                print("{}: ".format(label_line[i]), end='') 
                #last_len = len(label_line[i])  # TODO: DELETE
            #else:
                #print("  " + (" " * last_len + "{}".format(operation.operator)))

            # Build Jasmin equivalent of the operation     
            opbuilder.methods[operation.operator](operation, symbol_table) 

    return 8, " "


def build_header():
    print(
""".version 52 0 
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
    print(
"""\t.end code 
.end method 
.sourcefile 'Main.java' 
.end class""")


def main(args):
    file_path = args[1]
    stack_size = 4  # Max stack size
    n_locals = 50

    label_eq, label_line = parse_labels(file_path)

    build_header()

    print(("\t.code stack {} locals {}\n").format(stack_size, n_locals))

    n_locals, gen_code = parse_code(file_path, label_eq, label_line)
    
    build_footer()
    

if __name__ == "__main__":
    main(sys.argv)