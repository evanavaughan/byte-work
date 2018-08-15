# * A function that returns True if a number is divisible by 7 and False if it does not.
'''
def divisible7(x):
    if x%7 == 0:
        return "True"
    else:
        return "False"

# this just returns the function. it does not print it since the function has not been invoked



# * A function that returns True if a string is 10 characters or longer and False if it does not.

def long_string(x):
    if len(x) < 11:
        return"True"
    else:
        return "False"

x = "1234567890"
long_string(x)



# A function that returns the first letter of a string

def first_letter(x):
    return x[0]

first_letter("Jupiter")

'''

# A function that takes an integer and returns a list with that many elements,
# where every element is zero.
'''
def element_list(x):
    for i in [x] return(0)

y = element_list(6)
print(y)
'''

# * A function that takes a list as input and prints out the contents
# of each element on a numbered line, like:

'''
print_list(['a', 'bee', 'cee', None])
1. a
2. bee
3. cee
4. 'None'
'''
def print_list(x):
    for element in x:
        placeholder = (x.index(element)) + 1
        print(str(placeholder) + " " + element)
        

x = ["a", "b", "c", "d"]
print_list(x)
