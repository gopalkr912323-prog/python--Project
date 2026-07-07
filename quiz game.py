print("-"*40)
print("\n\nYou want to play Quiz game.\na. yes\nb. no")
a = "yes"
b = "no"
select = input("\nSelect Option : ")
print("-"*40)

if(select == "a"):
    print("        let's play Quiz game\n\n")
elif(select == "b"):
    print("ok no problem.\nThank you\nHave a nice day.")
    exit()
else:
    print("wrong input ")
    exit()

result = []
class Question:
    def __init__(self, q1 , a , b , c , d):
        self.q1 = q1
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    
    def print_option(self):
        print(self.q1)
        print("\na. ", self.a )
        print("b. ", self.b)
        print("c.", self.c)
        print("d. ", self.d  )
        

q1 = Question("Q1. What is capital of India ?", "Mumbai", "Kolkata","New Delhi",  "Chennai")
q1.print_option()
ans1 = input("Enter option: ")
result.append(ans1)
print("-"*40)



q2 = Question("\nQ2. Which planet is known as the Red Planet?", "venus", "mars", "jupiter", "Saturn")
q2.print_option()
ans2 = input("Enter option: ")
result.append(ans2)
print("-"*40)


q3 = Question("\nQ3. How many days are there in a leap year?", 364, 365, 366, 367)
q3.print_option()
ans3 = input("Enter option: ")
result.append(ans3)
print("-"*40)


q4 = Question("\nQ4. Which language is primarily used for Data Analysis?", "HTML", "CSS", "PYTHON", "XML")
q4.print_option()
ans4 = input("Enter option: ")
result.append(ans4)
print("-"*40)


q5 = Question("\nQ5. Who is known as the Father of Computers?","Alan Turing", "Charles Babbage","Bill Gates", "Steve Jobs")

q5.print_option()
ans5 = input("Enter option: ")
result.append(ans5)
print("-"*40)
P

q6 = Question("\nQ6.Which data type is used to store multiple values in Python?", "int", "float", "list", "bool")
q6.print_option()
ans6 = input("Enter option: ")
result.append(ans6)
print("-"*40)


q7 = Question("\nQ7. What is the result of 5 × 6?", 25, 30, 35, 40 )
q7.print_option()
ans7 = input("Enter option: ")
result.append(ans7)
print("-"*40)


q8 = Question("\nQ8. Which keyboard is used to define a function in Python?", "function", "define", "fun", "def")
q8.print_option()
ans8 = input("Enter option: ")
result.append(ans8)
print("-"*40)


q9 = Question("\nQ9. Which ocean in the largest in the world?", "Inian Ocean", "Atlantic Ocean", "Pacific Ocean", "Artic Ocean")
q9.print_option()
ans9 = input("Enter option: ")
result.append(ans9)
print("-"*40)


q10 = Question("\nQ10. What does SQl stand for?", "Structured Query Language", "Simple Query Language", "Standard Query language", "Sequential Query language")
q10.print_option()
ans10 = input("Enter option: ")
result.append(ans10)
print("-"*40)

result1 = ['c', 'b','c','c','b','c','b','d','c','a']


i = 0
c_ans = 1
while (i < 10):
    if(result[i] == result1[i]):
        print(i+1 , ". Correct")
        i += 1
        c_ans += 1

    else:
        print(i+1 , ". Incorrect")
        i += 1

print("\nTotal Score: ", c_ans - 1 , "out of 10")

