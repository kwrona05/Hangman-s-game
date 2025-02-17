import random

words = ["computer", "laptop", "car", "wifi"]
points = 5

while points > 0:
    word_to_guess = random.choice(words)
    print('1. Enter the char')
    print('2. Enter the word')
    option = input('Choose an option (1/2): ')

    if option == '1':
        user_char = input('Enter the char')
        for char in word_to_guess:
            if char == user_char:
                print(f'{user_char} is in the word')
                break
            else:
                points -= 1
                print('Not this time')
                print(f'Points left: {points}')
                break
    elif option == '2':
        user_word = input('Enter the word')
        if user_word == word_to_guess:
            print('Congrats, you win')
            break
        else:
            points -= 1
            print('Not this time')
            print(f'Points left: {points}')
