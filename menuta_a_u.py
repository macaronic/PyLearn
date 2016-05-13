import tkinter

def close():


    class Menubar1:
     exit()
window = tkinter.Tk()
menubar = tkinter.Menu(window)

filemenu = tkinter.Menu(menubar, tearoff= 0)
filemenu.add_command(label="Close", command=close)

menubar.add_cascade(label = "File", menu=filemenu)
window.config (menu=menubar)
