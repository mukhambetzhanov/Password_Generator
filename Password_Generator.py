# Password Generator Project
import random

# Lists of characters used to generate passwords
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message
print("Welcome to the PyPassword Generator!")

# Get user input for the password composition
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# List to store the generated password
password_list = []

# Add random letters to the password_list
for num in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

# Add random symbols to the password_list
for num in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))
    
# Add random numbers to the password_list
for num in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

# Shuffle the password_list to randomize the order of characters
random.shuffle(password_list)

# Convert the password_list into a string to create the final password
password_str = ""
for chr in password_list:
  password_str += chr

# Print the generated password
print(f"Here is your new password: {password_str}")
