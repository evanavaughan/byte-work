min_worked = dict()
userids = []

userid = int(input("what is your user ID?"))
if userid == 0:
    print(min_worked)
else:
    hours = int(input("how many hours did you work?:"))
    if userid not in min_worked:
        min_worked[userid] = hours
    else:
        min_worked[userid] = min_worked[userid] + hours

print(min_worked)


"""

min_worked = openfile("hours.json")

else:
#insert userID in dictionary

if userid > 0:
    #read file
    if userid in min_worked == True:
#update key
    hours = input("How many minutes did you work today?:\n")
    #update text file w/ employee ID & hours
    for hours in filename:

elif userid = 0:
    # boss' employee ID, print all userIDs w/ hours
    print('Employee ID: Minutes Worked')
    for userID,hours in min_worked.items():
        print(userID, hours)
        print(min_worked)

else:
    userid = int(input("put in a user ID that is a number 0 or greater:"))

    def write_json(filename, dictionary=example_dict):
    with open(filename, 'w') as jsonfile:
        json.dump(dictionary, jsonfile)

def openfile(filename):
    with open(filename, 'r') as fileobject:
        return json.load(fileobject)


# min_worked.get(userid, "default")
"""