'''
In this file, I will try to create high scores in table format using the data from the database.
'''
from tkinter import *
import tkinter.font
import sqlite3

highscores = Tk()
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

#!I don't have to accommodate for empty players because I disabled that in the first window
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

mainloop()
