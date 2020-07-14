import random
import math
import tkinter as tk
import webbrowser

# TODO
# add pemdas
# add decimal
# fix syntax error and divide by 0
# Giving a value to all variables

isFirstNum = True
isSecondNum = False

firstNum = 0
secondNum = 0
indexNum = 0

addNum = False
subtractNum = False
divideNum = False
multiplyNum = False
afterAnswer = False

# Extra buttons

def reportIssue():
	webbrowser.open('https://github.com/tinbolw/Calculator-2.0/issues')

def clearAll():
	global isFirstNum
	global indexNum
	global firstNum
	global secondNum
	hasNum = False
	firstNum = 0
	secondNum = 0
	outputBox.delete(0, tk.END)
	indexNum = 0
	isFirstNum = True

def deleteNum():
	global indexNum
	global hasNum
	if indexNum > 0:
		outputBox.delete(indexNum, tk.END)
		indexNum -= 1
	if indexNum == 0:
		hasNum = False

def addDecimal():
	global hasNum
	if hasNum:
		outputBox.insert(indexNum, ".")
		indexNum += 1
	elif not hasNum:
		hasNum = False
		afterAnswer = True
		outputBox.insert(0, "Syntax Error")


# All addnum functions

def add1():
	global isFirstNum
	global firstNum
	global indexNum
	global afterAnswer
	global hasNum
	if afterAnswer:
		clearAll()
		afterAnswer = False
		isFirstNum = True
		isSecondNum = False
		add1()
	elif isFirstNum:
		firstNum = str(firstNum)
		firstNum = firstNum + "1"
		firstNum = float(firstNum)
		outputBox.insert(indexNum, 1)
		indexNum += 1
		hasNum = True
	elif isSecondNum:
		secondNum = str(secondNum)
		secondNum = secondNum + "1"
		secondNum = float(secondNum)

def add2():
	global isFirstNum
	global firstNum
	global indexNum
	global afterAnswer
	if afterAnswer:
		clearAll()
		afterAnswer = False
		isFirstNum = True
		isSecondNum = False
		add2()
	elif isFirstNum:
		firstNum = str(firstNum)
		firstNum = firstNum + "2"
		firstNum = float(firstNum)
		outputBox.insert(indexNum, 2)
		indexNum += 1
	elif isSecondNum:
		secondNum = str(secondNum)
		secondNum = secondNum + "2"
		secondNum = float(secondNum)



def add3():
	global isFirstNum
	global firstNum
	global indexNum
	global afterAnswer
	if afterAnswer:
		clearAll()
		afterAnswer = False
		isFirstNum = True
		isSecondNum = False
		add3()
	elif isFirstNum:
		firstNum = str(firstNum)
		firstNum = firstNum + "3"
		firstNum = float(firstNum)
		outputBox.insert(indexNum, 3)
		indexNum += 1
	elif isSecondNum:
		secondNum = str(secondNum)
		secondNum = secondNum + "3"
		secondNum = float(secondNum)

def add4():
	global isFirstNum
	global firstNum
	global indexNum
	global afterAnswer
	if afterAnswer:
		clearAll()
		afterAnswer = False
		isFirstNum = True
		isSecondNum = False
		add4()
	elif isFirstNum:
		firstNum = str(firstNum)
		firstNum = firstNum + "4"
		firstNum = float(firstNum)
		outputBox.insert(indexNum, 4)
		indexNum += 1
	elif isSecondNum:
		secondNum = str(secondNum)
		secondNum = secondNum + "4"
		secondNum = float(secondNum)

def add5():
	global isFirstNum
	global firstNum
	global indexNum
	global afterAnswer
	if afterAnswer:
		clearAll()
		afterAnswer = False
		isFirstNum = True
		isSecondNum = False
		add5()
	elif isFirstNum:
		firstNum = str(firstNum)
		firstNum = firstNum + "5"
		firstNum = float(firstNum)
		outputBox.insert(indexNum, 5)
		indexNum += 1
	elif isSecondNum:
		secondNum = str(secondNum)
		secondNum = secondNum + "5"
		secondNum = float(secondNum)

def add6():
	global isFirstNum
	global firstNum
	global indexNum
	global afterAnswer
	if afterAnswer:
		clearAll()
		afterAnswer = False
		isFirstNum = True
		isSecondNum = False
		add6()
	elif isFirstNum:
		firstNum = str(firstNum)
		firstNum = firstNum + "6"
		firstNum = float(firstNum)
		outputBox.insert(indexNum, 6)
		indexNum += 1
	elif isSecondNum:
		secondNum = str(secondNum)
		secondNum = secondNum + "6"
		secondNum = float(secondNum)

def add7():
	global isFirstNum
	global firstNum
	global indexNum
	global afterAnswer
	if afterAnswer:
		clearAll()
		afterAnswer = False
		isFirstNum = True
		isSecondNum = False
		add7()
	elif isFirstNum:
		firstNum = str(firstNum)
		firstNum = firstNum + "4"
		firstNum = float(firstNum)
		outputBox.insert(indexNum, 7)
		indexNum += 1
	elif isSecondNum:
		secondNum = str(secondNum)
		secondNum = secondNum + "7"
		secondNum = float(secondNum)

def add8():
	global isFirstNum
	global firstNum
	global indexNum
	global afterAnswer
	if afterAnswer:
		clearAll()
		afterAnswer = False
		isFirstNum = True
		isSecondNum = False
		add8()
	elif isFirstNum:
		firstNum = str(firstNum)
		firstNum = firstNum + "8"
		firstNum = float(firstNum)
		outputBox.insert(indexNum, 8)
		indexNum += 1
	elif isSecondNum:
		secondNum = str(secondNum)
		secondNum = secondNum + "8"
		secondNum = float(secondNum)

def add9():
	global isFirstNum
	global firstNum
	global indexNum
	global afterAnswer
	if afterAnswer:
		clearAll()
		afterAnswer = False
		isFirstNum = True
		isSecondNum = False
		add9()
	elif isFirstNum:
		firstNum = str(firstNum)
		firstNum = firstNum + "9"
		firstNum = float(firstNum)
		outputBox.insert(indexNum, 9)
		indexNum += 1
	elif isSecondNum:
		secondNum = str(secondNum)
		secondNum = secondNum + "9"
		secondNum = float(secondNum)

def add0():
	global isFirstNum
	global firstNum
	global indexNum
	global afterAnswer
	if afterAnswer:
		clearAll()
		afterAnswer = False
		isFirstNum = True
		isSecondNum = False
		add0()
	elif isFirstNum:
		firstNum = str(firstNum)
		firstNum = firstNum + "0"
		firstNum = float(firstNum)
		outputBox.insert(indexNum, 0)
		indexNum += 1
	elif isSecondNum:
		secondNum = str(secondNum)
		secondNum = secondNum + "0"
		secondNum = float(secondNum)

#All operator functions

def addNum():
	global firstNumVar
	global secondNumVar
	global isAdd
	global isDivide
	global isSubtract
	global isMultiply
	firstNumVar = outputBox.get()
	outputBox.delete(0, tk.END)
	isSecondNum = True
	isAdd = True
	isDivide = False
	isSubtract = False
	isMultiply = False

def multiplyNum():
	global firstNumVar
	global secondNumVar
	global isAdd
	global isDivide
	global isSubtract
	global isMultiply
	firstNumVar = outputBox.get()
	outputBox.delete(0, tk.END)
	isSecondNum = True
	isMultiply = True
	isAdd = False
	isDivide = False
	isSubtract = False

def divideNum():
	global firstNumVar
	global secondNumVar
	global isAdd
	global isDivide
	global isSubtract
	global isMultiply
	firstNumVar = outputBox.get()
	outputBox.delete(0, tk.END)
	isSecondNum = True
	isMultiply = False
	isAdd = False
	isDivide = True
	isSubtract = False

def subtractNum():
	global firstNumVar
	global secondNumVar
	global isAdd
	global isDivide
	global isSubtract
	global isMultiply
	firstNumVar = outputBox.get()
	outputBox.delete(0, tk.END)
	isSecondNum = True
	isMultiply = False
	isAdd = False
	isDivide = False
	isSubtract = True

def calculate():
	global firstNumVar
	global secondNumVar
	global afterAnswer
	secondNumVar = outputBox.get()
	outputBox.delete(0, tk.END)
	if isAdd:
		firstNumVar = float(firstNumVar)
		secondNumVar = float(secondNumVar)
		answer = firstNumVar + secondNumVar
		outputBox.insert(0, answer)
		afterAnswer = True
	if isMultiply:
		firstNumVar = float(firstNumVar)
		secondNumVar = float(secondNumVar)
		answer = firstNumVar * secondNumVar
		outputBox.insert(0, answer)
		afterAnswer = True
	if isDivide:
		firstNumVar = float(firstNumVar)
		secondNumVar = float(secondNumVar)
		answer = firstNumVar / secondNumVar
		outputBox.insert(0, answer)
		afterAnswer = True
	if isSubtract:
		firstNumVar = float(firstNumVar)
		secondNumVar = float(secondNumVar)
		answer = firstNumVar - secondNumVar
		outputBox.insert(0, answer)
		afterAnswer = True


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

buttonDivide = tk.Button(root, width=15, height=6, text = "/", command = divideNum)
buttonDivide.grid(row=3, column=4)

buttonMultiply = tk.Button(root, width=15, height=6, text = "x", command = multiplyNum)
buttonMultiply.grid(row=4, column=4)

buttonSubtract = tk.Button(root, width=15, height=6, text = "-", command = subtractNum)
buttonSubtract.grid(row=5, column=4)

buttonAdd = tk.Button(root, width=15, height=6, text = "+", command = addNum)
buttonAdd.grid(row=6, column=4)

buttonBug = tk.Button(root, width=15, height=6, text = "Report \na bug", command = reportIssue)
buttonBug.grid(row=6, column=1)

buttonClear = tk.Button(root, width=30, height=6, text="Clear", command = clearAll)
buttonClear.grid(row=6, column=2)

root.mainloop()