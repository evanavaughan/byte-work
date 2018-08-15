'''
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
'''
hours= 4
def prompt(hours):
    hours = float(input("How many hours did you work?\n"))
    return hours

b = prompt(20)
print(hours)

"""
def computepay(hours, rate):

    if hours > 40:
        reg = rate*hours
        otp = (hours - 40.0) * (rate * .5)
        pay = reg + otp
    else:
        pay = hours * rate
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

xp = computepay(fh,fr)

print("Pay:", xp)

"""