#!/usr/bin/env python3

"""Operation builder. Builds operations based in bytecode syntax"""

__author__ = "João Francisco B. S. Martins and Pedro Dalla Vechia Chaves"
__email__ = "joaofbsm@dcc.ufmg.br, pedrodallav@dcc.ufmg.br"
__license__ = "GPL"
__version__ = "3.0"

import re


class OpBuilder:
    def __init__(self):
        """Operation builder constructor"""

        self.methods = {"attrib": self.build_attrib,  # Attribute value to variable
                        "arith_attrib": self.build_arith_attrib,  # Attribution with arithmetic operation
                        "arr_attrib": self.build_arr_attrib,  # Attribute value to array position
                        "attrib_arr": self.build_attrib_arr,  # Attribute array position value to variable
                        "if": self.build_if,
                        "iffalse": self.build_iffalse,
                        "goto": self.build_goto,
                        "empty": self.build_empty,
                        "print_var": self.build_print_var,
                        "print_arr_int": self.build_print_arr_int,
                        "print_arr_var": self.build_print_arr_var}


    def declare_arr(self, variable):
        """Declare double array of 1000 positions

        Arguments:
            variable -- Variable name.
        """

        op_seq = ""

        op_seq += ("sipush 1000\n")  # 1000 positions
        op_seq += ("\t\tnewarray double\n")
        op_seq += ("\t\tastore {}\n".format(variable.pos))

        return op_seq


    def is_variable(self, name):
        """Check if name is a valid variable name using regex
        
        Arguments:
            name -- Name to be matched.
        """

        variable_pattern = re.compile("^[a-zA-Z_$][a-zA-Z_$0-9]*")
        return bool(variable_pattern.match(name))


    def load_operand(self, op, symbol_table, first_line=False):
        """Load operand according to its type(constant or variable)
        
        Arguments:
            op -- Operand.
            symbol_table -- Dictionary describing the symbol table.
        """

        op_seq = ""

        if self.is_variable(op):
            op = symbol_table[op]
            if first_line:
                op_seq += ("dload {}\n".format(op.pos))
            else:
                op_seq += ("\t\tdload {}\n".format(op.pos))
        else:
            if first_line:
                op_seq += ("ldc2_w {}\n".format(float(op)))
            else:
                op_seq += ("\t\tldc2_w {}\n".format(float(op)))

        return op_seq


    def load_array(self, arr, symbol_table, first_line=False):
        """Load array pointer
        
        Arguments:
            array -- Array to be loaded.
            symbol_table -- Dictionary describing the symbol table.
        """

        op_seq = ""

        arr = symbol_table[arr]
        if first_line:
            op_seq += ("aload {}\n".format(arr.pos))
        else:
            op_seq += ("\t\taload {}\n".format(arr.pos))

        return op_seq


    def store_variable(self, op, symbol_table, first_line=False):
        """Store double variable
        
        Arguments:
            op -- Operand.
            symbol_table -- Dictionary describing the symbol table.
        """

        op_seq = ""

        op = symbol_table[op]
        if first_line:
            op_seq += ("dstore {}\n".format(op.pos))
        else:
            op_seq += ("\t\tdstore {}\n".format(op.pos))

        return op_seq


    def store_array(self, arr, symbol_table, first_line=False):
        """Store position in array of doubles
        
        Arguments:
            arr -- Array to be stored.
            symbol_table -- Dictionary describing the symbol table.
        """

        op_seq = ""

        arr = symbol_table[arr]
        if first_line:
            op_seq += ("astore {}\n".format(arr.pos))
        else:
            op_seq += ("\t\tastore {}\n".format(arr.pos))

        return op_seq


    def build_attrib(self, operation, symbol_table):
        """Build stack code for simple attribution

        x = y
        
        operator -> attrib
        op1      -> var
        op2      -> const/var
        op3      -> None
        arith_op -> None
        goto     -> None

        Arguments:
            operation -- Operation to be built.
            symbol_table -- Dictionary describing the symbol table.
        """

        op_seq = ""

        op_seq += (self.load_operand(operation.op2, symbol_table, first_line=True))
        op_seq += (self.store_variable(operation.op1, symbol_table))

        return op_seq


    def build_arith_attrib(self, operation, symbol_table):
        """Build stack code for attribution with arithmetic operation

        x = y + z
        
        operator -> arith_attrib
        op1      -> var to be updated
        op2      -> operand1
        op3      -> operand2
        arith_op -> arithmetic operation
        goto     -> None

        Arguments:
            operation -- Operation to be built.
            symbol_table -- Dictionary describing the symbol table.
        """

        op_seq = ""
        
        op_seq += (self.load_operand(operation.op2, symbol_table, first_line=True))
        op_seq += (self.load_operand(operation.op3, symbol_table))
        
        if operation.arith_op == "+":
            op_seq += ("\t\tdadd\n")
        elif operation.arith_op == "-":
            op_seq += ("\t\tdsub\n")
        elif operation.arith_op == "*":        
            op_seq += ("\t\tdmul\n")
        elif operation.arith_op == "/":
            op_seq += ("\t\tddiv\n")

        op_seq += (self.store_variable(operation.op1, symbol_table))

        return op_seq


    def build_attrib_arr(self, operation, symbol_table):
        """Build stack code for attribution of array position to variable

        x = a[v]
        
        operator -> attrib_arr
        op1      -> var
        op2      -> array var
        op3      -> array index
        arith_op -> None
        goto     -> None

        Arguments:
            operation -- Operation to be built.
            symbol_table -- Dictionary describing the symbol table.
        """

        op_seq = ""

        # Get correct index
        op_seq += (self.load_operand(operation.op3, symbol_table, first_line=True))
        op_seq += ("\t\tldc2_w 8.0\n")
        op_seq += ("\t\tddiv\n")
        op_seq += (self.store_variable(operation.op3, symbol_table))

        # Load array position
        op_seq += (self.load_array(operation.op2, symbol_table))  # Array pointer(initial position)
        op_seq += (self.load_operand(operation.op3, symbol_table))  # Corrected index
        op_seq += ("\t\td2i\n")  # Converting double to int
        op_seq += ("\t\tdaload\n")  # Load correct array index
        op_seq += (self.store_variable(operation.op1, symbol_table))

        return op_seq


    def build_arr_attrib(self, operation, symbol_table):
        """Build stack code for attribution to array position

        a[v] = x
        
        operator -> arr_attrib
        op1      -> array var
        op2      -> array index
        op3      -> value to be attributed
        arith_op -> None
        goto     -> None

        Arguments:
            operation -- Operation to be built.
            symbol_table -- Dictionary describing the symbol table.
        """

        op_seq = ""

        # Get correct index
        op_seq += (self.load_operand(operation.op2, symbol_table, first_line=True))
        op_seq += ("\t\tldc2_w 8.0\n")
        op_seq += ("\t\tddiv\n")
        op_seq += (self.store_variable(operation.op2, symbol_table))

        # Load array position
        op_seq += (self.load_array(operation.op1, symbol_table))  # Array pointer(initial position)
        op_seq += (self.load_operand(operation.op2, symbol_table))  # Corrected index
        op_seq += ("\t\td2i\n")  # Converting double to int
        op_seq += (self.load_operand(operation.op3, symbol_table))
        op_seq += ("\t\tdastore\n")  # Load correct array index

        return op_seq


    def build_if(self, operation, symbol_table):
        """Build stack code for if conditional
        
        operator -> if
        op1      -> operand1
        op2      -> logical operation(generates boolean)
        op3      -> operand2
        arith_op -> None
        goto     -> Label to go to if condition is satisfied

        Arguments:
            operation -- Operation to be built.
            symbol_table -- Dictionary describing the symbol table.
        """

        op_seq = ""

        op_seq += (self.load_operand(operation.op1, symbol_table, first_line=True))
        op_seq += (self.load_operand(operation.op3, symbol_table))

        if operation.op2 == "==":
            op_seq += ("\t\tdcmpl\n")
            op_seq += ("\t\tifeq {}\n".format(operation.goto))

        elif operation.op2 == "!=":
            op_seq += ("\t\tdcmpl\n")
            op_seq += ("\t\tifne {}\n".format(operation.goto))

        elif operation.op2 == ">":
            op_seq += ("\t\tdcmpl\n")
            op_seq += ("\t\tifgt {}\n".format(operation.goto))

        elif operation.op2 == ">=":
            op_seq += ("\t\tdcmpl\n")
            op_seq += ("\t\tifge {}\n".format(operation.goto))

        elif operation.op2 == "<":
            op_seq += ("\t\tdcmpg\n")
            op_seq += ("\t\tiflt {}\n".format(operation.goto))

        elif operation.op2 == "<=":
            op_seq += ("\t\tdcmpg\n")
            op_seq += ("\t\tifle {}\n".format(operation.goto))

        return op_seq


    def build_iffalse(self, operation, symbol_table):
        """Build stack code for iffalse conditional
        
        operator -> iffalse
        op1      -> operand1
        op2      -> logical operation(generates boolean)
        op3      -> operan2
        arith_op -> None
        goto     -> Label to go to if condition is satisfied

        Arguments:
            operation -- Operation to be built.
            symbol_table -- Dictionary describing the symbol table.
        """

        op_seq = ""

        op_seq += (self.load_operand(operation.op1, symbol_table, first_line=True))
        op_seq += (self.load_operand(operation.op3, symbol_table))

        if operation.op2 == "==":
            op_seq += ("\t\tdcmpl\n")
            op_seq += ("\t\tifne {}\n".format(operation.goto))

        elif operation.op2 == "!=":
            op_seq += ("\t\tdcmpl\n")
            op_seq += ("\t\tifeq {}\n".format(operation.goto))

        elif operation.op2 == ">":
            op_seq += ("\t\tdcmpl\n")
            op_seq += ("\t\tifle {}\n".format(operation.goto))

        elif operation.op2 == ">=":
            op_seq += ("\t\tdcmpl\n")
            op_seq += ("\t\tiflt {}\n".format(operation.goto))

        elif operation.op2 == "<":
            op_seq += ("\t\tdcmpg\n")
            op_seq += ("\t\tifge {}\n".format(operation.goto))

        elif operation.op2 == "<=":
            op_seq += ("\t\tdcmpg\n")
            op_seq += ("\t\tifgt {}\n".format(operation.goto))

        return op_seq


    def build_goto(self, operation, symbol_table):
        """Build stack code for "goto label" operation
        
        operator -> goto
        op1      -> Label to go to
        op2      -> None
        op3      -> None
        arith_op -> None
        goto     -> None

        Arguments:
            operation -- Operation to be built.
            symbol_table -- Dictionary describing the symbol table.
        """

        op_seq = ""

        op_seq += ("goto {}\n".format(operation.op1))

        return op_seq


    def build_empty(self, operation, symbol_table):
        """Empty line with label means the return is to be placed
        
        Arguments:
            operation -- [description]
            symbol_table -- [description]
        """

        op_seq = ""

        op_seq += ("return\n")  # Empty line is the end of the program

        return op_seq


    def build_print_var(self, operation, symbol_table):
        """Build stack code for variable print(System.out.println) operation
        
        operator -> print
        op1      -> variable to print
        op2      -> None
        op3      -> None
        arith_op -> None
        goto     -> None

        Arguments:
            operation -- Operation to be built.
            symbol_table -- Dictionary describing the symbol table.
        """

        op_seq = ""

        op_seq += ("getstatic Field java/lang/System out Ljava/io/PrintStream;\n")
        op_seq += "\t\tldc '{}: '\n".format(operation.op1)
        op_seq += ("\t\tinvokevirtual Method java/io/PrintStream print (Ljava/lang/String;)V\n") 

        op_seq += ("\t\tgetstatic Field java/lang/System out Ljava/io/PrintStream;\n")
        op_seq += (self.load_operand(operation.op1, symbol_table))
        op_seq += ("\t\tinvokevirtual Method java/io/PrintStream println (D)V\n")

        return op_seq


    def build_print_arr_int(self, operation, symbol_table):
        """Build stack code for array print(System.out.println) operation

        Array index is an integer
        
        operator -> print
        op1      -> array to print
        op2      -> array integer index
        op3      -> None
        arith_op -> None
        goto     -> None

        Arguments:
            operation -- Operation to be built.
            symbol_table -- Dictionary describing the symbol table.
        """

        op_seq = ""

        op_seq += ("getstatic Field java/lang/System out Ljava/io/PrintStream;\n")
        op_seq += "\t\tldc '{}[{}]: '\n".format(operation.op1, operation.op2)
        op_seq += ("\t\tinvokevirtual Method java/io/PrintStream print (Ljava/lang/String;)V\n") 

        op_seq += ("\t\tgetstatic Field java/lang/System out Ljava/io/PrintStream;\n")
        op_seq += (self.load_array(operation.op1, symbol_table))
        op_seq += ("\t\tsipush {}\n".format(operation.op2))
        op_seq += ("\t\tdaload\n")  # Load correct array index
        op_seq += ("\t\tinvokevirtual Method java/io/PrintStream println (D)V\n")

        return op_seq


    def build_print_arr_var(self, operation, symbol_table):
        """Build stack code for array print(System.out.println) operation

        Array index is a variable
        
        operator -> print
        op1      -> array to print
        op2      -> array variable index
        op3      -> None
        arith_op -> None
        goto     -> None

        Arguments:
            operation -- Operation to be built.
            symbol_table -- Dictionary describing the symbol table.
        """

        op_seq = ""

        op_seq += ("getstatic Field java/lang/System out Ljava/io/PrintStream;\n")
        op_seq += "\t\tldc '{}[{}]: '\n".format(operation.op1, operation.op2)
        op_seq += ("\t\tinvokevirtual Method java/io/PrintStream print (Ljava/lang/String;)V\n") 

        op_seq += ("\t\tgetstatic Field java/lang/System out Ljava/io/PrintStream;\n")
        op_seq += (self.load_array(operation.op1, symbol_table))
        op_seq += (self.load_operand(operation.op2, symbol_table))  # Index
        op_seq += ("\t\td2i\n")  # Converting double to int
        op_seq += ("\t\tdaload\n")  # Load correct array index
        op_seq += ("\t\tinvokevirtual Method java/io/PrintStream println (D)V\n")

        return op_seq


