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



def wordle():
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0

    gw = WordleGWindow()
    color_mode = "default" #set color mode to default

    def color_mode_option():
            nonlocal color_mode
            #determine if on or off
            if color_mode == "default":
                color_mode = "pastel"
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

    def play_game():
        N_COLS = 5
        N_ROWS = 6
        
        #clear keys

        gw.set_key_color("A", MISSING_COLOR)
        gw.set_key_color("B", MISSING_COLOR)
        gw.set_key_color("C", MISSING_COLOR)
        gw.set_key_color("D", MISSING_COLOR)
        gw.set_key_color("E", MISSING_COLOR)
        gw.set_key_color("F", MISSING_COLOR)
        gw.set_key_color("G", MISSING_COLOR)
        gw.set_key_color("H", MISSING_COLOR)
        gw.set_key_color("I", MISSING_COLOR)
        gw.set_key_color("J", MISSING_COLOR)
        gw.set_key_color("K", MISSING_COLOR)
        gw.set_key_color("L", MISSING_COLOR)
        gw.set_key_color("M", MISSING_COLOR)
        gw.set_key_color("N", MISSING_COLOR)
        gw.set_key_color("O", MISSING_COLOR)
        gw.set_key_color("P", MISSING_COLOR)
        gw.set_key_color("Q", MISSING_COLOR)
        gw.set_key_color("R", MISSING_COLOR)
        gw.set_key_color("S", MISSING_COLOR)
        gw.set_key_color("T", MISSING_COLOR)
        gw.set_key_color("U", MISSING_COLOR)
        gw.set_key_color("V", MISSING_COLOR)
        gw.set_key_color("W", MISSING_COLOR)
        gw.set_key_color("X", MISSING_COLOR)
        gw.set_key_color("Y", MISSING_COLOR)
        gw.set_key_color("Z", MISSING_COLOR)

        #clear board

        k = 0
        l = 0
        while k < 6:
            while l < 5:
                gw.set_square_letter(k,l,'')
                gw.set_square_color(k,l, UNKNOWN_COLOR)
                l+=l
        k+=k

        # create random word of the day
        random_word = random.choice(FIVE_LETTER_WORDS).upper()
        print(random_word)

        # keep track of correct letters and keys
        correct_guesses = set()
        correct_key_colors = {}
        present_key_colors = {}

        def enter_action(s):
            j=0
            i=0
            guess_to_check=''
            current_row = 0
            # keep track of the number of letters in the target word
            target_letter_counts = {}

            while j< N_COLS:
                # Get the letter in the corresponding column
                current_letter = gw.get_square_letter(gw.get_current_row(), j)
                guess_to_check =guess_to_check+current_letter
                j+=1

            # fill target_letter_counts dictionary
            for letter in random_word:
                target_letter_counts[letter] = target_letter_counts.get(letter, 0) + 1
        
            # evaluate if the guess is a word
            if guess_to_check.lower() in FIVE_LETTER_WORDS:
                gw.show_message("Great guess!")
                # color scheme when user is in default mode
                if color_mode == "default": 
                    i = 0
                    # loop through each of the 5 letters
                    while i < N_COLS:
                        # get current letter
                        current_letter = gw.get_square_letter(gw.get_current_row(), i)
                        # if current letter is in the right spot, change color to correct. set all corrects first
                        if current_letter == random_word[i]:
                            gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                            # decrement target letter count & add to correct guesses
                            target_letter_counts[current_letter] -= 1
                            correct_guesses.add(current_letter)
                            # set the key color to correct
                            gw.set_key_color(current_letter, CORRECT_COLOR)
                            correct_key_colors[current_letter] = CORRECT_COLOR
                        # if current letter is not in the word, set sqaure and keys to missing
                        else:
                            gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
                            gw.set_key_color(current_letter, MISSING_COLOR)
                        
                        # if current letter is in the word, but the wrong place, change color to present
                        if current_letter in random_word and gw.get_square_color(gw.get_current_row(), i,) != CORRECT_COLOR:
                            # account for more than 1 of the same letter
                            if target_letter_counts[current_letter] > 0:
                                gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                                target_letter_counts[current_letter] -= 1
                                # set key color to present
                                gw.set_key_color(current_letter, PRESENT_COLOR)
                                present_key_colors[current_letter] = PRESENT_COLOR
                            # account for word being guessed in the correct spot in a previous turn, but is now placed
                            # in different location
                            elif current_letter in correct_guesses and target_letter_counts[current_letter] > 1:
                                gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                                gw.set_key_color(current_letter, PRESENT_COLOR)
                                present_key_colors[current_letter] = PRESENT_COLOR
                            # if current letter is only in the word one time, multiple instances of the word should be marked missing
                            else:
                                gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
                                gw.set_key_color(current_letter, MISSING_COLOR)

                        # ensure that once marked, correct keys stay in the color "correct"
                        if current_letter in correct_key_colors:
                            gw.set_key_color(current_letter, correct_key_colors[current_letter])
                        # ensure that correct or present keys guessed more than once don't get grayed out
                        if current_letter not in correct_key_colors:
                            if current_letter in present_key_colors:
                                gw.set_key_color(current_letter, present_key_colors[current_letter])

                        i = i+1
                    current_row = gw.get_current_row()

                # color scheme when user is in pastel mode
                if color_mode == "pastel": 
                    i = 0
                    # loop through each of the 5 letters
                    while i < N_COLS:
                        # get current letter
                        current_letter = gw.get_square_letter(gw.get_current_row(), i)
                        # if current letter is in the right spot, change color to correct. set all corrects first
                        if current_letter == random_word[i]:
                            gw.set_square_color(gw.get_current_row(), i, NEW_CORRECT_COLOR)
                            # decrement target letter count & add to correct guesses
                            target_letter_counts[current_letter] -= 1
                            correct_guesses.add(current_letter)
                            # set the key color to correct
                            gw.set_key_color(current_letter, NEW_CORRECT_COLOR)
                            correct_key_colors[current_letter] = NEW_CORRECT_COLOR
                        # if current letter is not in the word, set sqaure and keys to missing
                        else:
                            gw.set_square_color(gw.get_current_row(), i, NEW_MISSING_COLOR)
                            gw.set_key_color(current_letter, NEW_MISSING_COLOR)
                        
                        # if current letter is in the word, but the wrong place, change color to present
                        if current_letter in random_word and gw.get_square_color(gw.get_current_row(), i,) != NEW_CORRECT_COLOR:
                            # account for more than 1 of the same letter
                            if target_letter_counts[current_letter] > 0:
                                gw.set_square_color(gw.get_current_row(), i, NEW_PRESENT_COLOR)
                                target_letter_counts[current_letter] -= 1
                                # set key color to present
                                gw.set_key_color(current_letter, NEW_PRESENT_COLOR)
                                present_key_colors[current_letter] = NEW_PRESENT_COLOR
                            # account for word being guessed in the correct spot in a previous turn, but is now placed
                            # in different location
                            elif current_letter in correct_guesses and target_letter_counts[current_letter] > 1:
                                print(current_letter + " in correct guesses")
                                gw.set_square_color(gw.get_current_row(), i, NEW_PRESENT_COLOR)
                                gw.set_key_color(current_letter, NEW_PRESENT_COLOR)
                                present_key_colors[current_letter] = NEW_PRESENT_COLOR
                            # if current letter is only in the word one time, multiple instances of the word should be marked missing
                            else:
                                gw.set_square_color(gw.get_current_row(), i, NEW_MISSING_COLOR)
                                gw.set_key_color(current_letter, NEW_MISSING_COLOR)

                        # ensure that once marked, correct keys stay in the color "correct"
                        if current_letter in correct_key_colors:
                            gw.set_key_color(current_letter, correct_key_colors[current_letter])
                        # ensure that correct or present keys guessed more than once don't get grayed out
                        if current_letter not in correct_key_colors:
                            if current_letter in present_key_colors:
                                gw.set_key_color(current_letter, present_key_colors[current_letter])

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
                    end_game(gw.get_current_row(), won, one, two, three, four, five, six)

            if gw.get_current_row()== 5:
                if guess_to_check.lower() == random_word.lower():
                    won = True
                    end_game(gw.get_current_row(), won)
                end_game(gw.get_current_row(), won, one, two, three, four, five, six)

            # don't move to next row if last guess or invalid word
            if current_row < N_ROWS - 1 :
                gw.set_current_row(current_row+1)
                if guess_to_check.lower() not in FIVE_LETTER_WORDS:
                    gw.set_current_row(current_row)

        target_letter_counts = {}
        gw.add_enter_listener(enter_action)

        def end_game(guesses_used, won, one, two, three, four, five, six):

            print("end game is called")

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
            btn=tkinter.Button(window, text="Play Again", fg='blue', command=play_game)
            btn.place(x=200, y=400)
            if won:
                lbl=tkinter.Label(window, text="Correct! You won! Here are your statistics: \n 1:" + str(one) + "\n 2:" + str(two) + "\n 3:" +str(three) + "\n 4:" + str(four) +"\n 5:"+ str(five)+ "\n 6:" +str(six), font=("Helvetica", 16))
                lbl.place(x=60, y=50)
            else:
                lbl=tkinter.Label(window, text="Game over! Here are your statistics: \n 1:" + str(one) + "\n 2:" + str(two) + "\n 3:" +str(three) + "\n 4:" + str(four) +"\n 5:"+ str(five)+ "\n 6:" +str(six), font=("Helvetica", 16))
                lbl.place(x=60, y=50)
            window.title('Game Summary')
            window.geometry("600x500+10+10")
            window.mainloop()
    
    play_game()

       
# Startup code

if __name__ == "__main__":
    wordle()
