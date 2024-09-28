# Mini-calculator

from math_operations import *
def calculator():
    print ()
while True:
    print("Welcome to this calculator")
    print(" Option 1 : + ")
    print(" Option 2 : - ")
    print(" Option 3 : *")
    print(" Option 4 : / ")
    print(" Option 5 : ((x + y) / 2) / ((x - y) * 2) ")
    operation = input("What do you want to calculate? Choose an option,please:  ")
    num1 = int (input("Enter the first number:  "))
    num2 = int (input("Enter the first number:  "))


#
    if operation == "1":
      result = add (num1, num2)
      print(f"{num1} + {num2} = {result}")

    elif operation == "2":
      result = sub(num1, num2)
      print(f"({num1} - {num2} = {result})")

    elif operation == "3":
      result = multiply (num1, num2)
      print(f"({num1} * {num2} = {result})")

    elif operation == "4":
      result = div(num1, num2)
      print(f"{num1} / {num2} = {result}")

    elif operation == "5":
      result = equation(num1, num2)
      print(f"(({num1} + {num2})/2) / (( {num1} - {num2} * 2)) = {result}")
    else:
      print("Invalid option")


    another_operation = input("Would you like to calculate again? (yes/no): ")
    if another_operation.lower() == "no":
      break

