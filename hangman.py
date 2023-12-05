# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, right_letters):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    for i in secret_word:
        if i in right_letters:
            return True


    return False




def get_guessed_word(secret_word, guessings):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    right_letters = ''

    for i in secret_word:
        if  i in guessings:
            right_letters = right_letters + i 
        else:
            right_letters = right_letters + '_ ' 
            


    return right_letters







def get_available_letters(guessings):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    lower = string.ascii_lowercase
    available = ''

    for i in lower:
    
        if not i in guessings:
            available = available + i
        

    return available



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6

    ## A variable to assign users' right inputs in
    right_letters = ''

    ## Game Greeting
    print("Welcome to the game Hangman")
    print("I am thinking of a word that is " , len(secret_word) , " letters long")
    print("Available letters:",string.ascii_lowercase)
    print("------------------------")
    print ("You have", guesses, "guesses left")
    vowels = ['a','e','i','o','u']



    while (not (guesses == 0 and is_word_guessed(secret_word, right_letters))):

        print("The secret word is: ", get_guessed_word(secret_word, right_letters))
        guessings = input('Please guess a letter: ')
        guessings = guessings.lower()
        print("Available letters:", get_available_letters(guessings))

        if  guesses > 0:
            # The user enetred an Invalid input
            if not guessings.isalpha():
            
                print("That's not a valid letter")
                guesses -= 1
                print("You have ", guesses, "guesses left", get_guessed_word(secret_word, right_letters))


            # The user entered a right letter
            elif guessings in secret_word:
                right_letters += guessings
                print("Good guess")
                print("You have ", guesses, "guesses left", get_guessed_word(secret_word, right_letters))


            # The user entered a vowel letter
            elif guessings in vowels:
                    print("Oops! That letter is not in my word")
                    guesses -= 2
                    print("You have ", guesses, "guesses left", get_guessed_word(secret_word, right_letters))   

            # The user entered a wrong letter
            elif not guessings in secret_word:

                print("Oops! That letter is not in my word")
                guesses -= 1
                print("You have ", guesses, " guesses left")

        # Winning Case
        if secret_word == get_guessed_word(secret_word, right_letters):
            print("Congratulations, you won!")
            break

        # Losing Case
        elif guesses == 0:
            print("Sorry, You ran out of guesses, The secret word is:", secret_word)
            break





if __name__ == "__main__":
    # pass


    secret_word = choose_word(wordlist)
    hangman(secret_word) 
