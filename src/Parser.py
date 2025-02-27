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
    
class Call:
    def __init__(self, var):
        self.value = get_variable(var[:var.index('(')])

    def __str__(self):
        return f"Call:{self.value}()" # NO PARAMS YET
    
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
    def __init__(self, name:Variable, parameters=None, body=None, ret:Value=None):
        if body is None: body = []
        if parameters is None: parameters = []
        self.id = name
        self.parameters = parameters
        self.body = body
        self.ret = ret

    def __str__(self):
        return f"Function (Name:{self.id}, Param:{self.parameters}, Return:{self.ret}, Body:({", ".join([str(x) for x in self.body])}))"
        
class Print:
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return f"Printing: ({self.expression})"

def get_variable(var):
    if var not in VAR_DICT: VAR_DICT[var] = "_" + hashlib.md5(var.encode()).hexdigest()[:6]
    return VAR_DICT[var]

def parse_function(tokens, main:bool = False):
    if main:
        name = tokens.pop(0)[1]
        tokens.pop(0)
        body = parse(tokens[:tokens.index(('RBRACE', '}'))]) # WONT WORK WITH IFS
        tokens = tokens[tokens.index(('RBRACE', '}')):]
        tokens.pop(0)
        return Function(name, body=body)
    return Function()
    
def parse_type(token): # TODO CALL FUNCTION WONT WORK CAUSE OF PARENTHESIS
    if token[0] == 'VARIABLE': return Variable(token[1])
    elif token[0] == 'CALL': return Call(token[1])
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
        func = parse_function(tokens, True)
        return func
    # elif tokens[0][0] == 'VARIABLE' and :
    #     pass
    elif tokens[0][0] == 'PRINT':
        tokens.pop(0)
        tokens.pop(0)
        expr = parse_operation(tokens)
        tokens.pop(0)
        tokens.pop(0)
        return Print(expr)

def parse(t):
    ast = []
    global tokens
    tokens = t
    check = tokens
    while tokens:
        ast.append(parse_statement(tokens))
        if tokens == check and tokens: Error.throw(Error.SyntaxError(tokens[0], tokens))
        check = tokens
    return ast

def test(t):
    print(", ".join([str(x) for x in parse(t)]))