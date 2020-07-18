'''
The window and text for the 'How to play' Button
'''

from tkinter import *
import tkinter.font
rules = Tk()
rules.title("Rules of the colour game!!")

#*tkinter.font works the best
header_font = tkinter.font.Font(size=20, weight="bold", slant="italic", underline=1)
header = Label(rules, text="How to play", font=header_font, width=20)
header.grid(row=0, column=0)

first_body_text = "1. When you start the game, a countdown will start.\n\n2. Click the entry box on the screen to get ready.\n\n3. When the countdown ends, a timer for 45 seconds will go off.\nA name of a colour will pop up on a big label above the entry box.\n\nFor example:"

first_body_label = Label(rules, text=first_body_text, width=50)
first_body_label.grid(row=1, column=0)

example_font = tkinter.font.Font(size=10)
example = Label(rules, text="Red", fg="blue", font=example_font, relief=RIDGE)
example.grid(row=2, column=0)

second_body_text = "4. Like the example above, you will notice that the \nFONT COLOUR of these colour names will be unique.\nYour task is to type this unique FONT COLOUR into the entry box."

second_body_label = Label(rules, text=second_body_text, width=50)
second_body_label.grid(row=3, column=0)

note_font = tkinter.font.Font(weight="bold", slant="italic", underline=1)
note_intro_text = "\nSome things to note:\n"
note_intro_label = Label(rules, text=note_intro_text , width=50, font=note_font)
note_intro_label.grid(row=4, column=0)

note_1_text = "1)You can see the remaining time and your current score.\n"
note_1_label = Label(rules, text=note_1_text, width=50)
note_1_label.grid(row=5, column=0)

note_2_text = "2)The COLOUR TEXT and FONT COLOUR will appear in random \norder.\n"
note_2_label = Label(rules, text=note_2_text, width=50)
note_2_label.grid(row=6, column=0)

note_3_text = "3)If you cannot recognize the font colour (e.g. Is this pink, magenta,\n or purple!?), there will be a list of COLOURS corresponding with\n their NAMES on the side. The correct answer will be included in\n this list.\n"
note_3_label = Label(rules, text=note_3_text, width=50)
note_3_label.grid(row=7, column=0)


note_4_text = "4)The answer ISN'T case-sensitive! It wouldn't matter if you type in\n all lower-case, all upper-case, or first letter capitalized etc.\n"
note_4_label = Label(rules, text=note_4_text, width=50)
note_4_label.grid(row=8, column=0)

note_5_text = "5)The entry box will auto-detect whether you have typed in the\n right answer or not. You don't have to submit your answer by\n clicking a submit button.\n"
note_5_label = Label(rules, text=note_5_text, width=50)
note_5_label.grid(row=9, column=0)

note_6_text = "6)When your answer is correct, the label will automatically change,\n the entry box will be cleared, and your score will increase by 1. But\n you cannot proceed to the next question if you don't clear the\n current one!\n"
note_6_label = Label(rules, text=note_6_text, width=50)
note_6_label.grid(row=10, column=0)

ending_font = tkinter.font.Font(size=10, weight="bold", slant="italic", underline=1)
ending_text = "Good Luck!!"
ending_label = Label(rules, text=ending_text, font=ending_font)
ending_label.grid(row=11, column=0)

mainloop()