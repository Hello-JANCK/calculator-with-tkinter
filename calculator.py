from tkinter import *
from tkinter import ttk
root = Tk()
root.configure(bg="#212121")
root.title("CALCULATOR")
root.iconbitmap('C:/Users/Bhanu Pratap Singh/Downloads/ishu.ico')
# def myfont():
	# font(size=18)
# root.geometry("500x500")
e = ttk.Entry(root, width=50)
e.grid(row=0, column=0, columnspan=3, padx=20, pady=20)
# e.insert(0, "Enter your name: ")


def add_button(number):
	
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))


def clear_num():
	e.delete(0, END)


def add_num():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = float(first_number)
	e.delete(0, END)


def equal_button():
	second_number = e.get()
	e.delete(0, END)
	
	if math == "addition":
		e.insert(0, f_num + float(second_number))
	if math == "subtraction":
		e.insert(0, f_num - float(second_number))
	if math == "multiplication":
		e.insert(0, f_num * float(second_number))
	if math == "division":
		e.insert(0, f_num / float(second_number))


def subtract_num():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = float(first_number)
	e.delete(0, END)


def multiply_num():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = float(first_number)
	e.delete(0, END)
def divide_num():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = float(first_number)
	e.delete(0, END)



# DEFINE BUTTONS
button_1 = Button(root, text = "1", padx=50 , pady=20, command=lambda: add_button(1), bg="#212121", fg="white", activebackground="#039BE5")
button_2 = Button(root, text = "2", padx=50 , pady=20, command=lambda: add_button(2), bg="#212121", fg="white", activebackground="#039BE5")
button_3 = Button(root, text = "3", padx=50 , pady=20, command=lambda: add_button(3), bg="#212121", fg="white", activebackground="#039BE5")
button_4 = Button(root, text = "4", padx=50 , pady=20, command=lambda: add_button(4), bg="#212121", fg="white", activebackground="#039BE5")
button_5 = Button(root, text = "5", padx=50 , pady=20, command=lambda: add_button(5), bg="#212121", fg="white", activebackground="#039BE5")
button_6 = Button(root, text = "6", padx=50 , pady=20, command=lambda: add_button(6), bg="#212121", fg="white", activebackground="#039BE5")
button_7 = Button(root, text = "7", padx=50 , pady=20, command=lambda: add_button(7), bg="#212121", fg="white", activebackground="#039BE5")
button_8 = Button(root, text = "8", padx=50 , pady=20, command=lambda: add_button(8), bg="#212121", fg="white", activebackground="#039BE5")
button_9 = Button(root, text = "9", padx=50 , pady=20, command=lambda: add_button(9), bg="#212121", fg="white", activebackground="#039BE5")
button_0 = Button(root, text = "0", padx=50 , pady=20, command=lambda: add_button(0), bg="#212121", fg="white", activebackground="#039BE5")

button_decimal = Button(root, text = ".", padx=52 , pady=20, command=lambda: add_button("."), bg="#212121", fg="white", activebackground="#039BE5")

button_add = Button(root, text = "+", padx=50 , pady=20, command=add_num, bg="#212121", fg="white", activebackground="#039BE5")
button_equal = Button(root, text = "=", padx=50 , pady=20, command=equal_button, bg="#212121", fg="white", activebackground="#039BE5")
button_clear = Button(root, text = "C", padx=50 , pady=20, command=clear_num, bg="#4CAF50", fg="white", activebackground="#039BE5")

button_subtract = Button(root, text = "-", padx=50 , pady=20, command=subtract_num, bg="#212121", fg="white", activebackground="#039BE5")
button_multiply = Button(root, text = "*", padx=51 , pady=20, command=multiply_num, bg="#212121", fg="white", activebackground="#039BE5")
button_divide = Button(root, text = "/", padx=50 , pady=20, command=divide_num, bg="#212121", fg="white", activebackground="#039BE5")
button_quit = Button(root, text="CLOSE", padx=40 , pady=20, command=root.quit, bg="#b71c1c", fg="white", activebackground="#039BE5")




#  PUT THE BUTTONS ON THE SCREEN
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_clear.grid(row=6, column=0)
button_add.grid(row=4, column=1)
button_equal.grid(row=5, column=1)

button_subtract.grid(row=4, column=2)
button_multiply.grid(row=5, column=2)
button_divide.grid(row=5, column=0)
button_quit.grid(row=6, column=1)
button_decimal.grid(row=6, column=2)

root.mainloop()
