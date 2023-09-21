# File: Wordle.py

"""
Program By: Brooke Woodland & Ellie Richardson
The purpose of this program is to simulate the game Wordle. Users get 6 chances to guess
the 5-letter word of the day. 
"""

import random
import tkinter

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, PRESENT_COLOR, CORRECT_COLOR, MISSING_COLOR, UNKNOWN_COLOR, NEW_CORRECT_COLOR, NEW_MISSING_COLOR, NEW_PRESENT_COLOR

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

def wordle():
    keep_playing = tkinter.BooleanVar()


    while keep_playing:

        gw = WordleGWindow()
        N_COLS = 5
        N_ROWS = 6
        color_mode = "default" #set color mode to default

        def color_mode_option():
            nonlocal color_mode
            #determine if on or off
            if color_mode == "default":
                color_mode = "bright"
            else:
                color_mode = "default"
            color_mode_label.config(text="Color Mode: " + color_mode)  # Update label text

        # display toggle screen for user to select default or bright mode
        root = tkinter.Tk()
        root.title("Wordle Color Mode")
        color_mode_label = tkinter.Label(root, text="Color Mode: " + color_mode)
        color_mode_label.pack()
        toggle_button = tkinter.Button(root, text="Change Mode", command=color_mode_option)
        toggle_button.pack()
        
        # create random word of the day
        random_word = random.choice(FIVE_LETTER_WORDS).upper()
        print(random_word)

        def enter_action(s):
            j=0
            i=0
            guess_to_check=''
            current_row = ''
            while j< N_COLS:
                # Get the letter in the corresponding column
                current_letter = gw.get_square_letter(gw.get_current_row(), j)
                guess_to_check =guess_to_check+current_letter
                j+=1
        
            # evaluate if the guess is a word
            if guess_to_check.lower() in FIVE_LETTER_WORDS:
                gw.show_message("Great guess!")
                # color scheme when user is in default mode
                if color_mode == "default": 
                    while i < N_COLS:
                        current_letter = gw.get_square_letter(gw.get_current_row(), i)
                        if current_letter == random_word[i]:
                            gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                        elif current_letter in random_word:
                            if gw.get_square_color(gw.get_current_row(), i) != CORRECT_COLOR:
                                gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                        else:
                            gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
                        i = i+1
                    current_row = gw.get_current_row()

                else: # color scheme when user is in bright mode
                    while i < N_COLS:
                        current_letter = gw.get_square_letter(gw.get_current_row(), i)
                        if current_letter == random_word[i]:
                            gw.set_square_color(gw.get_current_row(), i, NEW_CORRECT_COLOR)
                        elif current_letter in random_word:
                            if gw.get_square_color(gw.get_current_row(), i) != NEW_CORRECT_COLOR:
                                gw.set_square_color(gw.get_current_row(), i, NEW_PRESENT_COLOR)
                        else:
                            gw.set_square_color(gw.get_current_row(), i, NEW_MISSING_COLOR)
                        i = i+1
                    current_row = gw.get_current_row()

            # prevent user from entering an invalid guess
            else:
                gw.show_message("Not in word list. Please try again.")
                current_row = gw.get_current_row()
                for i in range(N_COLS):
                    gw.set_square_color(gw.get_current_row(), i, UNKNOWN_COLOR)
                i-=1

            won = False

            if guess_to_check.lower() == random_word.lower():
                    won = True
                    end_game(gw.get_current_row(), won)

            if gw.get_current_row()== 5:
                if guess_to_check.lower() == random_word.lower():
                    won = True
                    end_game(gw.get_current_row(), won)
                end_game(gw.get_current_row(), won)

            gw.set_current_row(current_row+1)

        gw.add_enter_listener(enter_action)

        def end_game(guesses_used, won):

            if guesses_used == 5:
                six = six +1
            elif guesses_used ==4:
                five = five + 1
            elif guesses_used ==3:
                four = four +1
            elif guesses_used == 2:
                three = three +1
            elif guesses_used== 1:
                two = two +1
            elif guesses_used== 0:
                one = one +1

            window=tkinter.Tk()
            btn=tkinter.Button(window, text="This is Button widget", fg='blue', command=change_variable)
            btn.place(x=200, y=400)
            if won:
                lbl=tkinter.Label(window, text="Correct! You won! Here are your statistics: \n 1:" + str(one) + "\n 2:" + str(two) + "\n 3:" +str(three) + "\n 4:" + str(four) +"\n 5:"+ str(five)+ "\n 6:" +str(six), font=("Helvetica", 16))
                lbl.place(x=60, y=50)
            else:
                lbl=tkinter.Label(window, text="Game over! Here are your statistics: \n 1:" + str(one) + "\n 2:" + str(two) + "\n 3:" +str(three) + "\n 4:" + str(four) +"\n 5:"+ str(five)+ "\n 6:" +str(six), font=("Helvetica", 16))
                #gw.show_message("You lost! Here are your statistics: 1:" + str(one) + ", 2:" + str(two) + ", 3:" +str(three) + ", 4:" + str(four) +", 5:"+ str(five)+ ", 6:" +str(six))
                lbl.place(x=60, y=50)
            window.title('Game Summary')
            window.geometry("600x500+10+10")
            window.mainloop()

            def change_variable():
                button_pressed = True  # Change this to the new value you want to set
                keep_playing.set(button_pressed)
       
# Startup code

if __name__ == "__main__":
    wordle()





    
 

            