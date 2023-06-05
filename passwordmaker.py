import random
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
characters = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
letters_mayus = letters.upper() # Quería probar si funcionaba
base = 0
password = ""
while base < 15:
    base += 1
    first_choice = random.choice([letters, numbers, letters_mayus, characters])
    char_choice = random.choice(first_choice)
    password += char_choice
print("La pass es:", password)
