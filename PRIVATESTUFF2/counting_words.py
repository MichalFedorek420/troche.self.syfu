from statistics import mode 
x = input("podaj dowolny tekst: ")
amount_of_words = x.split()
sentence = 0
most_often_word = 0
print(f'Liczba słów w tekście to: {len(amount_of_words)}')
print(f'Liczba unikalnych słów to: {set(amount_of_words)}')
for i in amount_of_words:
    for j in i:
        if j == ".":
            sentence+=1
print(f"liczba zdań to: {sentence}")
temp = [wrd for sub in amount_of_words for wrd in sub.split()]
res = mode(temp)
print(f'Najczęściej występujące słowo to: "{str(res)}"')
while str(res) in amount_of_words:
    amount_of_words.remove(str(res))
    most_often_word+=1
print(f"występuje ono {most_often_word} razy")



