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

    gw = WordleGWindow()
    N_COLS = 5
    N_ROWS = 6
    guesses_left = 6

    def enter_action(s):

        j=0
        guess_to_check=''
        while j< N_COLS:
            # Get the letter in the corresponding column
            current_letter = gw.get_square_letter(N_ROWS-(guesses_left+1), j)
            guess_to_check =guess_to_check+current_letter
            j+=1

        # evaluate if the guess is a word
        if guess_to_check in FIVE_LETTER_WORDS:
            gw.show_message("great guess")
        else:
            gw.show_message("not in word list")
        

 
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