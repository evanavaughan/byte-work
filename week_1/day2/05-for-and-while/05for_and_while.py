#* Write a program that inputs an integer from the user and then prints the numbers from 0 to that integer (including that integer)

x = int(input("Please enter a number: "))
for x in range(x+1):
    print(x)

#* Now make it input a second integer and print every even number from 0 until the given number.

y = int(input("Please enter a second number: "))
for y in range(0,y+1,2):
    print(y)

#* Write this program using both a step value for range and using an if test with % inside your loop.
x = int(input("Please enter a third number: "))

for x in range(0, x+1):
    if x%2 == 0:
        print(x)





