# File: Wordle.py

"""
Program By: Brooke Woodland & Ellie Richardson
The purpose of this program is to simulate the game Wordle. Users get 6 chances to guess
the 5-letter word of the day. 
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, PRESENT_COLOR, CORRECT_COLOR, MISSING_COLOR

def wordle():

    gw = WordleGWindow()
    N_COLS = 5
    N_ROWS = 6
    guesses_left = 6

    random_word = random.choice(FIVE_LETTER_WORDS).upper()

    def enter_action(s):

        j=0
        guess_to_check=''
        while j< N_COLS:
            # Get the letter in the corresponding column
            current_letter = gw.get_square_letter(gw.get_current_row(), j)
            if current_letter in random_word:
                gw.set_square_color(gw.get_current_row(), j, PRESENT_COLOR)
            else:
                gw.set_square_color(gw.get_current_row(), j, MISSING_COLOR)

            guess_to_check =guess_to_check+current_letter
            j+=1

        current_row = gw.get_current_row()
        gw.set_current_row(current_row+1)
    

        # evaluate if the guess is a word
        if guess_to_check.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Great guess!")
        else:
            gw.show_message("Not in word list. Please try again.")


    gw.add_enter_listener(enter_action)
    
    #for i, letter in enumerate(random_word):
        #if i < N_COLS:
            # Set the letter in the corresponding column
            #gw.set_square_letter(N_ROWS - guesses_left, i, letter)
    guesses_left-=1

# Startup code

if __name__ == "__main__":
    wordle()