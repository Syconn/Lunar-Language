# Compiler
from Lexer import tokenize_line
from Parser import parse
from Compiler import write_code
from subprocess import call

fileName = "basic_test.c"
tokens = tokenize_line("print(5 + 20); // Hey Im a Comment")
ast = parse(tokens)
write_code(fileName, ast)

# Generate and Executes Code
call(["gcc", fileName, "-o", fileName[:-2]])
call(["rm", fileName])
# call("./a")