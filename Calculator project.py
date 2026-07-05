print("\t\tCalculator")
print("\n Here look at the available operator")
print("\n1. + \n2. - \n3. * \n4. /\n5. ** \n6. %\n")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print("\nWhich operator you will use.")
select = int(input("Select option:- "))

if(select == 1):
    print("Sum : " , num1 + num2)
elif(select == 2):
    print("diff: ", num1 - num2)
elif(select == 3):
    print("mul: ", num1*num2)
elif(select == 4):
    print("num1 / num2 is : ", num1/num2)
elif(select == 5):
    print("Power : ", num1**num2)
elif(select == 6):
    print("remainder: ", num1 % num2)
else:
    print("Wrong input \nPlease enter right input.")
