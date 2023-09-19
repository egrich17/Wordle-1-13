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
    guesses_left = 5

    random_word = random.choice(FIVE_LETTER_WORDS).upper()
    print(random_word)

    def enter_action(s):

        j=0
        i=0
        guess_to_check=''
        while j< N_COLS:
            # Get the letter in the corresponding column
            current_letter = gw.get_square_letter(gw.get_current_row(), j)
            guess_to_check =guess_to_check+current_letter
            j+=1
    

        # evaluate if the guess is a word
        if guess_to_check.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Great guess!")
            guesses_left=guesses_left-1
            print(guess_to_check)
            print(random_word)
            while i < N_COLS:
                if current_letter == random_word[i]:
                    gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                elif current_letter in random_word:
                    if gw.get_square_color(gw.get_current_row(), i) != CORRECT_COLOR:
                        gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                else:
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
                i = i+1

            current_row = gw.get_current_row()
            gw.set_current_row(current_row+1)
        else:
            gw.show_message("Not in word list. Please try again.")

        if guess_to_check.lower() == random_word.lower():
            end_game()



    gw.add_enter_listener(enter_action)

    def end_game():

        one = 0
        two = 0
        three = 0
        four = 0
        five = 0
        six = 0

        print(guesses_left)

        if guesses_left == 0:
            six = six +1
        elif guesses_left ==1:
            five = five + 1
        elif guesses_left ==2:
            four = four +1
        elif guesses_left == 3:
            three = three +1
        elif guesses_left== 4:
            two = two +1
        elif guesses_left== 5:
            one = one +1

        gw.show_message("Correct! Here are your statistics: \n 1 guess:" + str(one) + "\n 2 guesses:" + str(two) + "\n 3 guesses:" +str(three) + "\n 4 guesses:" + str(four) +"\n 5 guesses:"+ str(five))

    
# Startup code

if __name__ == "__main__":
    wordle()





    
 

            