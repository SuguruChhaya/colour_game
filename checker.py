'''
In this project I will make a tricky game in which the player has to type the colour of the text of a colour.
For example, if "white" shows up with an fg of black, I have to type in black.

My thoughts/requirements:
1. This is obviously a timed project, so I want to to use the time module. I think I can make a dropdown menu for the user
to select the time span.
2. I want the entry to auto-detect whether what I typed in the textbox was correct or not. I want to make this non-case sensitive
to be leniant to players.
3. Since I learned about databses, I want to connect this game with a database so players can play with different usernames.
I won't get into passwords and all that becuase that is another databse project. The default account is Guest and I can 
in my username for scores to be scored on my account. I just want an error to pop up if someone has already claimed the account name.
I also want to create a leaderboard so people can see high scores.I think I can create new windows for that.
4. I think I can make the game trickier by adding twists to it. For example, I can change the bg colour of the entry box to the
same colour as what the text was saying so it will confuse people even more. Another idea is to play audio of my voice when 
the time switches. Constantly play the same audio while the player doesn't get it so it will get harder. To do this I have 
to learn how to play audio on tkinter. I think incorporating pygame will b e good because I need to be able to repeat, adjust volume,
know when to cut etc so...
'''

#*In this first step, I want to make a system which autodetects the if I type in something.
from tkinter import *
root = Tk()

#*Works Brilliantly!!
checker = StringVar()
def check(var, index, mode):
    global entry_box
    if checker.get().lower() == "suguru":
        a = Label(root, text="You wrote my name!!")
        a.pack()
        entry_box.delete(0, END)



#*Since I couldn't add a command to an entry, https://stackoverflow.com/questions/6548837/how-do-i-get-an-event-callback-when-a-tkinter-entry-widget-is-modified
#*recommends me to use the .trace method.


entry_box = Entry(root, textvariable=checker)
checker.trace_add('write', check)
entry_box.pack()

mainloop()
