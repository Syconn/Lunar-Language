# Compiler
import Lexer
import Parser
import Compiler
import subprocess
import os

# Interprets Code TODO Need to do Error Handling Somehow
lunarFiles = Compiler.get_lunar()
if lunarFiles:
    file = Compiler.get_file_data(lunarFiles[1])
    tokens = Lexer.tokenize_lines(lunarFiles[0])
    ast = Parser.parse(tokens)
    Compiler.write_code(file[1], ast)

    # Generate and Executes Code
    subprocess.call(["gcc", file[2], "-o", file[1]])
    os.remove(file[2])
    subprocess.call("./" + file[1])