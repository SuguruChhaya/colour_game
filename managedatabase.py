'''
This file is solely for creating the columns and all for the databases, adding, updating, and deleting them.
This is so that I can experiment with databases with the other files.
If I need to change the database, I can do it from this file.
'''
from tkinter import *
import sqlite3

root = Tk()
root.title("Manage Database")

connection = sqlite3.connect('highscores.db')
cursor = connection.cursor()

def add_record():
    connection = sqlite3.connect('highscores.db')
    cursor = connection.cursor()

    #!The keys for the dictionary would correspond to the VALUES
    cursor.execute("INSERT INTO highscores VALUES (:username, :easy_highscore, :medium_highscore, :hard_highscore)", 
    {
        'username' : username_entry.get(),
        'easy_highscore': easy_highscore_entry.get(),
        'medium_highscore': medium_highscore_entry.get(),
        'hard_highscore': hard_highscore_entry.get()
    })

    username_entry.delete(0, END)
    easy_highscore_entry.delete(0, END)
    medium_highscore_entry.delete(0, END)
    hard_highscore_entry.delete(0, END)

    connection.commit()
    connection.close()

def show_record():
    connection = sqlite3.connect('highscores.db')
    cursor = connection.cursor()

    cursor.execute("SELECT *, oid FROM highscores")

    record_show = cursor.fetchall()
    global record_show_label
    record_show_label.grid_forget()
    print_record = ""
    for item in record_show:
        print_record += str(item[4]) + "\t" + item[0] + "\t" + item[1] + " " + item[2] + " " + item[3] + "\n"
    
    record_show_label = Label(root, text=print_record)
    record_show_label.grid(row=9, column=0, columnspan=2)


    connection.commit()
    connection.close()


def delete_record():
    connection = sqlite3.connect('highscores.db')
    cursor = connection.cursor()
    #*I could replace oid= to first_name etc. I have to break the quotation before deleting ID.
    cursor.execute("DELETE FROM highscores WHERE oid= " + select_id_entry.get())




    connection.commit()
    connection.close()

def save_record():
    connection = sqlite3.connect('highscores.db')
    cursor = connection.cursor()

    cursor.execute("""UPDATE highscores SET
    username = :username,
    easy_highscore = :easy_highscore,
    medium_highscore = :medium_highscore,
    hard_highscore = :hard_highscore

    WHERE oid = :oid""",
    
    {
        'username' : username_entry_editor.get(),
        'easy_highscore' : easy_highscore_entry_editor.get(),
        'medium_highscore' : medium_highscore_entry_editor.get(),
        'hard_highscore' : hard_highscore_entry_editor.get(),
        'oid' : select_id_entry.get()

    }
    )

    editor.destroy()

    connection.commit()
    connection.close()


def update_record():
    connection = sqlite3.connect('highscores.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM highscores WHERE oid=" + select_id_entry.get())
    record_update = cursor.fetchall()

    global editor

    editor = Toplevel()
    editor.title("Edit record")

    #*Labels
    username_label_editor = Label(editor, text="username")
    username_label_editor.grid(row=0, column=0)

    easy_highscore_label_editor = Label(editor, text="easy_highscore")
    easy_highscore_label_editor.grid(row=1, column=0)

    medium_highscore_label_editor = Label(editor, text="medium_highscore")
    medium_highscore_label_editor.grid(row=2, column=0)

    hard_highscore_label_editor = Label(editor, text="hard_highscore")
    hard_highscore_label_editor.grid(row=3, column=0)

    #*Entries
    global username_entry_editor
    global easy_highscore_entry_editor
    global medium_highscore_entry_editor
    global hard_highscore_entry_editor

    username_entry_editor = Entry(editor)
    username_entry_editor.grid(row=0, column=1)

    easy_highscore_entry_editor = Entry(editor)
    easy_highscore_entry_editor.grid(row=1, column=1)

    medium_highscore_entry_editor = Entry(editor)
    medium_highscore_entry_editor.grid(row=2, column=1)

    hard_highscore_entry_editor = Entry(editor)
    hard_highscore_entry_editor.grid(row=3, column=1)

    save_record_button = Button(editor, text="Save record", command=save_record)
    save_record_button.grid(row=4, column=0, columnspan=2)

    entry_list = [username_entry_editor, easy_highscore_entry_editor, medium_highscore_entry_editor, hard_highscore_entry_editor]
    counter = 0
    for item in record_update[0]:
        entry_list[counter].insert(0, item)
        counter += 1

    connection.commit()
    connection.close()


#*Create labels
username_label = Label(root, text="username")
username_label.grid(row=0, column=0)

easy_highscore_label = Label(root, text="easy_highscore")
easy_highscore_label.grid(row=1, column=0)

medium_highscore_label = Label(root, text="medium_highscore")
medium_highscore_label.grid(row=2, column=0)

hard_highscore_label = Label(root, text="hard_highscore")
hard_highscore_label.grid(row=3, column=0)

#*Create entries
username_entry = Entry(root)
username_entry.grid(row=0, column=1)

easy_highscore_entry = Entry(root)
easy_highscore_entry.grid(row=1, column=1)

medium_highscore_entry = Entry(root)
medium_highscore_entry.grid(row=2, column=1)

hard_highscore_entry = Entry(root)
hard_highscore_entry.grid(row=3, column=1)

#*Creating Buttons
add_record_button = Button(root, text="Add record to database", command=add_record)
add_record_button.grid(row=4, column=0, columnspan=2)

show_record_button = Button(root, text="Show records", command=show_record)
show_record_button.grid(row=5, column=0, columnspan=2)

record_show_label = Label(root, text="")
record_show_label.grid(row=9, column=0)

select_id_label = Label(root, text="Select ID#")
select_id_label.grid(row=6, column=0)

select_id_entry = Entry(root)
select_id_entry.grid(row=6, column=1)

delete_record_button = Button(root, text="Delete record", command=delete_record)
delete_record_button.grid(row=7, column=0, columnspan=2)

update_record_button = Button(root, text="Update record", command=update_record)
update_record_button.grid(row=8, column=0, columnspan=2)







connection.commit()
connection.close()

mainloop()