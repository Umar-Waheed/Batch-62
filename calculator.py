# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    return x / y

# Function to ask if the user wants to perform another calculation
def another_calculation():
    return input("Do you want to perform another calculation? (yes/no): ").strip().lower() == 'yes'

# Main program
while True:
    # Print the operation choices
    print("\nSelection operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # For user input
    choice = input("Enter choice (1/2/3/4): ")

    # Check if the choice is valid (between 1 and 4)
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the selected operation
        if choice == '1':
            print(f"The result of addition: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result of subtraction: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result of multiplication: {multiply(num1, num2)}")
        elif choice == '4':
            if num2 != 0:  # Check to avoid division by zero
                print(f"The result of division: {divide(num1, num2)}")
            else:
                print("Error! Division by zero.")
    else:
        print("Invalid input! Please enter a valid operation choice.")

    # Ask if the user wants to perform another calculation
    if not another_calculation():
        print("Goodbye!")
        break