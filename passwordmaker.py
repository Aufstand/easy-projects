import random
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
characters = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
letters_mayus = letters.upper() # Quería probar si funcionaba
counter = 0
while True:
    try:
        passlen = int(input("Insert lenght of password:"))
        if passlen <= 0:
            raise ValueError
        break
    except ValueError:
        print("Do you have stupid?")
password = ""
while counter < passlen:
    counter += 1
    first_choice = random.choice([letters, numbers, letters_mayus, characters])
    char_choice = random.choice(first_choice)
    password += char_choice
print("La pass es:", password)
