import tkinter as tk

root = tk.Tk()

topFrame = tk.Frame(root)
topFrame.pack()
bottomFrame = tk.Frame(root)
bottomFrame.pack(side=tk.BOTTOM)

button1 = tk.Button(topFrame, text="button 1", fg="red")
button2 = tk.Button(topFrame, text="button 2", fg="pink")
button3 = tk.Button(topFrame, text="button 3", fg="blue")
button4 = tk.Button(bottomFrame, text="button 4", fg="green")

button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)
button4.pack(side=tk.BOTTOM)

root.mainloop()
