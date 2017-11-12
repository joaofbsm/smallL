#!/usr/bin/env python3

"""Variable structural representation"""

__author__ = "João Francisco B. S. Martins and Pedro Dalla Vechia Chaves"
__email__ = "joaofbsm@dcc.ufmg.br, pedrodallav@dcc.ufmg.br"
__license__ = "GPL"
__version__ = "3.0"


class Variable:
    def __init__(self, name, _type, pos):
        self.name = name
        self._type = _type
        self.pos = pos