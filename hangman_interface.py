from random import choice
from hangman_functions import list_provider, intro_hangman, play_hangman

# For normal hangman game a user have about 6 chances/attempts to guess a word.
attempts = 6

# Here we ask for a list from the list_provider() and choose a word from it.
words = list_provider()
chosen_word = choice(words)

# Introducing the game
intro_hangman()

# Giving the user a hint 
hint = f'The chosen word is a common noun which contains of {len(chosen_word)} letters'

# Playing the game.
play_hangman(chosen_word, hint, attempts)