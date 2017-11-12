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
                        "empty": self.build_empty}


    def declare_arr(self, variable):
        """Declare double array of 1000 positions

        Arguments:
            variable -- Variable name.
        """

        print("\t\tsipush 1000")  # 1000 positions
        print("\t\tnewarray double")
        print("\t\tastore {}".format(variable.pos))


    def is_variable(self, name):
        """Check if name is a valid variable name using regex
        
        Arguments:
            name -- Name to be matched.
        """

        variable_pattern = re.compile("^[a-zA-Z_$][a-zA-Z_$0-9]*")
        return bool(variable_pattern.match(name))


    def load_operand(self, op, symbol_table):
        """Load operand according to its type(constant or variable)
        
        Arguments:
            op -- Operand.
            symbol_table -- Dictionary describing the symbol table.
        """

        if self.is_variable(op):
            op = symbol_table[op]
            print("\t\tdload {}".format(op.pos))
        else:
            print("\t\tldc2_w {}".format(float(op)))


    def load_array(self, arr, symbol_table):
        """Load array pointer
        
        Arguments:
            array -- Array to be loaded.
            symbol_table -- Dictionary describing the symbol table.
        """

        arr = symbol_table[arr]
        print("\t\taload {}".format(arr.pos))


    def store_variable(self, op, symbol_table):
        """Store double variable
        
        Arguments:
            op -- Operand.
            symbol_table -- Dictionary describing the symbol table.
        """

        op = symbol_table[op]
        print("\t\tdstore {}".format(op.pos))


    def store_array(self, arr, symbol_table):
        """Store position in array of doubles
        
        Arguments:
            arr -- Array to be stored.
            symbol_table -- Dictionary describing the symbol table.
        """

        arr = symbol_table[arr]
        print("\t\tastore {}".format(arr.pos))


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
        """

        self.load_operand(operation.op2, symbol_table)
        self.store_variable(operation.op1, symbol_table)


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
        """
        
        self.load_operand(operation.op2, symbol_table)
        self.load_operand(operation.op3, symbol_table)
        
        if operation.arith_op == "+":
            print("\t\tdadd")
        elif operation.arith_op == "-":
            print("\t\tdsub")
        elif operation.arith_op == "*":        
            print("\t\tdmul")
        elif operation.arith_op == "/":
            print("\t\tddiv")

        self.store_variable(operation.op1, symbol_table)


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
        """

        # Get correct index
        self.load_operand(operation.op3, symbol_table)
        print("\t\tldc2_w 8.0")
        print("\t\tddiv")
        self.store_variable(operation.op3, symbol_table)

        # Load array position
        self.load_array(operation.op2, symbol_table)  # Array pointer(initial position)
        self.load_operand(operation.op3, symbol_table)  # Corrected index
        print("\t\td2i")  # Converting double to int
        print("\t\tdaload")  # Load correct array index
        self.store_variable(operation.op1, symbol_table)


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
        """

        # Get correct index
        self.load_operand(operation.op2, symbol_table)
        print("\t\tldc2_w 8.0")
        print("\t\tddiv")
        self.store_variable(operation.op2, symbol_table)

        # Load array position
        self.load_array(operation.op1, symbol_table)  # Array pointer(initial position)
        self.load_operand(operation.op2, symbol_table)  # Corrected index
        print("\t\td2i")  # Converting double to int
        self.load_operand(operation.op3, symbol_table)
        print("\t\tdastore")  # Load correct array index


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
        """

        self.load_operand(operation.op1, symbol_table)
        self.load_operand(operation.op3, symbol_table)

        if operation.op2 == "==":
            print("\t\tdcmpl")
            print("\t\tifeq {}".format(operation.goto))

        elif operation.op2 == "!=":
            print("\t\tdcmpl")
            print("\t\tifne {}".format(operation.goto))

        elif operation.op2 == ">":
            print("\t\tdcmpl")
            print("\t\tifgt {}".format(operation.goto))

        elif operation.op2 == ">=":
            print("\t\tdcmpl")
            print("\t\tifge {}".format(operation.goto))

        elif operation.op2 == "<":
            print("\t\tdcmpg")
            print("\t\tiflt {}".format(operation.goto))

        elif operation.op2 == "<=":
            print("\t\tdcmpg")
            print("\t\tifle {}".format(operation.goto))


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
        """

        self.load_operand(operation.op1, symbol_table)
        self.load_operand(operation.op3, symbol_table)


        if operation.op2 == "==":
            print("\t\tdcmpl")
            print("\t\tifne {}".format(operation.goto))

        elif operation.op2 == "!=":
            print("\t\tdcmpl")
            print("\t\tifeq {}".format(operation.goto))

        elif operation.op2 == ">":
            print("\t\tdcmpl")
            print("\t\tifle {}".format(operation.goto))

        elif operation.op2 == ">=":
            print("\t\tdcmpl")
            print("\t\tiflt {}".format(operation.goto))

        elif operation.op2 == "<":
            print("\t\tdcmpg")
            print("\t\tifge {}".format(operation.goto))

        elif operation.op2 == "<=":
            print("\t\tdcmpg")
            print("\t\tifgt {}".format(operation.goto))


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
        """

        print("\t\tgoto {}".format(operation.op1))


    def build_empty(self, operation, symbol_table):
        print("\t\treturn")  # Empty line is the end of the program
