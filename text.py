# Created by Mervyn Smith
import tkinter as tk

root = tk.Tk()

f_name = tk.Label(root, text="First Name:")
f_name.grid(row = 0, column = 0)

e1 = tk.Entry(root)
e1.grid(row = 1, column = 0)

b1 = tk.Button(root, text="Submit")
b1.grid(row = 2, column = 0, columnspan = 3)

root.mainloop()