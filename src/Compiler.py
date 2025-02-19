# Compiles Code: C Based

from Parser import *

def generate_code(ast):
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


def write_file(fileName, code):
    with open(fileName, 'w+') as file:
        file.write(code)

def write_code(fileName, ast):
    write_file(fileName, generate_code(ast))