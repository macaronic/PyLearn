import tkinter as tk

root = tk.Tk()


def printName():
    print("hello my name is teo")


button_1 = tk.Button(root, text="print", command=printName)
button_1.pack()
root.mainloop()