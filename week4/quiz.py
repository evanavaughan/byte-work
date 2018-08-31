def input_hours():
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
