from tkinter import *
import tkinter.font
import sqlite3

preparation = Tk()

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

def start_countdown():
    preparation.destroy()



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

start_button = Button(preparation, text="START GAME!!", height=3, width=20, bg="green yellow", command=start_countdown)
start_button.grid(row=6, column=0)

mainloop()