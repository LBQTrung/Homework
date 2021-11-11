import pickle
class Person:
    def __init__(self,name = None,phoneNumber = None,email = None):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email

    def outputInfo(self):
        return f"Name: {self.name}, Phone: {self.phoneNumber}, Email: {self.email}"
    
    def checkClass(self):
        return "Person" 

class Student(Person):
    def __init__(self,name = None,phoneNumber = None,email = None,studentNumber=None,averageMark=None):
        super().__init__(name,phoneNumber,email)
        self.studentNumber = studentNumber
        self.averageMark = averageMark

    def outputInfo(self):
        return f"Name: {self.name}, Phone: {self.phoneNumber}, Email: {self.email}, Student Number: {self.studentNumber}, Average Mark: {self.averageMark}"
    
    def checkClass(self):
        return "Student"

class Professor(Person):
    def __init__(self,name=None,phoneNumber=None,email=None,salary=None):
        super().__init__(name,phoneNumber,email)
        self.salary = salary
    
    def outputInfo(self):
        return f"Name: {self.name}, Phone: {self.phoneNumber}, Email: {self.email}, salary: {self.salary}"
    
    def checkClass(self):
        return "Professor"

''' Function: Input list include 10 object
    Input: List hold object
    Output: List hold object after inputting
'''
def inputClassList(objectList):
    for i in range(0,10):
        print(i+1)
        #Input information of person
        inputName = input("Enter the name: ")
        inputPhoneNumber = input("Enter the phone number: ")
        inputEmail = input("Enter the email address: ")
        #assign value to object
        objectList[i].name = inputName
        objectList[i].phoneNumber = inputPhoneNumber
        objectList[i].email = inputEmail
        if objectList[i].checkClass() == "Person":
            continue
        elif objectList[i].checkClass() == "Student":
            #Input information of student
            inputStudentNumber = input("Enter the student number: ")
            inputAverageMark = input("Enter the average mark: ")
            #assign value to object
            objectList[i].studentNumber = inputStudentNumber
            objectList[i].averageMark = inputAverageMark
        else:
            #input information of professor
            inputSalary = input("Enter the salary: ")
            #assign value to object
            objectList[i].salary = inputSalary
    return objectList


def main():
    #Class Person
    #Initialize list include object of class Person
    personList = [Person() for i in range(0,10)]
    inputClassList(personList)
    #Sort list of people descending with name
    personList.sort(key = lambda x: x.name(), reverse = True)
    #Save file with Pickle
    file1 = open("Person","wb")
    pickle.dump(personList, file1)
    file1.close()
    #Read file and print screen
    file1 = open("Person","rb")
    print("Person list:")
    for i in range(0,10):
        print(pickle.load(file1)[i].outputInfo()) # Because pickload(file1) is list include object of class Person
    file1.close()
    

    #Class Student
    #Initialize list include object of class Student 
    studentList = [Student() for i in range(0,10)]
    inputClassList(studentList)
    #Sort list of student descending with average mark
    studentList.sort(key = lambda x: x.average_mark, reverse = True)
    #Save file with Pickle
    file2 = open("Student","wb")
    pickle.dump(studentList, file2)
    file2.close()
    #Read file and print screen
    file2 = open("Student","rb")
    print("Student list:")
    for i in range(0,10):
        print(pickle.load(file2)[i].outputInfo()) # Because pickload(file2) is list include object of class Student
    file2.close()

    #Class Professor
    #Initialize list include object of class Professor 
    professorList = [Professor for i in range(0,10)]
    inputClassList(professorList)
    #Sort list of professor ascending with salary
    professorList.sort(key = lambda x: x.salary)
    #Save file with Pickle
    file3 = open("Professor","wb")
    pickle.dump(professorList, file3)
    file3.close()
    #Read file and print screen
    file3 = open("Professor","rb")
    print("Professor list:")
    for i in range(0,10):
        print(pickle.load(file3)[i].outputInfo()) # Because pickload(file3) is list include object of class Professor
    file3.close()

if __name__ == "__main__":
    main()

