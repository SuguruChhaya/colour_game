'''
In this file, I will learn how to use audio in my tkinter game.
I am going to try the winsound module
'''
from tkinter import *
import winsound
import time
import pygame
from pygame import mixer
pygame.init()
mixer.init()
root = Tk()
def countdown(t):
    while t > 0:
        try:
            countdown_label.grid_forget()
        except NameError:
            pass
        print(t)
        countdown_label = Label(root, text=str(t))
        countdown_label.grid(row=0, column=0)
        t -= 1
        time.sleep(1)

#*winsound has a weird thing how the running stops when it plays someting. So I think I shouldn't just cut off the playing.
#!In fact, it blocks all the other functions from running(including the timer), so maybe I shouldn't use this.
def countdown2():
    global initial
    global a
    if a == 0:
        root.destroy()
        #*Since I am calling a label I have destroyed in line 39, the tcl error occurs. I can fix this by not calling it.
    countdown_label.config(text=str(a))
    a -=1
    countdown_label.after(1000, countdown2)

def play_loop():
    #?.ogg  somehow doesn't work so mp3 is the best option.
    if stop:
        mixer.music.load('light_green.mp3')
        mixer.music.play()
    #*For this case, I guess since the window the .after 
        countdown_label.after(2000, play_loop)
    else:
        pass

stop = True
initial = True
a = 5
play_loop_time = 2
countdown_label = Label(root, text=str(a))
countdown_label.grid(row=0, column=0)
countdown2()
play_loop()
mainloop()









#!I think the audio type has to be a .wav file.
#winsound.PlaySound('ending.m4a', winsound.SND_FILENAME)