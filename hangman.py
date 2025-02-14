import random

words = ['computer', 'pc', 'mouse', 'keyboard', 'monitor', 'microphone', 'headphones']
selected_chars = []
print('Welcome in hangman game')
while True:
    start_word = input("Enter 'start' for run the game")

    if start_word == 'start':
        word_to_guess = random.choice(words)

        if users_word == word_to_guess:
            print('You win')
        else:
            for char in word_to_guess:
                users_char = input('Enter the char')
                if users_char in word_to_guess:
                    index = word_to_guess.index(users_char)
                    print(f'Congrats, this char is {index}')
                else:
                    print("Nah, this char isn'n in this word. Try again")
        