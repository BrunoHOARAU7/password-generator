letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

#try / except

#choice of input stored in a list
for _ in range(1, nr_letters +1) :
    letter = random.choice(letters)
    password += letter
for _ in range(1, nr_symbols +1) :
    sym = random.choice(symbols)
    password += sym
for _ in range(1, nr_numbers +1) :
    nb = random.choice(numbers)
    password += nb

# for the end password, random, and for loop into password to mix all of it together randomly
#to mix the characters together
random.shuffle(password)
print(''.join(password))
