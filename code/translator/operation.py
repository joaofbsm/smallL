#!/usr/bin/env python3

"""Operation structural representation"""

__author__ = "João Francisco B. S. Martins and Pedro Dalla Vechia Chaves"
__email__ = "joaofbsm@dcc.ufmg.br, pedrodallav@dcc.ufmg.br"
__license__ = "GPL"
__version__ = "3.0"


class Operation:
    def __init__(self, operator, op1, op2, op3, arith_op, goto):
        self.operator = operator
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.arith_op = arith_op
        self.goto = goto
