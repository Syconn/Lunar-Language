# Parser: AST

class Number:
    def __init__(self, value):
        self.value = int(value)

    def __str__(self):
        return f"Number: {self.value}"

class BinaryOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f"Operation: {self.left} {self.op} {self.right}"
    
class Print:
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return f"Printing: {self.expression}"

def parse_operation(tokens):
    left = Number(tokens.pop(0)[1])  # First number
    while tokens and tokens[0][0] in ('PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE'):
        op = tokens.pop(0)[1]  # Operator
        right = Number(tokens.pop(0)[1])  # Next number
        left = BinaryOp(left, op, right)
    return left

def parse_statement(tokens):
    print(tokens)
    if tokens[0][0] == 'PRINT':
        tokens.pop(0)  # Remove 'PRINT'
        tokens.pop(0)  # Remove '('
        expr = parse_operation(tokens)
        tokens.pop(0)  # Remove ')'
        tokens.pop(0)  # Remove ';'
        return Print(expr)
    elif tokens[0][0] == 'NUMBER':
        return parse_operation(tokens)

def parse(tokens):
    ast = []
    while tokens: ast.append(parse_statement(tokens))
    return ast

def test(tokens):
    print("".join([str(x) + " | " for x in parse(tokens)]))