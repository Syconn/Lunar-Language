# Compiles Code: C Based
import Parser
import os

def find_files(path = os.path.curdir, ext = ".moon"):
    lunarFiles = []
    for subPath in os.scandir(path):
        if (subPath.name.endswith(ext)):
            lunarFiles.append(subPath.path)
        elif (subPath.is_dir()):
            files = find_files(path=subPath.path)
            if (files): lunarFiles.append(files)
    return lunarFiles

def generate_code(ast):
    code = "#include <stdio.h>\nint main() {\n"
    for stmt in ast:
        if isinstance(stmt, Parser.Print):
            expr = stmt.expression
            if isinstance(expr, Parser.BinaryOp):
                code += f"    printf(\"%d\\n\", {expr.left.value} {expr.op} {expr.right.value});\n"
            else:
                code += f"    printf(\"%d\\n\", {expr.value});\n"
    code += "    return 0;\n}"
    return code


def write_file(fileName, code):
    with open(fileName, 'w+') as file:
        file.write(code)

def write_code(fileName, ast):
    write_file(fileName, generate_code(ast))