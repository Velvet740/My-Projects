print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division ")
Calculation = input("Enter which calculation you would like to perform: ")
if Calculation == "1. Addition":
  num1 = input("Enter a number: ")
  num2 = input("Enter another number: ")
  result = float(num1) + float(num2)
  print("The result is " + str(result))
elif Calculation == "2. Subtraction":
  num1 = input("Enter a number: ")
  num2 = input("Enter another number: ")
  result = float(num1) - float(num2)
  print("The result is " + str(result))
elif Calculation == "3. Multiplication":
  num1 = input("Enter a number: ")
  num2 = input("Enter another number: ")
  result = float(num1) * float(num2)
  print("The result is " + str(result))
elif Calculation == "4. Division":
  num1 = input("Enter a number: ")
  num2 = input("Enter another number: ")
  result = float(num1) / float(num2)
  print("The result is " + str(result))
else:
  print("Invalid input")