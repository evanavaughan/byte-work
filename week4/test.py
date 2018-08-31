import json

the_file = "hours.json"

def open_file(filename):
    with open(filename, 'r') as fileobject:
        opened_file = json.load(fileobject)

min_worked = open_file(the_file)

def input_hours():
    userid = int(input("what is your user ID?"))
    if userid == 0:
        #for aaa,value in tesla_dictionary.items():
        #    print(aaa, value)
        print("Employee ID : Hours Worked")
        for userid,hours in min_worked.items():
            print(userid, hours)
    else:
        hours = int(input("how many hours did you work?:"))
        if userid not in min_worked:
            min_worked[userid] = hours
        else:
            min_worked[userid] = min_worked[userid] + hours
        update_file(the_file)

def update_file(filename, dictionary=min_worked):
        with open(filename, 'w') as jsonfile:
            json.dump(min_worked, jsonfile)

print(min_worked)

openfile("hours.json")





new_dictionary = {
    'Name': tesla_dictionary['Name'],
    'Symbol': tesla_dictionary['Symbol'],
    'LastPrice': tesla_dictionary['LastPrice'],
    'Volume': tesla_dictionary['Volume'],
}

print(new_dictionary)

def write_dictionary(filename, dictionary=new_dictionary):
    with open(filename, 'w') as jsonfile:
        json.dump(dictionary, jsonfile)

write_dictionary('tesla_summary_ev.json')



# min_worked.get(userid, "default")
"""