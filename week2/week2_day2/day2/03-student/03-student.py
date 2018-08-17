class Student():
    pass

    def __init__(self, first_name, last_name, age, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades

    def addgrade(self, grade):
        # adds grade to list of grades
        self.grades.append(grade)
        print(self.grades)

    def gpa(self):
        #calculates GPA
        gpa = sum(self.grades)/len(self.grades)
        print(gpa)

student1 = Student('Evan', 'Vaughan', 36, [4,3,3,3])
student1.addgrade(3)
student1.gpa()