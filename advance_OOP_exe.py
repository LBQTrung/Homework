class person:
    def __init__(self):
        self.name = ""
        self.phone_number = ""
        self.email = ""
    def input_info(self):
        self.name = input("Input name: ")
        self.phone_number = input("Input phone number: ")
        self.email = input("Nhập email ")
    @property #Take the last name to sort as an attribute
    def last_name(self):
        split_name = (self.name).split(" ")
        a = split_name[len(split_name)-1]
        return a
    def output_info(self):
        return self.name + "," + self.phone_number + "," + self.email
    def list_header():
        return "name,phone number,email"

class student(person):
    def __init__(self):
        super().__init__()
        self.student_number = ""
        self.average_mark = 0
    def input_info(self):
        super().input_info()
        self.student_number = input("Input student number: ")
        self.average_mark = float(input("Input average mark: "))
    def output_info(self):
        return self.name + "," + self.phone_number + "," + self.email + "," + self.student_number + "," + str(self.average_mark)
    def list_header():
        return "name,phone number,email,student number, average mark"

class professor(person):
    def __init__(self):
        super().__init__()
        self.salary = 0
    def input_info(self):
        super().input_info()
        self.salary = float(input("Input salary(USD): "))
    def output_info(self):
        return self.name + "," + self.phone_number + "," + self.email + ","  + str(self.salary)
    def list_header():
        return "name,phone number,email,salary"

def input_list(list_name):    
    for i in range(0,10):
        print(str(i+1) + ". Input information: ")
        list_name[i].input_info()
    return list_name

def output_list(list_name):
    for i in range(0,10):
        print(list_name[i].output_info())

def write_to_file(file_name, class_name, list_name):
    file_name.write(class_name.list_header())
    file_name.write("\n")
    for i in range(0,10):
        file_name.write(list_name[i].output_info())
        file_name.write("\n")

def main():
    #Input and sort list of people descending with name:
    people_list = [person() for i in range(0,10)]
    input_list(people_list)
    people_list.sort(key = lambda x: x.last_name, reverse = True)

    #Input and sort list of student descending with average mark:
    student_list = [student() for i in range(0,10)]
    input_list(student_list)
    student_list.sort(key = lambda x: x.average_mark, reverse = True)

    #Input and sort list of professor ascending with salary
    professor_list = [professor() for i in range(0,10)]
    input_list(professor_list)
    professor_list.sort(key = lambda x: x.salary)

    #Output 3 list
    output_list(people_list)
    print("-------------------------------------")
    output_list(student_list)
    print("-------------------------------------")
    output_list(professor_list)

    #Open file to write 
    file1 = open("list1.txt","w")
    file2 = open("list2.txt","w")
    file3 = open("list3.txt","w")

    write_to_file(file1,person,people_list)
    write_to_file(file2,student,student_list)
    write_to_file(file3,professor,professor_list)

    #Close file written
    file1.close()
    file2.close()
    file3.close()

    #Open file to read 
    file1 = open("list1.txt","r")
    file2 = open("list2.txt","r")
    file3 = open("list3.txt","r")

    #Em trả về danh sách là string nên không dùng pickle được
    print(file1.read())
    print("-------------------------------------")
    print(file2.read())
    print("-------------------------------------")
    print(file3.read())

    #Close file read
    file1.close()
    file2.close()
    file3.close()

if __name__ == "__main__":
    main()

