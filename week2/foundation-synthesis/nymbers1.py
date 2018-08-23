import re

thelist = []
first = "hello"
while first != 'done':
    first = input("Input first name: \n")
    if first == "done":
        break
    else:    
        thelist.append(first)
        last = str(input("Input last name: \n"))
        thelist.append(last)
        title = str(input("Input job title: \n"))
        thelist.append(title)
        salary = ("${0:.2f}".format(float(input("Input salary: \n"))))
        thelist.append(salary)
    # person = [first, last, title, salary]
    #thelist.append(person)

def chunks(l, n):
    records = []
    for i in range(0 , len(l), n):
        records.append(l[i:i + n])
    return records

def output(filename, records):
    with open(filename, "w") as fileobject:
        for person in records:
            print("\"{}\" \"{}\" \"{}\" {}".format(person[0],person[1],person[2],person[3]),file=fileobject)
    

output("x", chunks(thelist,4))

# print(chunks(thelist, 4))
# print(chunks(thelist, 4))



'''
def output_lines(filename):
    with open(filename, 'w') as open_file:
        for person in thelist:
            print(person)

output_lines("textfile2.txt")
'''
