import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password > "))
nr_symbols = int(input(f"How many symbols would you like > "))
nr_numbers = int(input(f"How many numbers would you like > "))

for i in letters:
    pass_letters = random.choices(letters, k=nr_letters)
for i in numbers:
    pass_numbers = random.choices(numbers, k=nr_numbers)
for i in symbols:
    pass_symbols = random.choices(symbols, k=nr_symbols)

let_str = ''.join(str(e) for e in pass_letters)
num_str = ''.join(str(e) for e in pass_numbers)
sym_str = ''.join(str(e) for e in pass_symbols)

pass_len = int(nr_symbols) + int(nr_numbers) + int(nr_letters)
result = let_str + num_str + sym_str
result_list = list(result)
random.shuffle(result_list)
result_mix_str = ''.join(str(e) for e in result_list)
print(result_mix_str)

#Attempt 1(5, 5, 5) - +0b%5I((520Dm&p
#Attempt 2(5, 5, 5) - )74+VBG80(&n8&E
#Attempt 3(5, 5, 5) - 0Xe)D&g9#I9$&01
