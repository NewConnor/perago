import sys

'''
    IDENT
    NUM
    STR
    ASSIGN
    PLUS
    MINUS
    MULTIP
    DIVIDE
    MODUL
    WSPACE
    ERROR
'''

class Lexer:
    def __init__(self):
        self.serial = ""

    def SCAN_IDENT(self, string=""):
        if string[0].isalpha() or string[0] == '_':
            for i in range(len(string)):
                if string[i].isalnum or string[i] == '_' or string[i] == '.':
                    continue
            else:
                return (string[0:i], "IDENT")
