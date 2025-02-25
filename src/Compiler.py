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
            if (files): lunarFiles += files
    return lunarFiles

def get_lines(paths):
    lines = []
    for path in paths:
        with open(path) as file:
            lines += [clean_line(line) for line in file if clean_line(line) != ""]
    return lines

def clean_line(line):
    return remove_comments(line).replace("\n", "").strip()

def remove_comments(line):
    if ('//' in line): line = line[:line.find('//')]
    if ('#' in line): line = line[:line.find('#')]
    return line

def generate_code(ast):
    code = "#include <stdio.h>\nint main() {\n"
    for stmt in ast:
        if isinstance(stmt, Parser.Print):
            expr = stmt.expression
            if isinstance(expr, Parser.BinaryOp):
                code += f"    printf(\"%d\\n\", {expr.left.value} {expr.op} {expr.right.value});\n"
            else:
                code += f"    printf(\"%d\\n\", {expr.value});\n"
        elif isinstance(stmt, Parser.AssignmentOp):
            code += f"    {stmt.type} {stmt.var} = {stmt.value};\n"
    code += "    return 0;\n}"
    return code


def write_file(fileName, code):
    with open(fileName, 'w+') as file:
        file.write(code)

def write_code(fileName, ast):
    write_file(fileName + ".c", generate_code(ast))

def get_file_name(files): # Name after first file or file with main function
    return files[0]

def get_lunar(): 
    lunarFiles = find_files()
    if (not lunarFiles): return []
    return [get_lines(lunarFiles), get_file_name(lunarFiles)]

def get_file_data(fileName):
    return [fileName, fileName[:-5] if ".moon" in fileName else fileName, 
            fileName[:-5] + ".c" if ".moon" in fileName else fileName]