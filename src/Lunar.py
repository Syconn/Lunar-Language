# Compiler
import Lexer
import Parser
import Compiler
import subprocess
import os

def run():
    # Interprets Code TODO Need to do Error Handling Somehow
    lunar_files = Compiler.get_lunar()
    if lunar_files:
        file = Compiler.get_file_data(lunar_files[1])
        tokens = Lexer.tokenize_lines(lunar_files[0])
        ast = Parser.parse(tokens)
        print(Compiler.generate_code(ast))

        # Generate and Executes Code
        # subprocess.call(["gcc", file[2], "-o", file[1]])
        # os.remove(file[2]) 
        # subprocess.call("./" + file[1])

if __name__ == '__main__':
    run()