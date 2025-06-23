def AddFunct():
  try:
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))
    result=num1+num2
    print(f"The Addition of the numbers is:{result}")
  except ValueError:
    print("Only Numbers are allowed..")

def SubFunct():
  try:
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))
    result=num1-num2
    print(f"The Subtraction of the numbers is:{result}")
  except ValueError:
    print("Only Numbers are allowed..")

def MulFunct():
  try:
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))
    result=num1*num2
    print(f"The Multiplication  of the numbers is:{result}")
  except ValueError:
    print("Only Numbers are allowed..")

def DivFunct():
  try:
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))
    if num2==0:
        print("Enter any Number other than Zero..")
    else:
      result=num1/num2
      print(f"The Division of the numbers is:{result}")
  except ValueError:
    print("Only Numbers are allowed..")

def PowFunct():
  try:
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the power:"))
    result=num1**(num2)
    print(f"The Power of the number is:{result}")
  except ValueError:
    print("Only Numbers are allowed..")

while True:
  print('''
        A.Addition
        S.Subtraction
        M.Multiplication
        D.Division
        P.Power
        X.Quit''')
  choice=input("Enter your choice:").upper()
  if choice=="A":
    AddFunct()
  elif choice=="S":
    SubFunct()
  elif choice=="M":
    MulFunct()
  elif choice=="D":
    DivFunct()
  elif choice=="P":
    PowFunct()
  elif choice=="X":
    print("Quitting The Process..")
    break
  else:
    print("Enter Valid character to proceed..")
