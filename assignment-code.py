def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Greet the user and get their name
name = input("Enter your name: ")

# Prompt the user for three favorite numbers
first_num = int(input("Enter your first favorite number: "))
second_num = int(input("Enter your second favorite number: "))
third_num = int(input("Enter your third favorite number: "))

# Store the numbers in a list
numbers = [first_num, second_num, third_num]

# Personalized greeting
print(f"\nHello, {name}! Let's explore your favorite numbers:")

# Check if each number is even or odd and store in a list of tuples
even_odd_list = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]

# Print the even/odd status of each number
for num, status in even_odd_list:
    print(f"The number {num} is {status}.")

# Print each number and its square
print("\nHere are your numbers and their squares:")
for num in numbers:
    print(f"The number {num} and its square: ({num}, {num ** 2})")

# Calculate the sum of the three numbers
total_sum = sum(numbers)
print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

# Check if the sum is a prime number
if is_prime(total_sum):
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"{total_sum} is not a prime number, but that's still interesting!")

