import random
import math
import tkinter as tk

#TODO
#add pemdas

mathVar = 0

def add1():
	outputBox.insert(0, 1)
	mathVar1 = outputBox.get()

root = tk.Tk()

root.title("Calculator")

button1Label = tk.Label(root, text = "Calculator V 1.0.0")
button1Label.grid(row=0, column=2)

outputBox = tk.Entry(root,)
outputBox.grid(row=1,column=2)

button1 = tk.Button(root, width=15, height=6, text = "1", command = add1)
button1.grid(row=2, column=1)

button2 = tk.Button(root, width=15, height=6, text = "2")
button2.grid(row=2, column=2)

button3 = tk.Button(root, width=15, height=6, text = "3")
button3.grid(row=2, column=3)

button4 = tk.Button(root, width=15, height=6, text = "4")
button4.grid(row=3, column=1)

button5 = tk.Button(root, width=15, height=6, text = "5")
button5.grid(row=3, column=2)

button6 = tk.Button(root, width=15, height=6, text = "6")
button6.grid(row=3, column=3)

button7 = tk.Button(root, width=15, height=6, text = "7")
button7.grid(row=4, column=1)

button8 = tk.Button(root, width=15, height=6, text = "8")
button8.grid(row=4, column=2)

button9 = tk.Button(root, width=15, height=6, text = "9")
button9.grid(row=4, column=3)

button0 = tk.Button(root, width=15, height=6, text = "0")
button0.grid(row=5, column=1)

buttonDecimal = tk.Button(root, width=15, height=6, text = ".")
buttonDecimal.grid(row=5, column=2)

buttonEquals = tk.Button(root, width=15, height=6, text = "=")
buttonEquals.grid(row=5, column=3)

buttonDelete = tk.Button(root, width=15, height=6, text = "Delete")
buttonDelete.grid(row=2, column=4)

buttonDivide = tk.Button(root, width=15, height=6, text = "/")
buttonDivide.grid(row=3, column=4)

buttonMultiply = tk.Button(root, width=15, height=6, text = "x")
buttonMultiply.grid(row=4, column=4)

buttonSubtract = tk.Button(root, width=15, height=6, text = "-")
buttonSubtract.grid(row=5, column=4)

buttonAdd = tk.Button(root, width=15, height=6, text = "+")
buttonAdd.grid(row=6, column=4)

root.mainloop()