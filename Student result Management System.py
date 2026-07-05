
print("\n\n\t\tStudent result Management System")
print("\n\tMenu")
print("1. Add Student")
print("2. Search Student")
print("3. Show topper")
print("4. Show all student")
print("5. Exit")
select = int(input("\nSelect option: "))

class Add_student:
    def __init__(self, name , m1, m2, m3 , m4 , m5):
        self.name = name
        self.hons1 = m1
        self.hons2 = m2
        self.math = m3
        self.eng = m4
        self.hindi = m5


    def total_marks(self):
        total = self.name + self.hons1 + self.math + self.hindi + self.eng
        print("Total marks : ", total)
    

    def percentage(self):
        print("percentage : ", (self.name + self.hons1 + self.math + self.hindi + self.eng)/5)

    def grade(self):
        if(self.percentage >= 90):
            print("Grade: A")
        elif(self.percentage >= 80):
            print("Grade : B")
        elif(self.percentage >= 70):
            print("Grade : C")
        else:
            print("Grade: D")
        
        

def add_student():
    name = input("Enter your name: ")
    roll = int(input("Enter your roll number: "))
    hons1 = int(input("Enter hons1 marks: "))
    hons2 = int(input("Enter hons2 marks: "))
    math = int(input("Enter math marks: "))
    hindi = int(input("Enter hindi marks: "))
    end = int(input("Enter english marks: "))

def total_marks():
    

# if(select == 1):

