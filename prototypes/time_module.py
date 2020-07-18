import time
'''
Using the time module, I need to be able to do the following basic things.
1. Stopwatch for 30sec and 1 min.
2. Display the remaining time left.
3. For the hard mode where I record my voice, I need the time module to control time incriments for when the 
audio is played.
'''

import time
def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        #*The time.sleep method suspends the incriments. I always want to keep this at 1.
        time.sleep(1)
    print("BLAST OFF!")

print("How many seconds to count down? Enter an integer:")
seconds = input()
while not seconds.isdigit():
    print("That wasn't an integer! Enter an integer:")
    seconds = input()
seconds = int(seconds)
countdown(seconds)


from tkinter import *
root = Tk()

def display(a):
    if choose_time.get() == "30sec":
        time_display.config(text="00:30")
    elif choose_time.get() == "60sec":
        time_display.config(text="01:00")

choose_time = StringVar()
choose_time.set("00")
dropbox = OptionMenu(root, choose_time, *["30sec", "60sec"], command=display)
dropbox.grid(row=0, column=0)

time_display = Label(root, text="00:" + choose_time.get())
time_display.grid(row=1, column=0)

mainloop()