def rpn(x):
    stack = []
    operators=['+', '-', '*']

    for i in x.split(' '):
        if i in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            if i=='+': result = op2 + op1
            if i=='-': result = op2 - op1
            if i=='*': result = op2 * op1
            stack.append(result)
        else:
            stack.append(float(i))

    return stack.pop()


x = str(input("Enter a polish expression:"))
result = rpn(x)
print (result)