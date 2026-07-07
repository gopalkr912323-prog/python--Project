# Student Management System

students = []

# ---------------- Add Student ----------------
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "Roll": roll,
        "Name": name,
        "Age": age,
        "Course": course
    }

    students.append(student)
    print("\nStudent Added Successfully!\n")


# ---------------- View Students ----------------
def view_students():
    if len(students) == 0:
        print("\nNo Student Found!\n")
    else:
        print("\n----- Student List -----")
        for student in students:
            print("---------------------------")
            print("Roll   :", student["Roll"])
            print("Name   :", student["Name"])
            print("Age    :", student["Age"])
            print("Course :", student["Course"])
        print("---------------------------\n")


# ---------------- Search Student ----------------
def search_student():
    roll = input("Enter Roll Number to Search: ")

    for student in students:
        if student["Roll"] == roll:
            print("\nStudent Found")
            print("Name   :", student["Name"])
            print("Age    :", student["Age"])
            print("Course :", student["Course"])
            return

    print("\nStudent Not Found!\n")


# ---------------- Delete Student ----------------
def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["Roll"] == roll:
            students.remove(student)
            print("\nStudent Deleted Successfully!\n")
            return

    print("\nStudent Not Found!\n")


# ---------------- Main Menu ----------------
while True:

    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice!\n")