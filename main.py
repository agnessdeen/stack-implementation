import re

def read_input_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def write_output_file(filename, results):
    with open(filename, 'w') as file:
        for result in results:
            file.write(f"{result:.2f}\n")

def precedence(op):
    return {'+':1, '-':1, '*':2, '/':2}.get(op, 0)

def infix_to_postfix(expression):
    output = []
    stack = []
    tokens = re.findall(r'\d+\.?\d*|[()+\-*/]', expression)
    for token in tokens:
        if token.isnumeric() or re.match(r'\d+\.\d+', token):
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(token) <= precedence(stack[-1]):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output

def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        if token.isnumeric() or re.match(r'\d+\.\d+', token):
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a / b)
    return stack[0]

def main():
    expressions = read_input_file('input.txt')
    results = []
    for expr in expressions:
        postfix = infix_to_postfix(expr)
        result = evaluate_postfix(postfix)
        results.append(result)
    write_output_file('output.txt', results)

if __name__ == "__main__":
    main()
