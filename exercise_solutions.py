# Task: Assign a message to a variable and then print that message.
message : str = "Hello, Python World!"
print(message)
# Change the value of the variable to a new message, and print the new message.
message2 : str = "Welcome to Python Programming!"
print(message2)
# Use a variable to represent a person’s name.
name : str = "Eric"
# Print a message to that person, such as, “Hello Eric, would you like to learn some Python today?”
print(f"Hello {name}, would you like to learn some Python today?")
# Use a variable to represent a person’s name.
rename : str = "Umar Waheed"
# Print the person’s name in lowercase, uppercase, and title case.
print(rename.lower())
print(rename.upper())
print(rename.title())
# Find a quote from a famous person you admire.
# "The man who ask a question is a fool for a minute, the man who does not ask is a fool for life." from confucius
# Print the quote and the name of its author.
print('Confucius once said, "The man who ask a question is a fool for a minute, the man who does not ask is a fool for life."')
# Use a variable called famous_person to represent the famous person’s name.
# Compose the message and represent it with a variable called message.
message3 : str = "The man who ask a question is a fool for a minute, the man who does not ask is a fool for life."
famous_person : str = "Confucius"
print(f'{famous_person} once said, "{message3}"')
# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, \t and \n, at least once.
first_name : str = "\n\t Umar Waheed \t\n"
# Print the name once, so the whitespace around the name is displayed.
print(first_name)
# Print the name using each of the three stripping functions: lstrip(), rstrip(), and strip().
print(first_name.lstrip())
print(first_name.rstrip())
print(first_name.strip())
# Assign the values 5, 10, and 15 to three variables x, y, and z. Print their sum.
x : int = 5
y : int = 10
z : int = 15
print("The sum of x, y, and z is:", x + y + z)
# Swap the values of two variables a and b. Print the values before and after the swap.
a : int = 10
b : int = 20
print("a =", a)
print("b =", b)
a, b = b, a
print("a =", a)
print("b =", b)
# Create a variable with your favorite color and print it.
favorite_color : str = "Blue"
print(favorite_color)
# Then change the variable name to something else and print the color again.
color = favorite_color
print(color)
# Create a variable pet_name and set it to "Buddy". 
pet_name : str = "Buddy"
# Change the value of pet_name to "Max" and print the new value.
pet_name1 : str = "Max"
print(pet_name1)
# Assign the value "Sunshine" to a variable and print it.
p : str = "Sunshine"
print(p)
# Then, mistakenly try to print a variable with a different name (like sunsine) and observe the error.
print(p)
# Assign the value 100 to a variable score and print it.
score : int = 100
print(score)
#  Then assign a new value to score and print it again.
score1 : int = 50
print(score1)
# Create a string variable city and assign it the name of a city you like. Print the city name.
city_name : str = "Shanghai"
print(city_name)
# Create a variable text with the value "python programming" and print it in title case.
d : str = "python programming"
print(d.title())
# Assign a string with mixed cases to a variable and print it in all lowercase letters.
e : str = "UmAr WaHEeD"
print(e.lower())
# Assign a string with mixed cases to a variable and print it in all uppercase letters.
print(e.upper())
# Create a variable temperature with the value 25. Print "The current temperature is [temperature] degrees." using the variable.
temperature : int = 25
print(f'The current temperature is {temperature} degrees.')
# Create a variable poem with a short poem that has multiple lines. 
poem: str = """Roses are red,
Violets are blue,
Sugar is sweet,
And so are you."""
#Print the poem with each line starting on a new line.
print(poem)
