import tkinter as tk
from tkinter import Label, StringVar, Entry, Button, Menu, Frame, Tk, Canvas
import subprocess


class SampleApp(tk.Tk):
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)

            container = tk.Frame(self)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)
            print("Hellooo Stack")
            self.frames = {}
            for F in (MainWindow,Master):
                frame = F(container, self)
                self.frames[F] = frame

                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(MainWindow)

        def show_frame(self, c):

            frame = self.frames[c]
            frame.tkraise()
class MainWindow(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)

            button = tk.Button(self, text="Connections",compound=tk.LEFT, command =lambda: exit())
            button.pack(pady=50)
            button1 = tk.Button(self, text="   Locker            ", compound=tk.LEFT,
                                    command=lambda: controller.show_frame(Master))
            button1.pack(pady=50)

class Master(tk.Frame):
       def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            menubar = Menu(self)
            filemenu = Menu(menubar,tearoff=0)
            filemenu.add_command(label="New",)
            filemenu.add_command(label="Open",)
            filemenu.add_command(label="Save As..")
            filemenu.add_command(label="Colour")
            filemenu.add_command(label="Close")
            menubar.add_cascade(label="File",menu=filemenu)
            controller.configure(menu = menubar)
if __name__ == "__main__":
        app = SampleApp()
        app.title("APPS")
        app.mainloop()