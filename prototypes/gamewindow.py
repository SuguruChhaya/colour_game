from tkinter import *
from tkinter import messagebox
import tkinter.font
import random

import sqlite3
import time
import pygame
from pygame import mixer
pygame.init()
mixer.init()

game = Tk()
game.title("Main game window")

difficulty = "medium_highscore"

colour_list = ['yellow', 'green yellow', 'green', 'sky blue', 'white', 'gray', 'orange', 'pink', 'magenta', 'red', 'purple', 'blue', 'black']
answer_list = ['yellow', 'light green', 'green', 'light blue', 'white', 'gray', 'orange', 'pink', 'magenta', 'red', 'purple', 'blue', 'black']
background_list = ['yellow', 'green yellow', 'green', 'sky blue', 'white', 'gray', 'orange', 'pink', 'magenta', 'red', 'purple', 'blue']
audio_list = ['yellow.mp3', 'light_green.mp3', 'green.mp3', 'light_blue.mp3', 'white.mp3', 'gray.mp3', 'orange.mp3', 'pink.mp3', 'magenta.mp3', 'red.mp3', 'purple.mp3', 'blue.mp3', 'black.mp3']

score = 0
def check_answer(a, b, c):
    #*The checking part comes here.
    global score
    if main_entry_text.get().lower() == answer:
        main_entry.delete(0, END)
        score += 1
        current_score.config(text=str(score))
        try:
            main_entry.after_cancel(repeat)
        except NameError:
            pass
        random_choose()


def audio_play():
    #!I think the after is binded multiple times when this is ran.
        #*The problem is somewhere in here: the music is played excessively.
    global repeat
    mixer.music.load(audio)
    mixer.music.play()
    #!The repeating issue was solved by assigning the after thing to a variable.
    #*I didn't really know how to use the after_cancel function.
    #*Thanks to https://stackoverflow.com/questions/25702094/tkinter-after-cancel-in-python 
    repeat= main_entry.after(1500, audio_play)

def random_choose():
    global answer 
    global audio
    answer = random.choice(answer_list)
    fake = random.choice(answer_list)
    audio = audio_list[answer_list.index(fake)]
    background = "white"
    if difficulty.get() == "medium_highscore" or difficulty.get() == "hard_highscore":
        background = random.choice(background_list)
        if difficulty.get() == "hard_highscore":
            audio_play()
    main_label.config(text=fake, fg=answer)
    main_entry.config(bg=background)



header_game_font = tkinter.font.Font(size=20, slant="italic", weight="bold", underline=1)
header_game_label = Label(game, text="COLOUR GAME", font=header_game_font, width=30)
#*Might have to change columnspan
header_game_label.grid(row=0, column=0, columnspan=3)

countdown_info_font = tkinter.font.Font(size=18)
countdown_info = Label(game, text="Game starts in", font=countdown_info_font, relief=RIDGE, width=12)
countdown_info.grid(row=6, column=0, rowspan=2)

countdown_number = Label(game, text="5", font=countdown_info_font, relief=RIDGE, width=12)
countdown_number.grid(row=7, column=0, rowspan=3)

main_label_font = tkinter.font.Font(size=18, weight="bold")
main_label = Label(game, text="CLICK ON THE \nENTRY BOX BELOW!", font=main_label_font, width=17, relief=RIDGE, fg="red")
main_label.grid(row=10, column=0, rowspan=4)

main_entry_text = StringVar()
main_entry_text.trace_add('write', check_answer)

main_entry_font = tkinter.font.Font(size=18)
main_entry = Entry(game, width=17, font=main_entry_font, textvariable=main_entry_text)
main_entry.grid(row=14, column=0, rowspan=2)

score_font = tkinter.font.Font(size=11)

current_label = Label(game, text="Your current score: ", font=score_font)
current_label.grid(row=1, column=0, sticky=E)

current_score = Label(game, text=str(score), font=score_font)
current_score.grid(row=1, column=1, sticky=W)

highscore_label = Label(game, text="Your previous highscore: ", font=score_font)
highscore_label.grid(row=2, column=0, sticky=E)

#*I am just going to try fetching from the database using random usernames and all.
user = StringVar()
user.set('Suguru')
difficulty = StringVar()
difficulty.set("medium_highscore")

connection = sqlite3.connect('highscores.db')
cursor = connection.cursor()

#cursor.execute("SELECT " + f"'{difficulty.get()}' " +  "FROM highscores WHERE username=" + f"'{user.get()}'")
#!f"" works wonderfully for sqlite commands!! By doing this, I can easy find the row, column I have to accesss and possible modify
cursor.execute(f"SELECT {difficulty.get()} FROM highscores WHERE username='{user.get()}'")
record = cursor.fetchall()

for item in record[0]:
    highscore_table = item
    
connection.commit()
connection.close()

highscore_score = Label(game, text=highscore_table, font=score_font)
highscore_score.grid(row=2, column=1, sticky=W)




colours_intro_font = tkinter.font.Font(slant="italic", underline=1)
colours_intro = Label(game, text="Available colours", font=colours_intro_font)
colours_intro.grid(row=3, column=1, columnspan=2)

colour_row_tracker = 4
for item in colour_list:
    label_text= item
    if item == "green yellow":
        label_text = "light green"
    elif item == "sky blue":
        label_text = "light blue"
    Label(game, bg=item, width= 10).grid(row=colour_row_tracker, column=1, sticky=E)
    Label(game, text=label_text, width=8).grid(row=colour_row_tracker, column=2, sticky=W)
    colour_row_tracker += 1

forty_five_sec_timer = 15
def forty_five_sec():
    global forty_five_sec_timer
    if forty_five_sec_timer > 0:
        countdown_number.config(text=str(forty_five_sec_timer))
        forty_five_sec_timer -= 1
        countdown_number.after(1000, forty_five_sec)

    elif forty_five_sec_timer == 0:
        try:
            main_entry.after_cancel(repeat)
        except NameError:
            pass
        countdown_number.config(text="STOP!!")
        main_entry.config(state=DISABLED)
        countdown_number.update()
        main_entry.update()
        time.sleep(1)
        #*I have to add the new window which pops up.
        #*f"" doesn't seem to work
        #*whether high score or not, then the score
        #*I am keeping the game window open because the askquestion needs at least one window open.

        #*Connecting to databse to see if this was new record.
        connection = sqlite3.connect('highscores.db')
        cursor = connection.cursor()
        question_text = ""
        if score > int(highscore_table):
            question_text += "NEW HIGHSCORE!\n"
            cursor.execute(f"UPDATE highscores SET {difficulty.get()} = {score}")
        question_text += f"Your score is {score}.\nContinue playing?"


        response = messagebox.askquestion("Continue?", question_text)
        game.destroy()
        
        connection.commit()
        connection.close()


five_sec_countdown = 5
def five_sec():
    global five_sec_countdown
    if five_sec_countdown > 0:
        countdown_number.config(text=str(five_sec_countdown))
        five_sec_countdown -= 1
        countdown_number.after(1000, five_sec)
    elif five_sec_countdown == 0:
        #?Somehow doesn't change...
        #https://stackoverflow.com/questions/28165342/python-time-sleep-delays-previous-commands 
        countdown_number.config(text="START!!")
        #*.update() forces the update
        countdown_number.update()
        time.sleep(1)
        countdown_info.config(text="Time Remaining")
        #*Call next 45 sec function
        forty_five_sec()
        random_choose()

five_sec()

mainloop()
