'''
There will be a total of 4 windows involved in my game.
1. Initial window where I select user or create new username.
(I will control this through radiobuttons. There will be radiobuttons for all user name and one radiobutton which will
say "CREATE NEW USER.)
2. Rules and game setting window. This window will explain the basic rules. The user can choose the level radio buttons.
(Easy: No special distractions, Medium: Entry box colour changes, Hard: Voice plays)
3. Game window (alert user to click on enrty box, countdown, play). Display the possible colours included in this game.
Play sound after game ends, display score and whether high score was achieved or not and automatically close window after
8 seconds or so.
4. Leaderboard window(This will show high scores for all difficulty levels for all users. The only time is 45 sec.)
At the top, it will show highest scores out of all the players. 


'''

from tkinter import *
import tkinter.font
import sqlite3

userwindow = Tk()
userwindow.title("Select User")

def login():
    userwindow.destroy()
    #*After this, the new window will popup.

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

def check(var, index, mode):
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
#*I think I can make the record global so I can use it when I check whether new username is valid.

record = cursor.fetchall()
row_tracker = 1
user = StringVar()
login_state = NORMAL

#*In case there are no users added in database.
try:
    user.set(record[0][0])
except IndexError:
    login_state = DISABLED

for i in record:
    a = Radiobutton(userwindow, text=i[0], variable=user, value=i[0], width=10, anchor=W)
    #*Deselect doesn't work
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