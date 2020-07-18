from tkinter import *
from tkinter import messagebox
import tkinter.font
import sqlite3
import random
import time
import pygame
pygame.init()
from pygame import mixer
mixer.init()

userwindow = Tk()
userwindow.title("Select User")

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
        print("1")
        if score > int(highscore_table):
            question_text += "NEW HIGHSCORE!\n"
            #!Have to specify users to update
            print("2")
            cursor.execute(f"UPDATE highscores SET {difficulty.get()} = {score} WHERE username ='{user.get()}'")
            print("3")
        question_text += f"Your score is {score}.\nContinue playing?"


        response = messagebox.askyesno("Continue?", question_text)
        game.destroy()

        if response == YES:
            preparationwindow()
        
        connection.commit()
        connection.close()

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

def game_window():
    global five_sec_countdown
    global countdown_number
    global countdown_info
    global forty_five_sec_timer
    global answer_list
    global main_entry
    global audio_list
    global main_label
    global score
    global highscore_table
    global game
    global main_entry_text
    global current_score
    global background_list

    preparation.destroy()
    game = Tk()
    game.title("Main game window")

    colour_list = ['yellow', 'green yellow', 'green', 'sky blue', 'white', 'gray', 'orange', 'pink', 'magenta', 'red', 'purple', 'blue', 'black']
    answer_list = ['yellow', 'light green', 'green', 'light blue', 'white', 'gray', 'orange', 'pink', 'magenta', 'red', 'purple', 'blue', 'black']
    background_list = ['yellow', 'green yellow', 'green', 'sky blue', 'white', 'gray', 'orange', 'pink', 'magenta', 'red', 'purple', 'blue']
    audio_list = ['audio/yellow.mp3', 'audio/light_green.mp3', 'audio/green.mp3', 'audio/light_blue.mp3', 'audio/white.mp3', 'audio/gray.mp3', 'audio/orange.mp3', 'audio/pink.mp3', 'audio/magenta.mp3', 'audio/red.mp3', 'audio/purple.mp3', 'audio/blue.mp3', 'audio/black.mp3']

    score = 0
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

    forty_five_sec_timer = 10
    five_sec_countdown = 5

    five_sec()

def rules_function():
    rules = Toplevel()
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


    note_4_text = "4)The answer ISN'T case-sensitive! It wouldn't matter if you type in\n all lower-case, all upper-case, or first letter capitalized etc.\nBUT, make sure to add a space for two-word colours!\n"
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

def view_highscores():
    highscores = Toplevel()
    highscores.title("Highscores!!")

    connection = sqlite3.connect('highscores.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM highscores")
    record_highscores = cursor.fetchall()

    highscore_header_font = tkinter.font.Font(size=20, weight="bold", slant="italic", underline=1)
    highscore_header_label = Label(highscores, text="Highscores", font=highscore_header_font)
    highscore_header_label.grid(row=0, column=0, columnspan=4)



    users_label = Label(highscores, text="Users", width=8, relief=RIDGE)
    users_label.grid(row=1, column=0)

    easy_label = Label(highscores, text="Easy", width=8, relief=RIDGE)
    easy_label.grid(row=1, column=1)

    medium_label = Label(highscores, text="Medium", width=8, relief=RIDGE)
    medium_label.grid(row=1, column=2)

    hard_label = Label(highscores, text="Hard", width=8, relief=RIDGE)
    hard_label.grid(row=1, column=3)



    row_checker = 3
    username_list = []
    easy_highscores_list = []
    medium_highscores_list = []
    hard_highscores_list = []
    for tuples in record_highscores:
        column_checker = 0
        for item in range(len(tuples)):
            if item == 0:
                username_list.append(tuples[item])
            elif item == 1:
                easy_highscores_list.append(tuples[item])
            elif item == 2:
                medium_highscores_list.append(tuples[item])
            elif item == 3:
                hard_highscores_list.append(tuples[item])
            b = Label(highscores, text=tuples[item], width=8, relief=RIDGE)
            b.grid(row=row_checker, column=column_checker)
            column_checker += 1
        row_checker += 1


    overall_max_easy = ""
    overall_max_medium = ""
    overall_max_hard = ""


    overall_max_easy += str(max(map(int, easy_highscores_list)))
    overall_max_medium += str(max(map(int, medium_highscores_list)))
    overall_max_hard += str(max(map(int, hard_highscores_list)))


    overall_max_easy += f"\n({username_list[easy_highscores_list.index(overall_max_easy)]})"
    overall_max_medium += f"\n({username_list[medium_highscores_list.index(overall_max_medium)]})"
    overall_max_hard += f"\n({username_list[hard_highscores_list.index(overall_max_hard)]})"

    max_frame = LabelFrame(highscores, bg="red")
    a = Label(max_frame, text="OVERALL\nMAX", relief=RIDGE, width=8)
    a.grid(row=0, column=0)
    b = Label(max_frame, text=overall_max_easy, relief=RIDGE, width=8)
    b.grid(row=0, column=1)
    c = Label(max_frame, text=overall_max_medium, relief=RIDGE, width=8)
    c.grid(row=0, column=2)
    d = Label(max_frame, text=overall_max_hard, relief=RIDGE, width=8)
    d.grid(row=0, column=3)
    max_frame.grid(row=2,column=0, columnspan=4)
            

    connection.commit()
    connection.close()


def preparationwindow():
    global difficulty
    global preparation
    preparation = Tk()
    preparation.title("Preparation Window")
    header_preparation_font = tkinter.font.Font(size=20, weight="bold", slant="italic", underline=1)
    header_preparation_label = Label(preparation, text="Choose difficulty", font=header_preparation_font)
    header_preparation_label.grid(row=0, column=0)

    difficulty = StringVar()
    #*I will have to set theseaccording to the column name of the highscore table.
    #*Then, it will be easier to access and change data later on.
    difficulty.set("easy_highscore")

    easy_radiobutton = Radiobutton(preparation, text="Easy\n(No additional tricks)", variable=difficulty, value="easy_highscore")
    easy_radiobutton.grid(row=1, column=0)
    medium_radiobutton = Radiobutton(preparation, text="Medium\n(Entry boxes change colour)", variable=difficulty, value="medium_highscore")
    medium_radiobutton.grid(row=2, column=0)
    hard_radiobutton = Radiobutton(preparation, text="Hard\n(Medium + voice distraction)", variable=difficulty, value="hard_highscore")
    hard_radiobutton.grid(row=3, column=0)

    rules_button = Button(preparation, text="How to play this game", command=rules_function, bg="green yellow", width=20)
    rules_button.grid(row=4, column=0)

    highscores_button = Button(preparation, text="View highscores", command=view_highscores, bg="yellow", width=20)
    highscores_button.grid(row=5, column=0)

    start_button = Button(preparation, text="START GAME!!", height=3, width=20, bg="green yellow", command=game_window)
    start_button.grid(row=6, column=0)


def login():
    userwindow.destroy()
    preparationwindow()


def add_user():
    connection = sqlite3.connect('highscores.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO highscores VALUES (:username, :easy_highscore, :medium_highscore, :hard_highscore)", 
    {
        'username' : checker.get(),
        'easy_highscore': '0',
        'medium_highscore': '0',
        'hard_highscore': '0'

    }
    )
    userwindow.destroy()
    connection.commit()
    connection.close()

    user.set(checker.get())
    preparationwindow()

def check(var, index, mode):
    #*For when there is nothing in record
    if len(checker.get()) == 0 or len(checker.get()) > 15:
        if len(checker.get()) == 0:
            new_user_label_text = f"'{checker.get()}'' is an empty username."
        else:
            new_user_label_text = f"Username '{checker.get()}' is too long."
        new_user_frame.config(bg="red")
        new_user_label.config(text=new_user_label_text)
        add_user_button.config(state=DISABLED)
    else:
        new_user_frame.config(bg="green yellow")
        new_user_label_text = f"'{checker.get()}' is a valid username.'"
        new_user_label.config(text=new_user_label_text)
        add_user_button.config(state=NORMAL)
    
    for name in record:
        if checker.get() == name[0]:
            new_user_frame.config(bg="red")
            new_user_label_text = f"'{checker.get()}' is an existing username."
            new_user_label.config(text=new_user_label_text)
            add_user_button.config(state=DISABLED)
            break
        elif len(checker.get()) == 0 or len(checker.get()) > 15:
            if len(checker.get()) == 0:
                new_user_label_text = f"'{checker.get()}'' is an empty username."
            else:
                new_user_label_text = f"Username '{checker.get()}' is too long."
            new_user_frame.config(bg="red")
            new_user_label.config(text=new_user_label_text)
            add_user_button.config(state=DISABLED)
            break
        else:
            new_user_frame.config(bg="green yellow")
            new_user_label_text = f"'{checker.get()}' is a valid username.'"
            new_user_label.config(text=new_user_label_text)
            add_user_button.config(state=NORMAL)

def new_user():
    global checker
    global new_user_frame
    global new_user_label
    global add_user_button
    checker = StringVar()

    new_user_button.config(state=DISABLED)
    new_user_frame = LabelFrame(userwindow, bg="red", width=20)
    new_user_entry = Entry(new_user_frame, textvariable=checker)
    checker.trace_add('write', check)
    new_user_entry.grid(row=0, column=0)
    new_user_label = Label(new_user_frame, text="Username cannot be empty.")
    new_user_label.grid(row=1, column=0)
    add_user_button = Button(new_user_frame, text="Add User/Proceed", command=add_user, bg="green yellow")
    add_user_button.grid(row=2, column=0)
    new_user_frame.grid(row=row_tracker, column=0)

def view_highscores():
    highscores = Toplevel()
    highscores.title("Highscores!!")

    connection = sqlite3.connect('highscores.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM highscores")
    record_highscores = cursor.fetchall()

    highscore_header_font = tkinter.font.Font(size=20, weight="bold", slant="italic", underline=1)
    highscore_header_label = Label(highscores, text="Highscores", font=highscore_header_font)
    highscore_header_label.grid(row=0, column=0, columnspan=4)



    users_label = Label(highscores, text="Users", width=8, relief=RIDGE)
    users_label.grid(row=1, column=0)

    easy_label = Label(highscores, text="Easy", width=8, relief=RIDGE)
    easy_label.grid(row=1, column=1)

    medium_label = Label(highscores, text="Medium", width=8, relief=RIDGE)
    medium_label.grid(row=1, column=2)

    hard_label = Label(highscores, text="Hard", width=8, relief=RIDGE)
    hard_label.grid(row=1, column=3)



    row_checker = 3
    username_list = []
    easy_highscores_list = []
    medium_highscores_list = []
    hard_highscores_list = []
    for tuples in record_highscores:
        column_checker = 0
        for item in range(len(tuples)):
            if item == 0:
                username_list.append(tuples[item])
            elif item == 1:
                easy_highscores_list.append(tuples[item])
            elif item == 2:
                medium_highscores_list.append(tuples[item])
            elif item == 3:
                hard_highscores_list.append(tuples[item])
            b = Label(highscores, text=tuples[item], width=8, relief=RIDGE)
            b.grid(row=row_checker, column=column_checker)
            column_checker += 1
        row_checker += 1


    overall_max_easy = ""
    overall_max_medium = ""
    overall_max_hard = ""


    overall_max_easy += str(max(map(int, easy_highscores_list)))
    overall_max_medium += str(max(map(int, medium_highscores_list)))
    overall_max_hard += str(max(map(int, hard_highscores_list)))


    overall_max_easy += f"\n({username_list[easy_highscores_list.index(overall_max_easy)]})"
    overall_max_medium += f"\n({username_list[medium_highscores_list.index(overall_max_medium)]})"
    overall_max_hard += f"\n({username_list[hard_highscores_list.index(overall_max_hard)]})"

    max_frame = LabelFrame(highscores, bg="red")
    a = Label(max_frame, text="OVERALL\nMAX", relief=RIDGE, width=8)
    a.grid(row=0, column=0)
    b = Label(max_frame, text=overall_max_easy, relief=RIDGE, width=8)
    b.grid(row=0, column=1)
    c = Label(max_frame, text=overall_max_medium, relief=RIDGE, width=8)
    c.grid(row=0, column=2)
    d = Label(max_frame, text=overall_max_hard, relief=RIDGE, width=8)
    d.grid(row=0, column=3)
    max_frame.grid(row=2,column=0, columnspan=4)
            

    connection.commit()
    connection.close()

header_font = tkinter.font.Font(size=13, weight="bold", slant="italic", underline=1)
header_label = Label(userwindow, text="CHOOSE USER ACCOUNT", font=header_font)
header_label.grid(row=0, column=0)

connection = sqlite3.connect('highscores.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM highscores")

record = cursor.fetchall()
row_tracker = 1
user = StringVar()
login_state = NORMAL

try:
    user.set(record[0][0])
except IndexError:
    login_state = DISABLED

for i in record:
    a = Radiobutton(userwindow, text=i[0], variable=user, value=i[0], width=10, anchor=W)
    a.grid(row=row_tracker, column=0)
    row_tracker += 1

login_button = Button(userwindow, text="Login", command=login, state=login_state, bg="green yellow", width=20)
login_button.grid(row=row_tracker, column=0)
row_tracker += 1

highscores_button = Button(userwindow, text="View Highscores", command=view_highscores, state=login_state, bg="yellow", width=20)
highscores_button.grid(row=row_tracker, column=0)
row_tracker += 1

new_user_button = Button(userwindow, text="Create New User Account", command=new_user, bg="green yellow", width=20)
new_user_button.grid(row=row_tracker, column=0)
row_tracker += 1

connection.commit()
connection.close()

mainloop()
