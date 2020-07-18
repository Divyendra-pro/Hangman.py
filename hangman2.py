print('Welcome to hangman game')
print('0 - exit ')
print('1 - Add new words in the list')
choice = input('Enter your choice: ')


def hidden_word(args):
    pass


def word(args):
    pass


if choice == '0':
    print('Exiting the program...')
elif choice == '1':
    list = []
    x = 0
    while x != 5:
        word = str(input('Enter the new word on the word:'))
        list.append(word)
        word = word.upper()
        x += 1
elif choice == 2:
    print('The word is ')
    print(hidden_word)
    print('\nthere are', len(word), 'letters in the word')print(' '.join(guessed))
            print("\n You have", lives,"lives remaining")
            guess = input("\n Guess a letter: \n")
            guess = guess.upper()

