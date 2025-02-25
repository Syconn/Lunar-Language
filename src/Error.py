class Error:
    def message(self):
        pass

class SyntaxError(Error):
    def __init__(self, unknown, output):
        self.unknown = unknown
        self.output = output

    def message(self):
        return f"Syntax Error, unknow value {self.unknown} in {self.output}"

class TypeError(Error):
    def __init__(self, line, symbol):
        self.line = line
        self.symbol = symbol

    def message(self):
        return f"TypeError at {self.line}, unkown symbol {self.symbol}"

def throw(error: Error):
    print(error.message())
    exit(1)