import tkinter as tk

root = tk.Tk()

one = tk.Label(root, text="One", bg="green", fg="white")
one.pack()
two = tk.Label(root, text="two", bg="white")
two.pack(fill=tk.X)
three = tk.Label(root, text="three", bg="blue", fg="white")
three.pack(side=tk.LEFT, fill=tk.Y)

root.mainloop()