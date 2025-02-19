# Compiler
from Lexer import tokenize_line
from Parser import *

def generate_code(ast): # C Based
    c_code = "#include <stdio.h>\nint main() {\n"
    for stmt in ast:
        if isinstance(stmt, Print):
            expr = stmt.expression
            if isinstance(expr, BinaryOp):
                c_code += f"    printf(\"%d\\n\", {expr.left.value} {expr.op} {expr.right.value});\n"
            else:
                c_code += f"    printf(\"%d\\n\", {expr.value});\n"
    c_code += "    return 0;\n}"
    return c_code

tokens = tokenize_line("print(5 + 8); // Hey Im a Comment")
ast = parse(tokens)
code = generate_code(ast)
print(code)