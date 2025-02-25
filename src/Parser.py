# Parser: AST
from Lexer import TYPES
import Error
import hashlib

VAR_DICT = {}

class Value:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Value:{self.value}"

class Int(Value):
    def __init__(self, value):
        super().__init__(int(value))

    def __str__(self):
        return f"Int:{self.value}"
    
class Float(Value):
    def __init__(self, value):
        super().__init__(float(value))

    def __str__(self):
        return f"Float:{self.value}"
    
class Bool(Value):
    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return f"Bool:{self.value}"
    
class String(Value):
    def __init__(self, value):
        super().__init__(str(value))

    def __str__(self):
        return f"String:{self.value}"
    
class Variable:
    def __init__(self, var):
        self.value = get_variable(var)

    def __str__(self):
        return f"Variable:{self.value}"
    
class BinaryOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f"BinaryOp: ({self.left} {self.op} {self.right})"
    
class AssignmentOp:
    def __init__(self, type, var, value):
        self.type = type
        self.var = get_variable(var)
        self.value = value

    def __str__(self):
        return f"AssignmentOp: ({self.var} {self.value}:{self.type})"
    
class Function:
    def __init__(self, id:Variable, parms:list[(Variable, Value)]=[], body=[], ret:Value=None):
        self.id = id
        self.parms = parms
        self.body = body
        self.ret = ret

    def __str__(self):
        return f"Function:{self.id} (Param:({self.parms}), Return:{self.ret}, Body:({self.body}))"
        
class Print:
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return f"Printing: ({self.expression})"

def get_variable(var):
    if (var not in VAR_DICT): VAR_DICT[var] = "_" + hashlib.md5(var.encode()).hexdigest()[:6]
    return VAR_DICT[var]

def parse_function(tokens, main:bool = False):
    if main:
        id = tokens.pop(0)[1]
        tokens.pop(0)
        body = parse(tokens[:tokens.index(('RBRACE', '}'))])
        tokens.pop(0)
        return Function(id, body=body)
    return Function()
    
def parse_type(token):
    if token[0] == 'VARIABLE': return Variable(token[1])
    elif token[1].isdecimal(): return Int(token[1])
    elif token[1].replace(".", "", 1).isnumeric(): return Float(token[1])
    elif token[1] == 'true': return Bool(True)
    elif token[1] == 'false': return Bool(False)
    else: return String(token[1])

def parse_operation(tokens):
    left = parse_type(tokens.pop(0))
    while tokens and tokens[0][0] in ('PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE'):
        op = tokens.pop(0)[1]
        right = parse_type(tokens.pop(0))
        left = BinaryOp(left, op, right)
    return left

def parse_assignment(tokens):
    type = tokens.pop(0)[1]
    var = tokens.pop(0)[1]
    tokens.pop(0)
    return AssignmentOp(type, var, tokens.pop(0)[1])

def parse_statement(tokens):
    # Variables
    if tokens[0][0] in TYPES and tokens[2][0] == 'EQUALS':
        assig = parse_assignment(tokens)
        tokens.pop(0)
        return assig

    # Functions
    elif tokens[0][0] == 'MAIN':
        return parse_function(tokens, True)
    # elif tokens[0][0] == 'VARIABLE' and :
    #     pass
    elif tokens[0][0] == 'PRINT':
        print(tokens.pop(0))
        print(tokens.pop(0))
        expr = parse_operation(tokens)
        print(tokens.pop(0))
        print(tokens.pop(0))
        print(tokens)
        return Print(expr)

def parse(tokens):
    ast = []
    check = tokens
    while tokens: 
        ast.append(parse_statement(tokens))
        if tokens == check: Error.throw(Error.SyntaxError(tokens[0], tokens))
    return ast

def test(tokens):
    print("[" + ", ".join([str(x) for x in parse(tokens)])+ "]")