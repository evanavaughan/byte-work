import re

def get_teachers_info():
    records = []
    while True:
        firstname = input("Enter first name: ")
        if firstname.lower() == "done": break

        lastname = input("Enter last name: ")
        title = input("Enter Title:")
        salary = float(input("Enter salary: "))
        salary = "{:.2f}".format(salary)

        record = [firstname, lastname, title, salary]
        records.append(record)
    return records

def output_teachers_info(filename):
    records = get_teachers_info()
    with open(filename, "w") as openfile:
        for record in records:
            teacher_info = '"{}" "{}" "{}" ${}'.format(record[0], record[1], record[2], record[3])
            print(teacher_info, file = openfile)
    
def create_table_for_teacher(filename):
    records = []
    with open(filename, "r") as openfile:
        for line in openfile:
            first_last_title = re.findall("[a-zA-Z]+\s*[a-zA-Z]*", line)
            salary = re.findall("\$\d+\.\d{2}", line)[0]
            firstname = first_last_title[0]
            lastname = first_last_title[1]
            title = first_last_title[2]
            records.append([firstname, lastname, title, salary])
    line1 = "+------------+------------+--------------------+------------+"
    line2 = "| First Name | Last Name  | Job Title          | Salary     |"
    line3 = "+------------+------------+--------------------+------------+"  
    lastline = "+------------+------------+--------------------+------------+"
    lines = [line1, line2, line3]      
    for record in records:
        string = "| {:<11}| {:<11}| {:<19}|{:<12}|".format(record[0], record[1], record[2], record[3])
        lines.append(string)
    lines.append(lastline)  
    for line in lines:
        print(line)  
    

# 
file = "teacher-info.txt"
output_teachers_info(file)
print(create_table_for_teacher(file))


# #Display a table based on the data in the file. It should be formatted in an attractive way with rows of uniform width and borders. 
# openfile = file.open()
# print(openfile)

# f
# openfile = open(file, 'r')
# fileread = openfile.read()
# openfile.close()
# salary_regex = "\$\d+\.\d{2}"
# pattern = "[a-zA-Z]+\s*[a-zA-Z]+"
# pattern2 = "([a-zA-Z]+\s*[a-zA-Z]+) | (\$\d+\.{2})"
# print(re.findall(pattern, fileread))