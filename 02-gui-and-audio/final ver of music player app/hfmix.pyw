from tkinter import*
from sound_panel import*  #import module tao app tao panel frame tu sound_panel(3 def) va lenh tat
import pygame.mixer
import os

app = Tk()
app.title("Head First Mix")


mixer = pygame.mixer
mixer.init()

#create_gui(app, mixer, "Oh Qué Será_, but its slowed to perfection.mp3")
#create_gui(app, mixer, "carhorn.wav")

dirList = os.listdir(".")
for fname in dirList:
    if fname.endswith((".wav", ".mp3")):
        panel = SoundPanel (app, mixer, fname)
        panel.pack()

def shutdown():
    mixer.stop()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", shutdown)

app.mainloop()
