# Simple Calculator Program

def calculator():
    # Ask the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Ask the user for a mathematical operation
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    
    # Perform the operation based on user input
    if operation == 'add':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == 'subtract':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif operation == 'multiply':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Invalid operation. Please choose add, subtract, multiply, or divide.")

# Call the calculator function to run the program
calculator()
# Defining variables
name="My name is Ivy Wanjiru."
gender= "I am female."
age= 20
hobby="I love music."

print(name)
print(gender)
print(age)
print (hobby)
