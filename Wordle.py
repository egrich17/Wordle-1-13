# File: Wordle.py

"""
Program By: Brooke Woodland & Ellie Richardson
The purpose of this program is to simulate the game Wordle. Users get 6 chances to guess
the 5-letter word of the day. 
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    N_COLS = 5
    N_ROWS = 6
    guesses_left = 6

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    random_word = random.choice(FIVE_LETTER_WORDS).upper()
    print(random_word)
    
    for i, letter in enumerate(random_word):
        if i < N_COLS:
            # Set the letter in the corresponding column
            gw.set_square_letter(N_ROWS - guesses_left, i, letter)
    guesses_left-=1

# Startup code

if __name__ == "__main__":
    wordle()