'''
def fizz_buzz(x):
    for i in range(1,21):
        if i == x:
            pass
        elif i %3 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0 and i%5 != 0:
            print("Fizz")
        elif i%5 == 0 and i%3 != 0:
            print("Buzz")
        else:
            print(i)
fizz_buzz(12)

#nested loops and triangles
def pypart(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
    print("\r")

pypart(10)
'''
def fahrenheit_to_celsius(temp):
    f = int(input("What is the temperature?\n"))
    cel = (f - 32) * 5/9
    return cel
    pass

def celsius_to_fahrenheit(temp):
    cel = int(input("What is the temperature?\n"))
    f = (c * 9/5) + 32
    return f
    pass
'''