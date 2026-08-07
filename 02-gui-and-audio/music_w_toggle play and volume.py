from tkinter import*
from tkinter.messagebox import askokcancel
import pygame.mixer


app=Tk()
app.title("list nhac dj")
sound_file = "Oh Qué Será_, but its slowed to perfection.mp3"
mixer = pygame.mixer
mixer.init()

def track_toggle():
    if track_playing.get() == 1:
        track.play(loops=-1)
    else:
        track.stop()

def change_volume(v):
    track.set_volume(volume.get())

track = mixer.Sound(sound_file)
track_playing = IntVar()
track_button = Checkbutton(app, variable = track_playing,
                                command = track_toggle,
                                text    = sound_file)
track_button.pack(side = LEFT)

volume = DoubleVar()
volume_scale = Scale(app,
                     variable   = volume,
                     from_      = 0.0,
                     to         = 1.0,
                     resolution = 0.1,
                     command    = change_volume,
                     label      = "Volume",
                     orient     = HORIZONTAL)
volume_scale.pack(side = RIGHT)

def shutdown():
    if askokcancel(title = 'Are you sure?', message = 'Do you really want to quit?'):
        track.stop() #debugged myself for destroy not working properly
        mixer.quit() #AI recommended to clear before quit
        app.destroy()
        

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop() 
