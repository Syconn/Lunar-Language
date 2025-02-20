# Lexer: Tokenizer
import re

# https://www.w3schools.com/python/python_regex.asp
TOKEN_REGEX = [
    # Functions
    (r'\bprint\b', 'PRINT'),

    # Variables
    (r'\bbool\b', 'BOOL'),
    (r'\bint\b', 'INT'),
    (r'\bstr\b', 'STRING'),

    # Method Names, Variable Names, String Values
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'), 

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
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r';', 'SEMICOLON'),

     # Ignore spaces
    (r'\s+', None)
]

def tokenize_line(code):
    tokens = []
    while code:
        for pattern, token_type in TOKEN_REGEX:
            match = re.match(pattern, code)
            if match:
                if token_type == 'COMMENT':
                    code = ""
                    break
                elif token_type:
                    tokens.append((token_type, match.group(0)))
                code = code[len(match.group(0)):]
                break
        else:
            raise SyntaxError(f"Unexpected character: {code[0]}")
    return tokens

def tokenize_lines(lines):
    tokens = []
    for line in lines:
        tokens += tokenize_line(line)
    return tokens