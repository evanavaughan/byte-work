def paycheck(hours, wage):

    if hours <= 40:
        paycheck = wage*hours
        print(paycheck)
    else:
        paycheck = ((hours-40)*1.5*wage + 40*wage)
        print(paycheck)
    

hours = float(input("How many hours did you work?\n"))
wage = float(input("What is your hourly wage?\n"))


paycheck(40, 10.50)
print return()

