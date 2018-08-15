x = int(input("Enter a number:"))
if x == 0:
    print("It is zero!")
else:
    print("It's not zero!")

if x < 10:
    print("Less than 10!")
elif 10 < x < 20:
    print("Less than 20!")
else:
    print("Big number you got there!")

if 0 <= x <= 100:
    print("{:03d}".format(x))

if x%2 == 0:
    print("It is even!")

if x%5 == 0:
    print("It is divisible by 5!")

if x%13 == 0 or x%17 == 0:
    print("Cicadas!")

if x%2 == 0 and x%5 == 0:
    print("It is both even and divisible by 5!")

if x%2 == 0:
    if x%5 == 0:
        print("It is both even and divisible by 5!")

if x%7 != 0:
    print(x*7)
else:
    print(x/2)

