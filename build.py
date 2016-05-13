import tkinter as tk
import sys

class Appp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._create_menubar()
        self.text = tk.Text()
        self.text.pack(side="top", fill="both", expand=True)

#the e menuto + prozoreca
    def _create_menubar(self):
        self.menubar = tk.Menu()
        self.configure(menu=self.menubar)

        #fail menu
        file_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Quit", command=self.on_quit)

        #edit menuto
        edit_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", underline=2, command=self.on_cut)
        edit_menu.add_command(label="Copy", underline=0, command=self.on_copy)
        edit_menu.add_command(label="Paste", underline=0, command=self.on_paste)


        #view
        view_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_cascade(label="Whatever", command=self.on_whatever)


    def log(self, s):
        self.text.insert("end",s + "\n")
        self.text.see("end")

    def on_cut(self): self.log("cut...")
    def on_copy(self): self.log("copy...")
    def on_paste(self): self.log("paste...")
    def on_quit(self): sys.exit(0)
    def on_whatever(self): self.log("whatever...")

if __name__ == "__main__":
    app = Appp()
    app.mainloop()