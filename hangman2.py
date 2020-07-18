import random

choice = None

list = ["HANGMAN", "ASSIGNEMENT", "PYTHON", "SCHOOL", "PROGRAMMING", "CODING", "CHALLENGE"]
while choice != "0":
    print('''
    ******************
    Welcome to Hangman
    ******************

    Please select a menu option:

    0 - Exit
    1 - Enter a new list of words
    2 - Play Game

    ''')
    choice= input("Enter you choice: ")

    if choice == "0":
        print("Exiting the program...")
    elif choice =="1":
        list = []
        x = 0
        while x != 5:
            word = str(input("Enter a new word to put in the list: "))
            list.append(word)
            word = word.upper()
            x += 1
    elif choice == "2":
        word = random.choice(list)
        word = word.upper()
        hidden_word = " _ " * len(word)
        lives = 6
        guessed = []

        while lives != 0 and hidden_word != word:
            print("\n******************************")
            print("The word is")
            print(hidden_word)
            print("\nThere are", len(word), "letters in this word")
            print("So far the letters you have guessed are: ")
            print(' '.join(guessed))
            print("\n You have", lives,"lives remaining")
            guess = input("\n Guess a letter: \n")
            guess = guess.upper()
            if len(guess) > 1:
                guess = input("\n You can only guess one letter at a time!\n Try again: ")
                guess = guess.upper()
            while guess in guessed:
                print("\n You have already guessed that letter!")
                guess = input("\n Please take another guess: ")
                guess = guess.upper()
