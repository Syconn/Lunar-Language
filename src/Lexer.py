# Lexer: Tokenizer
import re

# https://www.w3schools.com/python/python_regex.asp
TOKEN_REGEX = [
    (r'\bprint\b', 'PRINT'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),
    (r'\d+', 'NUMBER'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'MULTIPLY'),
    (r'/', 'DIVIDE'),
    (r'=', 'EQUALS'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r';', 'SEMICOLON'),
    (r'\s+', None),  # Ignore spaces
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