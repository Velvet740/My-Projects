#Calculator layout
print("My Awesome Calculator")
print("+---------------------+")
print("+ |+| |-| |*| |/| |^| |avg| +")
print("+     |numbers' game|       +")
print("+        Calculate          +")
print("       \\\\\\\\ ^--^ \\\\\\\\     ")
print()
print()

#Calculator instructions
print("My Awesome Calculator that includes")
print("1. Addition (+). Please input + when prompted")
print("2. Subtraction (-). Please input - when prompted")
print("3. Multiplication (*). Please input * when prompted")
print("4. Division (/). Please input / when prompted")
print("5. Exponentiation (^). Please input ^ when prompted")
print("6. Average (avg). Please input avg when prompted")


#Main program loop:
while True:
    #Iniating the calculations and prompting the users: also adding newline characters (\n) to enhance readability
    o = input("\nEnter which mathematical calculation you would like to perform?: ")
    
    #Check if the mathematical operation is one of the listed ones
    if o not in ['+', '*', '-', '/', '^', 'avg']:
        print("Not a valid mathematical calculation")
        continue
    
    #Prompting users to enter the numbers for the average calculation: then checking if the numbers entered are valid by using try statement. 
    #For calculating average: using .split() method which would split the input string into a list of strings based on spaces and commas. The strip() method would remove any extra spaces around the numbers before converting them to float.
    #Replace(',', ' ') to replace commas , with spaces ' ' in the listnumbers string. This is useful to split the string by spaces, later using .split() to get individual numbers. [e.g. if listnumbers is "11, 4, 5", after replace(',', ' '), it becomes "11 4 5". With .split(), it will be ['11', '4', '5'], which can then be converted to a list of numbers.]
    
    if o == 'avg':
        listnumbers = input("Enter a list of numbers seperated by commas or spaces: ")
        try:
            numbers =[float(num.strip()) for num in listnumbers.replace (',', ' ').split()]
        except ValueError:
            print("The values entered are not valid numbers.",
            "Please try again.")
            continue
        
        #Calculate average: dividing the sum of the numbers by the count of numbers using sum(numbers) / len(numbers). Also using the map(str, numbers) to convert each number in the numbers list back to a string; ' , '.join(...) joins these strings with commas to form a single string. The avg:.3f part displays the average up to three decimal places.
        avg = sum(numbers)/len(numbers)
        print(f"The average of {' , '.join(map(str, numbers))} is {avg:.3f}")
        
        #Ask if the user wants to continue
        more_calculation = input("\nWould you like to continue with another calculation? (yes/no): ")
        if more_calculation.lower() == 'no':
            print("Thank you!")
            break
        continue
    
    
    #Prompting for values:
    x=input("Enter the x value: ")
    y=input("Enter the y value: ")
    
    #Convert x and y to floats and check if x and y are valid numbers
    try:
        x = float(x)
    except ValueError:
        print("x value entered is not a valid number.",
        "Goodbye")
        continue
    
    try:
        y = float(y)
    except ValueError:
        print("y value entered is not a valid number.",
        "Goodbye")
        continue
    
    #Perfomring calculation and displaying the result:
    if o=="+":
        print("The result of the addition is ", x+y)
    elif o=="*":
        print("The result of the multiplication is ", x*y)
    elif o=="-":
        print("The result of the subtraction is ", x-y)
    elif o=="/":
        if y == 0:
            print("The result of the division is 'Infinity'")
        else:
            print(f"The result of the division is {x/y:.3f}")
    elif o=="^":
        print(f"The result of the {x} to the power of {y} is {x ** y}")
    else:
        print("Invalid output")
        
    # Check if user wants to continue using the calculator
    question = input("\nWould you like to perform another calculation? (yes/no): ")
    if question.lower() != 'yes':
        print("Thank you, see you later!")
        break
    
#Print a smiley and a sustainability message at the end of the output
print(":-)")
print()
print()
print("Save water, save environment.")
