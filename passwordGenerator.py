import random
# Initialising the lists of letters, numbers and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
# Taking the number of letters, symbols and numbers from the user
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []
# Generating the password
for i in range(nr_letters):     # Appending the letters to the password
    password.append(random.choice(letters))
for i in range(nr_symbols):     # Appending the symbols to the password
    password.append(random.choice(symbols))
for i in range(nr_numbers):     # Appending the numbers to the password
    password.append(random.choice(numbers))
for i in password:
    random.shuffle(password)    # Shuffling the password
password = ''.join(password)    # Joining the password
print(f"Your strong password is {password}")