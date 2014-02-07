from random import randrange
from string import *
#demo of graphics
from hangman_lib import *

# -----------------------------------
# Helper code

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

words_dict = load_words()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    check = 0
    tot = len(secret_word)
    for a in secret_word:
        if a in letters_guessed:
            check += 1

    if check == tot:
        #if every letter in the secret_word is in letters_guessed
        return True
    else:
        return False

    #pass # This tells your code to skip this function; delete it when you
         # start working on this function


def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed

    word = ''
    for a in secret_word:
        if a in letters_guessed:
            word = word+a
        else:
            word = word+'-'
    return word

    #pass # This tells your code to skip this function; delete it when you
         # start working on this function

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    
    secret_word  = get_word()

    while mistakes_made<MAX_GUESSES:
        new = raw_input("Please enter a letter that you want to guess: ")
        #to avoid repeated guesses
        while new in letters_guessed:
            new = raw_input("You already guessed that letter, please enter a new one: ")

        #Just in case user enter a upper case letter 
        new = lower(new)

        #update letter guessed
        letters_guessed.append(new)
        print "Update after your guess"
        status = print_guessed()
        print status

        #check if the new is guessed correctly
        if new in status:
            #check if the word is guessed
            if word_guessed():
                print "You won the game!"
                break
        else:
            mistakes_made+=1
            #update graphics
            print_hangman_image(mistakes_made)
            print "You have", MAX_GUESSES-mistakes_made, 'chances left.'

    #if user uses all chances and haven't got the word 
    if mistakes_made==MAX_GUESSES:
        print "You have no more chances. Gamve Over."
        print "The correct word was "+ secret_word+ '.'

    return None


#To play
play_hangman()    
