x = int(input("Please enter a year: "))

if x%4 == 0 and x%400 == 0:
    print("You chose a leap year!")
elif x%100 == 0:
    print("Sorry brah, you didn't choose a leap year.")
else:
    print("You chose a leap year!")



