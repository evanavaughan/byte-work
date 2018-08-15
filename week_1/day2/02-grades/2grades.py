x = float(input("Enter a number between 0.0 and 1.0: "))

if x < 0 or x > 1:
    print("Sorry, you've made an error.")

if x > 0.9:
    print("The grade is an A")

if 0.8 <= x <= 0.9:
    print("The grade is a B")
elif 0.7 <= x <= 0.8:
    print("The grade is a C")
elif 0.6 <= x <= 0.7:
    print("The grade is a D")
else:
    print("The grade is an F")

if x > 0.9:
    grade = "A"

if 0.8 <= x <= 0.9:
    grade = "B"
elif 0.7 <= x <= 0.8:
    grade = "C"
elif 0.6 <= x <= 0.7:
    grade = "D"
else:
    grade = "F"

print("Your grade is a " + grade)