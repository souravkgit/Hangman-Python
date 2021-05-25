import string
from words import choose_word
from images import IMAGES
def is_word_guessed(secret_word, letters_guessed):
    for el in secret_word:
        if el not in letters_guessed:
            return False
    return True
def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word
def get_available_letters(letters_guessed):
    letters_left = list(string.ascii_lowercase)
    for el in letters_guessed:
        if el in letters_left:
            letters_left.remove(el)
    return letters_left
def hangman(secret_word):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')
    letters_guessed = []
    while len(IMAGES)>0:
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))

        guess = input("Please guess a letter: ")
        letter = guess.lower()
        if letter not in available_letters:
            print("This Letter Is Already Selected , You Can't Select This Letter Again!!")
        elif letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed):
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
        else:
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            letters_guessed.append(letter)
            print(IMAGES.pop(0))
            if len(IMAGES)==1 and len(letters_guessed)!=len(secret_word):
                print("\nYou Wasted All Of Your Attempts And Your Game Is Over")
                print("The Correct Word Was " + secret_word)
                break
            print("")
secret_word = choose_word()
hangman(secret_word)
