# -*- coding: utf-8 -*-
import time
import threading
import tkinter as tk
from PIL import Image, ImageTk
import Settings as s
import random




class Screen(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self, className='Poppy')
        self._frame = None
        
        # robot or simulation on pc
        if s.RUN_MODE == 'ROBOT':
            self.attributes('-fullscreen', True) 
        else:
            self.geometry("800x600") 
            
        self.switch_frame(SelectPage)
        # self.switch_frame(EyesPage)
        self["bg"] = "#F3FCFB"
        
        # גורם לחלון לקפוץ קדימה מעל ה-VS Code
        self.lift()
        self.attributes("-topmost", True)
        self.focus_force()
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(expand=True, fill="both")
        # self._frame.pack(expand=True)




class EyesPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        image = Image.open('pictures//eyes.png')
        self.photo_image = ImageTk.PhotoImage(image)  # self. - for keeping the photo in memory so it will be shown
        tk.Label(self, image=self.photo_image).pack()

        self.bind_all("<space>", lambda event: self.reboot())

    def reboot(self):
        print("Reboot performed: Resetting inter_aff and hardwere_aff")
        # s.say("Reboot")
        if s.hardwere_aff:
            print("Resetting robot...")
            s.reboot_flag = True
        elif s.inter_aff:
            s.inter_aff = False


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom=self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

class SelectPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#F3FCFB")
        tk.Label(self, text="Researcher Control", font=("Helvetica", 24), bg="#F3FCFB").pack(pady=20)
        
        # Neutral buttons for the researcher
        btn_style = {"font": ("Helvetica", 18), "width": 15, "pady": 10}
        tk.Button(self, text="Mode A", command=lambda: self.set_mode(0), **btn_style).pack(pady=5)
        tk.Button(self, text="Mode B", command=lambda: self.set_mode(1), **btn_style).pack(pady=5)
        tk.Button(self, text="Mode C", command=lambda: self.set_mode(2), **btn_style).pack(pady=5)

    def set_mode(self, mode):
        # s.WORKFLOW_MODE = mode
        # s.Team_Number = s.WORKFLOW_MODE
        s.Team_Number = mode        
        # Transition to the neutral "Waiting" page
        self.master.switch_frame(WaitingPage)


class WaitingPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="#F3FCFB")
        tk.Label(self, text="System is ready", font=("Helvetica", 30), bg="#F3FCFB").pack(pady=100)
        
        # This is the button the experimenter presses when the participant is ready
        tk.Button(self, text="START EXPERIMENT", font=("Helvetica", 24, "bold"), 
                  bg="green", fg="white", command=self.go, padx=50, pady=20).pack()

    def go(self):
        s.experiment_started = True
        self.master.switch_frame(EyesPage)

if __name__ == "__main__":
    s.screen = Screen()
    app = FullScreenApp(s.screen)
    s.screen.mainloop()
