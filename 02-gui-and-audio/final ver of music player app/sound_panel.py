from tkinter import*
import pygame.mixer  #3 function in here toggle, init_frame, volume details

class SoundPanel(Frame):
    def __init__(self, app, mixer, sound_file):  #goi khoi dau init va frame
        Frame.__init__(self, app)
        self.track = mixer.Sound(sound_file)   #track la mixer sound file
        self.track_playing = IntVar() #value on off
        display_name = sound_file[:20]  # only show first 20 characters
        track_button = Checkbutton(self, variable = self.track_playing,
                                       command = self.track_toggle, text = sound_file) #toggle on off

        track_button.pack(side = LEFT)
        self.volume = DoubleVar() #doublevar to hold float 1.0
        self.volume.set(self.track.get_volume())
        volume_scale = Scale(self, variable = self.volume, from_ = 0.0, to = 1.0,
                                 resolution = 0.1, command = self.change_volume,
                                     label = "Volume", orient = HORIZONTAL) #tao thanh volume gia tri 0.0-1.0
        volume_scale.pack(side = RIGHT)                                     #thay doi 0.1                                        

    def track_toggle(self):
        if self.track_playing.get() == 1: #toggle play n loop or stop
            self.track.play(loops = -1)            
        else:
            self.track.stop()

    def change_volume(self, v): #thay doi am luong?
        self.track.set_volume(self.volume.get())
