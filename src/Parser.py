# Parser: AST

class Number:
    def __init__(self, value):
        self.value = int(value)

class BinaryOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Print:
    def __init__(self, expression):
        self.expression = expression

def parse_expression(tokens):
    """Parses expressions like 5 + 3"""
    left = Number(tokens.pop(0)[1])  # First number
    while tokens and tokens[0][0] in ('PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE'):
        op = tokens.pop(0)[1]  # Operator
        right = Number(tokens.pop(0)[1])  # Next number
        left = BinaryOp(left, op, right)
    return left

def parse_statement(tokens):
    """Parses statements like print(5 + 3);"""
    if tokens[0][0] == 'PRINT':
        tokens.pop(0)  # Remove 'PRINT'
        tokens.pop(0)  # Remove '('
        expr = parse_expression(tokens)
        tokens.pop(0)  # Remove ')'
        tokens.pop(0)  # Remove ';'
        return Print(expr)

def parse(tokens):
    ast = []
    while tokens:
        ast.append(parse_statement(tokens))
    return ast
