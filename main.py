import random
import math
import tkinter as tk

def clearNumbers():
	print("WIP")
	#TODO

def add1():
	print("WIP")
	#TODO

def add2():
	print("WIP")
	#TODO

def add3():
	print("WIP")
	#TODO

def add4():
	print("WIP")
	#TODO

def add5():
	print("WIP")
	#TODO

def add6():
	print("WIP")
	#TODO

def add7():
	print("WIP")
	#TODO

def add8():
	print("WIP")
	#TODO

def add9():
	print("WIP")
	#TODO

def add0():
	print("WIP")
	#TODO

root = tk.Tk()

Label1 = tk.Label(root, text="Calculator Version 1.0.0")
Label1.pack()

clearButton = tk.Button(root, width=5, height=2, text = "Clear", command = clearNumbers)

Button1 = tk.Button(root, width = 5, height = 2, text = "1", command = add1)
Button1.pack()

Button2 = tk.Button(root, width = 5, height = 2, text = "2", command = add2)
Button2.pack()

Button3 = tk.Button(root, width = 5, height = 2, text = "3", command = add3)
Button3.pack()

Button4 = tk.Button(root, width = 5, height = 2, text = "4", command = add4)
Button4.pack()

Button5 = tk.Button(root, width = 5, height = 2, text = "5", command = add5)
Button5.pack()

Button6 = tk.Button(root, width = 5, height = 2, text = "6", command = add6)
Button6.pack()

Button7 = tk.Button(root, width = 5, height = 2, text = "7", command = add7)
Button7.pack()

Button8 = tk.Button(root, width = 5, height = 2, text = "8", command = add8)
Button8.pack()

Button9 = tk.Button(root, width = 5, height = 2, text = "9", command = add9)
Button9.pack()

Button0 = tk.Button(root, width = 5, height = 2, text = "0", command = add0)
Button0.pack()

root.mainloop()
