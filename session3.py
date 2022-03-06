"""1-Write a Python program that gets the income of user as the input and prints their net income after tax deduction."""
income = input('Please insert your monthly income here (Between 0 to 6k or more then 8k per month): ')
income = int(income)
if income <= 1000:
    result = income
if income > 1000 and income <= 2500:
    result = income - (income * 0.10)
if income > 2500 and income <= 4000:
    result = income - (income * 0.15)
if income > 4000 and income <= 6000:
    result = income - (income * 0.20)
if income > 8000:
    result = income - (income * 0.30)
print(result)

"""2-Write a Python program that gets the sides of a triangle and if this triangle is a right triangle, the program should print "RIGHT triangle", otherwise it should print "NOT RIGHT" """
sideA = input("Please insert side A : ")
sideB = input("Please insert side B : ")
sideC = input("Please insert side C : ")
sideA = int(sideA)
sideB = int(sideB)
sideC = int(sideC)
situation1 = sideA**2 + sideB**2
situation2 = sideA**2 + sideC**2
situation3 = sideB**2 + sideC**2
if situation1 == sideC**2 or situation2 == sideB**2 or situation3 == sideA**2:
    print("RIGHT triangle")
else:print("NOT RIGHT")

"""3-Write a Python program that requests five intger values from user. it then print one of two things: if any of values entered are deplacates, it prints "DUPLICATES"; otherwise, it prints "ALL UNIQUE" """
Num1 = input("please insert 1st intger number : ")
Num2 = input("please insert 2nd intger number : ")
Num3 = input("please insert 3rd intger number : ")
Num4 = input("please insert 4th intger number : ")
Num5 = input("please insert 5th intger number : ")
Num1 = int(Num1)
Num2 = int(Num2)
Num3 = int(Num3)
Num4 = int(Num4)
Num5 = int(Num5)
if Num1 == Num2 or Num1 == Num3  or Num1== Num4 or Num1 == Num5:
    print("DUPLICATES")
elif Num2 == Num3 or Num2 == Num4  or Num2== Num5:
    print("DUPLICATES")
elif Num3 == Num4 or Num3 == Num5:
    print("DUPLICATES")
elif Num4 == Num5:
    print("DUPLICATES")
else:print("ALL UNIQUE")
