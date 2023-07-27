import string
import random
import sys
characters_left = 0
password = []

length = int(input('Jak długie ma być hasło? '))
if length < 5:
    print('Hasło musi zawierać conajmniej 5 znaków ')
    sys.exit(0)
else:
    characters_left += length

def update_characters_left(number_of_character):
    global characters_left
    if number_of_character < 0 or number_of_character > characters_left:
        print('liczba znaków z poza przedziału 0 -',length)
        sys.exit(0)
    else:
        characters_left -= number_of_character
        print('pozostało znaków:', characters_left)

upper_case = int(input('Ile ma być duzych liter? '))
update_characters_left(upper_case)

lower_case = int(input('ile ma być małych liter? '))
update_characters_left(lower_case)

extra = int(input('ile ma być znaków specjalnych? '))
update_characters_left(extra)

numbers = int(input('ile ma być cyfr? '))
update_characters_left(numbers)

if characters_left > 0:
    print('Nadmiar znaków zostanie uzupełniony małymi literami')
    password.append(random.choices(string.ascii_lowercase, k=characters_left))
    


password.append(random.choices(string.ascii_lowercase, k=lower_case))
password.append(random.choices(string.ascii_uppercase, k=upper_case))
password.append(random.choices(string.punctuation, k=extra))
password.append(random.choices(string.digits, k=numbers))
random.shuffle(password)
print("wygenerowane hasło to:", "".join(["".join(sublist) for sublist in password]))

