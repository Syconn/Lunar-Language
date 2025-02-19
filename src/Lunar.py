# Compiler
import Lexer
import Parser
import Compiler
import subprocess
import os

# Finds programming Files (Searches for files in src directory | main director)
print(Compiler.find_files())

# # Interprets Code
# fileName = "basic_test.c" # TODO Need to do Error Handling Somehow
# tokens = Lexer.tokenize_line("print(5 + 20); // Hey Im a Comment")
# ast = Parser.parse(tokens)
# Compiler.write_code(fileName, ast)

# # Generate and Executes Code
# subprocess.call(["gcc", fileName, "-o", fileName[:-2]])
# os.remove(fileName)
# subprocess.call("./" + fileName[:-2])