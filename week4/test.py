#import json

the_file = "hours.txt"
min_worked = dict()

def open_file(filename):
    with open(filename, 'r') as fileobject:
        return min_worked

def input_hours(filename):
    userid = int(input("what is your user ID?"))
    if userid == 0:
        print("Employee ID : Hours Worked")
        for userid,hours in min_worked.items():
            print(userid, hours)
    else:
        hours = int(input("how many hours did you work?:"))
        if userid not in min_worked:
            min_worked[userid] = hours
        else:
            min_worked[userid] = min_worked[userid] + hours


open_file(the_file)
input_hours(min_worked)


