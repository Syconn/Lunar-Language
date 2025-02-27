# Lexer: Tokenizer
import re
import Error

TYPES = [
    'BOOL', 
    'INT',
    'FLOAT',
    'STRING'
]

TOKEN_REGEX = [ # https://www.w3schools.com/python/python_regex.asp
    # Functions
    (r'\bprint\b', 'PRINT'),
    (r'\bmain\b', 'MAIN'),

    # Variables
    (r'\bbool\b', 'BOOL'),
    (r'\bint\b', 'INT'),
    (r'\bstr\b', 'STRING'),

    # Method Names, Variable Names, String Values
    (r'[a-zA-Z_][a-zA-Z0-9_]*\(\)', 'CALL'), 
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'VARIABLE'), 

    # Operators
    (r'tr', 'TRUE'),
    (r'fal', 'FALSE'),
    (r'and', 'AND'),
    (r'&&', 'AND'),
    (r'\|\|', 'OR'),
    (r'or', 'OR'),
    (r'//', 'INTEGER_DIVIDE'),
    (r'\*\*', 'EXPONENT'),
    (r'%', 'MODULUS'),
    (r'==', 'EQUALITY'),
    (r'!=', 'INEQUALITY'),
    (r'\d+', 'NUMBER'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'MULTIPLY'),
    (r'/', 'DIVIDE'),
    (r'=', 'EQUALS'),

    # Body Controls
    (r'\"', 'QUOTATION'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r';', 'SEMICOLON'),
    (r'\{', 'LBRACE'),
    (r'\}', 'RBRACE'),
    (r'\s+', None)    
]

def tokenize_line(code, line):
    tokens = []
    while code:
        for pattern, token_type in TOKEN_REGEX:
            match = re.match(pattern, code)
            if match:
                if token_type == 'COMMENT':
                    code = ""
                    break
                elif token_type == 'QUOTATION':
                    code = code[1:]
                    tokens.append(('STRING', code[:code.index('"')]))
                    code = code[code.index('"'):]
                elif token_type:
                    tokens.append((token_type, match.group(0)))
                code = code[len(match.group(0)):]
                break
        else:
            Error.throw(Error.TypeError(line, code[0]))
    return tokens

def tokenize_lines(lines):
    tokens = []
    for num, line in enumerate(lines):
        tokens += tokenize_line(line, num)
    return tokens