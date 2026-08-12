# SCHOOL MANAGEMENT SYSTEM

students = []

def add_student():
    name = input("Enter Name : ")
    student_id = int(input("Enter student_id : "))
    marks = int(input("Enter marks : "))


    std_info= {
        "name" : name ,
        "student_id" : student_id,
        "marks" : marks
    }
    students.append(std_info)


    with open("student.txt" , "a") as f:
        f.write(str(std_info) + "\n")
        
        
    print("student successfully added!")


def delete_student():
    student_id = int(input("Enter ID : "))

    
    found = False

    for std_info in students:
        if student_id == std_info["student_id"]:
            students.remove(std_info)
            found = True
            break
    if not found:
        print("Student not found")        

def search_student():
    student_id = int(input("Enter ID : "))

    found = False

    for std_info in students:
        if student_id == std_info["student_id"]:
            print(std_info)
            found = True
            break

    if not found:
        print("Student not found") 


def update_marks():

    student_id = int(input("Enter ID : "))
    
    found = False

    for std_info in students:
        if student_id == std_info["student_id"]:
            new_marks = int(input("Enter new marks"))
            std_info["marks"] = new_marks
            found = True
            break

    if not found:
        print("student not found")            
    

def find_topper():
    if len(students) == 0:
        print("no student added")
        return 
        
    topper = students[0]

    for std_info in students:
        if std_info["marks"] > topper["marks"]:
            topper = std_info
    print(topper)    

def save_student():
    with open("student.txt", "w") as f:
        for student in students:
            f.write(str(student) + "\n")


import ast

with open("student.txt", "r") as f:
    for line in f:
        student = ast.literal_eval(line.strip() )
        students.append(student)


while True:
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Find Topper")
    print("6. Exit")

    choice = int(input("Enter choice: "))


    match choice:
        case 1:
            add_student()
        case 2:
            delete_student()
        case 3:
            search_student()
        case 4:
            update_marks()
        case 5:
            find_topper()
        case 6:
            save_student()
            break
        case _:
            print("Invalid choice")