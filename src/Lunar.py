# Compiler
from Lexer import tokenize_line
from Compiler import generate_code
from Parser import parse



tokens = tokenize_line("print(5 + 8); // Hey Im a Comment")
ast = parse(tokens)
code = generate_code(ast)
print(code)