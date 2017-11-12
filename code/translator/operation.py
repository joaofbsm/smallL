#!/usr/bin/env python3

"""Operation structural representation"""

__author__ = "João Francisco B. S. Martins and Pedro Dalla Vechia Chaves"
__email__ = "joaofbsm@dcc.ufmg.br, pedrodallav@dcc.ufmg.br"
__license__ = "GPL"
__version__ = "3.0"


class Operation:
    def __init__(self, operator, op1, op2, op3, arith_op, goto):
        """Operation constructor
        
        Arguments:
            operator -- Operation type.
            op1 -- Operand 1.
            op2 -- Operand 2. It may take the form of arithmetic or logical 
                   operators.
            op3 -- Operand 3.
            arith_op -- Special field for arith_attrib operations.
            goto -- Special field for conditional(if) operations.
        """

        self.operator = operator
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.arith_op = arith_op
        self.goto = goto
