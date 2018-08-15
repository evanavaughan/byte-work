'''
hours = float(input("How many hours did you work?: "))
rate = float(input("What is your rate per hour?: "))

if hours <= 40:
    print(hours*rate)
else:
    print(40*rate+(hours-40)*1.5*rate)
'''
a_list = [2,3,4,5]
def square_list(a_list):
    for number in a_list:
        square = number**2
        print(number,'squared is',square)

square_list(a_list)