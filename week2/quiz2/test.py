import re
import math

operators = []
def rpn(equation):
    for value in equation:
        if math.isnan(value):
            operators.append(value)


print(rpn("4+5-4-3"))
print(equation)
print(operators)

#iterate through string, take out operators using math.isnan(x), add them back in




'''
def sieve(n):
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            return(i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)

print(sieve(100))
'''