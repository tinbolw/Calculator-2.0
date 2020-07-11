import random
import math
import tkinter as tk
import webbrowser

#TODO
#add pemdas

isFirstNum = True
isSecondNum = False

firstNum = 0
secondNum = 0
indexNum = 0

addNum = False
subtractNum = False
divideNum = False
multiplyNum = False


def reportIssue():
	webbrowser.open('https://github.com/tinbolw/Calculator-2.0/issues')

def clearAll():
	global isFirstNum
	global indexNum
	global firstNum
	global secondNum
	firstNum = 0
	secondNum = 0
	outputBox.delete(0, tk.END)
	indexNum = 0
	isFirstNum = True

def deleteNum():
	global indexNum
	outputBox.delete(indexNum, tk.END)
	indexNum -= 1

#All addnum functions

def add1():
	global isFirstNum
	global indexNum
	if isFirstNum:
		outputBox.insert(indexNum, 1)
		firstNumVar = outputBox.get()
		indexNum += 1
	elif isSecondNum:
		outputBox.insert(indexNum, 1)
		secondNumVar = outputBox.get()
		indexNum += 1


def add2():
	global indexNum
	outputBox.insert(indexNum, 2)
	indexNum += 1

def add3():
	global indexNum
	outputBox.insert(indexNum, 3)
	indexNum += 1


def add4():
	global indexNum
	outputBox.insert(indexNum, 4)
	indexNum += 1

def add5():
	global indexNum
	outputBox.insert(indexNum, 5)
	indexNum += 1

def add6():
	global indexNum
	outputBox.insert(indexNum, 6)
	indexNum += 1

def add7():
	global indexNum
	outputBox.insert(indexNum, 7)
	indexNum += 1

def add8():
	global indexNum
	outputBox.insert(indexNum, 8)
	indexNum += 1

def add9():
	global indexNum
	outputBox.insert(indexNum, 9)
	indexNum += 1

def add0():
	global indexNum
	outputBox.insert(indexNum, 0)
	indexNum += 1

#All operator functions

def addNum():
	global firstNumVar
	global secondNumVar
	global isAdd
	firstNumVar = outputBox.get()
	outputBox.delete(0, tk.END)
	isSecondNum = True
	isAdd = True

def calculate():
	global firstNumVar
	global secondNumVar
	secondNumVar = outputBox.get()
	outputBox.delete(0, tk.END)
	if isAdd:
		outputBox.insert(str(firstNumVar + secondNumVar))


root = tk.Tk()

root.title("Calculator")

button1Label = tk.Label(root, text = "Calculator V 1.0.0")
button1Label.grid(row=0, column=2)

outputBox = tk.Entry(root,)
outputBox.grid(row=1,column=2)

#All the number buttons

button1 = tk.Button(root, width=15, height=6, text = "1", command = add1)
button1.grid(row=2, column=1)

button2 = tk.Button(root, width=15, height=6, text = "2", command = add2)
button2.grid(row=2, column=2)

button3 = tk.Button(root, width=15, height=6, text = "3", command = add3)
button3.grid(row=2, column=3)

button4 = tk.Button(root, width=15, height=6, text = "4", command = add4)
button4.grid(row=3, column=1)

button5 = tk.Button(root, width=15, height=6, text = "5", command = add5)
button5.grid(row=3, column=2)

button6 = tk.Button(root, width=15, height=6, text = "6", command = add6)
button6.grid(row=3, column=3)

button7 = tk.Button(root, width=15, height=6, text = "7", command = add7)
button7.grid(row=4, column=1)

button8 = tk.Button(root, width=15, height=6, text = "8", command = add8)
button8.grid(row=4, column=2)

button9 = tk.Button(root, width=15, height=6, text = "9", command = add9)
button9.grid(row=4, column=3)

button0 = tk.Button(root, width=15, height=6, text = "0", command = add0)
button0.grid(row=5, column=1)

#All the operator buttons

buttonDecimal = tk.Button(root, width=15, height=6, text = ".")
buttonDecimal.grid(row=5, column=2)

buttonEquals = tk.Button(root, width=15, height=6, text = "=", command = calculate)
buttonEquals.grid(row=5, column=3)

buttonDelete = tk.Button(root, width=15, height=6, text = "Delete", command = deleteNum)
buttonDelete.grid(row=2, column=4)

buttonDivide = tk.Button(root, width=15, height=6, text = "/")
buttonDivide.grid(row=3, column=4)

buttonMultiply = tk.Button(root, width=15, height=6, text = "x")
buttonMultiply.grid(row=4, column=4)

buttonSubtract = tk.Button(root, width=15, height=6, text = "-")
buttonSubtract.grid(row=5, column=4)

buttonAdd = tk.Button(root, width=15, height=6, text = "+", command = addNum)
buttonAdd.grid(row=6, column=4)

buttonBug = tk.Button(root, width=15, height=6, text = "Report \na bug", command = reportIssue)
buttonBug.grid(row=6, column=1)

buttonClear = tk.Button(root, width=30, height=6, text="Clear", command = clearAll)
buttonClear.grid(row=6, column=2)

root.mainloop()