from getpass import getpass

number_of_lifes = 6
phrase = getpass("---->START GRY<----\nPodaj słowo: ")
list_of_letters = []
list_of_tries = []
correct_letters = []

for i in phrase:
    list_of_letters.append(i)

while True:
    check = all(item in correct_letters for item in list_of_letters)

    if check:
        print("---->GRATULACJE WYGRAŁEŚ!<----")
        break

    tryy = input("Podaj literę: ")
    list_of_tries.append(tryy)
    str_list_of_tries = ", ".join(list_of_tries)
    print(f"wykorzystane litery: {str_list_of_tries}")
    if check:
        print("---->GRATULACJE WYGRAŁEŚ!<----")
        break
    else:
        if tryy in list_of_letters:
            print(f"Bingo! pozostało {number_of_lifes} życia")
            # Znajdź wszystkie wystąpienia litery w słowie
            indices = [i for i, x in enumerate(list_of_letters) if x == tryy]
            # Dodaj literę do listy poprawnych liter
            correct_letters.append(tryy)
            # Wyświetl słowo z podkreśleniami i literami odgadniętymi
            word_display = ""
            for i in range(len(list_of_letters)):
                if list_of_letters[i] in correct_letters:
                    word_display += list_of_letters[i] + " "
                else:
                    word_display += "_ "
            print(word_display)
    
        else:
            number_of_lifes -= 1
            print(f"Zła odpowiedź! pozostało {number_of_lifes} życia ")
            if number_of_lifes == 0:
                print("---->PRZEGRAŁEŚ<----\nPoprawna odpowiedź to:", phrase)
                break