import json
points = 0
def show_questions(question):
    global points
    print()
    print(question["pytanie"])
    print('a:', question["a"])
    print('b:', question["b"])
    print('c:', question["c"])
    print('d:', question["d"])
    print()
    answer = input('Jaka jest poprawna odpowiedz?')
    if answer == question['prawidlowa_odpowiedz']:
        points += 1
        print(f'To poprawna odpowiedź\nLiczba punktów: {points}')
    else:
        points -=1
        print(f'To zła odpowiedź\nLiczba punktów: {points}\nPoprawna odpowiedź to: {question["prawidlowa_odpowiedz"]}')
    

with open('quiz.json') as json_file:
    questions = json.load(json_file)
    for i in range(0,len(questions)):
        show_questions(questions[i])
    print('Koniec Gry')