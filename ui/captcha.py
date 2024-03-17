from tkinter import Tk, Label, Entry, ttk, StringVar
from PIL import Image, ImageTk
import sv_ttk


class Captcha(Tk):
    def __init__(self, captcha: str, command):
        super(Captcha, self).__init__()
        sv_ttk.set_theme("dark")
        self.command = command
        self.display = ImageTk.PhotoImage(file=captcha)
        self.label(self.display)
        self.value = StringVar()
        self.captcha_input()
        self.ok_button()

    def label(self, image: ImageTk.PhotoImage):
        ui = ttk.Label(self, image=image)
        ui.pack()
        return ui

    def captcha_input(self):
        ui = ttk.Entry(self, textvariable=self.value)
        ui.pack()
        return ui

    def ok_button(self):
        ui = ttk.Button(self, text="OK", command=self.command)
        ui.pack()
        return ui

    def main(self):
        self.mainloop()
        return self
