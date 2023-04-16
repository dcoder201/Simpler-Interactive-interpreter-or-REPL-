class Interpreter:
    def __init__(self):
        self.variables = {}

    def input(self, expression):
        tokens = self.tokenize(expression)
        result = self.evaluate(tokens)
        if result is None:
            return ""
        else:
            return int(result)

    def tokenize(self, expression):
        tokens = []
        i = 0
        while i < len(expression):
            c = expression[i]
            if c.isspace():
                i += 1
            elif c.isdigit() or c == ".":
                start = i
                while i < len(expression) and (expression[i].isdigit() or expression[i] == "."):
                    i += 1
                tokens.append(expression[start:i])
            elif c.isalpha() or c == "_":
                start = i
                while i < len(expression) and (expression[i].isalnum() or expression[i] == "_"):
                    i += 1
                tokens.append(expression[start:i])
            elif c in "+-*/%()=":
                tokens.append(c)
                i += 1
            else:
                raise ValueError(f"Invalid character: {c}")
        return tokens

    def evaluate(self, tokens):
        if not tokens:
            return None
        elif len(tokens) == 1:
            return self.evaluate_token(tokens[0])
        elif "=" in tokens:
            index = tokens.index("=")
            variable = tokens[index - 1]
            value = self.evaluate(tokens[index + 1:])
            self.variables[variable] = value
            return int(value)
        else:
            for op in ["+", "-", "*", "/", "%"]:
                if op in tokens:
                    index = tokens.index(op)
                    left = self.evaluate(tokens[:index])
                    right = self.evaluate(tokens[index + 1:])
                    if op == "+":
                        return left + right
                    elif op == "-":
                        return left - right
                    elif op == "*":
                        return left * right
                    elif op == "/":
                        return left / right
                    elif op == "%":
                        return left % right
            raise ValueError("Invalid expression")

    def evaluate_token(self, token):
        if token in self.variables:
            return self.variables[token]
        elif "." in token:
            return int(token)
        else:
            return int(token)   
