Category = {
    "Jedzenie":0,
    "Transport":0,
    "Rozrywka":0,
    "Ubrania":0,
    "Alkohol":0,
    "Nikotyna":0,
    "Partner/Parnterka":0,
    "Sport":0,
    "Kosmetyki":0,
    "Zwierzęta":0,
    "Dom":0,
    "Zdrowie":0,
}
def new_category(your_new_category):
    Category.update({your_new_category:0})
    return Category[your_new_category]

while True:
    print('Nowy przychód (wpisz"przychód"), czy wydatek (wpisz"wydatek")?\n')
    x=input(':')
    print()
    amount=int(input('Podaj kwotę: '))
    print()
    choose_category=input(f'Wybierz kategorie lub dodaj nową (wpisz nazwę nowej kategori)\n\n{Category.keys()}\n')
    if choose_category not in Category.keys():
        new_category(choose_category)
    if x == "przychód":
        Category[choose_category]+= amount
        print(Category.items(), '\n')
    if x == "wydatek":
        Category[choose_category]-= amount
        print(Category.items(), '\n')
        

    
        


    