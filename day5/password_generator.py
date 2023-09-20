import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# result = ""
# for n in range(0, int(nr_letters)):
#     n = random.choice(letters)
#     result += n
# for n2 in range(0, int(nr_symbols)):
#     n2 = random.choice(symbols)
#     result += n2
# for n3 in range(0, int(nr_numbers)):
#     n3 = random.choice(numbers)
#     result += n3
# print(result)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for n in range(0, int(nr_letters)):
    n = random.choice(letters)
    password_list += n
for n2 in range(0, int(nr_symbols)):
    n2 = random.choice(symbols)
    password_list += n2
for n3 in range(0, int(nr_numbers)):
    n3 = random.choice(numbers)
    password_list += n3
password = ""
random.shuffle(password_list)
for char in password_list:
    password += char
print(password)
