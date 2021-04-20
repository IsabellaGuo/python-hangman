import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #choose somthing from the list ramdomly
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words) #make sure the letter is valid
    word_letters = set(word) #letters in the word. It will keep track what has been guessed in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    while len(word_letters) > 0:
        #letters has used
        print('You have used these letters: ', ' '.join(used_letters))
        #' '.join(['a', 'b', 'cd']) --> 'a b cd'

        #what current word is (ie: W - R D )
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper() #getting user input
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        
        else:
            print('Invalid character. Please try again')

       

hangman()