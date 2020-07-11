import random
import math
import tkinter as tk

root = tk.Tk()

button1Label = tk.Label(root, text = "Calculator V 1.0.0").grid(row=0, column=2)

outputBox = tk.Entry(root,).grid(row=1,column=2)


button1 = tk.Button(root, width=5, height=2, text = "1")
button1.grid(row=2, column=1)

button2 = tk.Button(root, width=5, height=2, text = "2")
button2.grid(row=2, column=2)

button3 = tk.Button(root, width=5, height=2, text = "3")
button3.grid(row=2, column=3)

button4 = tk.Button(root, width=5, height=2, text = "4")
button4.grid(row=3, column=1)

button5 = tk.Button(root, width=5, height=2, text = "5")
button5.grid(row=3, column=2)

button6 = tk.Button(root, width=5, height=2, text = "6")
button6.grid(row=3, column=3)

button7 = tk.Button(root, width=5, height=2, text = "7")
button7.grid(row=4, column=1)

button8 = tk.Button(root, width=5, height=2, text = "8")
button8.grid(row=4, column=2)

button9 = tk.Button(root, width=5, height=2, text = "9")
button9.grid(row=4, column=3)

root.mainloop()