from tkinter import *  
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from math import *



# (sqrt(x)-sin(x))/log2(x)

def info():
	text = 'Эта программа строит график для функций содержаших ТОЛЬКО одну переменную x.\n Область значения введенная пользователем должна соответсвовать области значения функции.\nПоддерживаются:	\n 	- все стандартные функции библиотеки math.\nВозведение в степень производится оператором ** .	\n+ - * / не изменны.'
	messagebox.showinfo('Примечание', text)

def closeWindow():
	window.quit()

def constructFunc():
	try:
		
		func = funcL.get()
		y = lambda x: eval(func)
		y1 = np.vectorize(y)
		fig = plt.subplots()
		x = np.linspace(int(x1.get()), int(x2.get()),100)
		plt.plot(x, y1(x))
		plt.savefig('fun.png')
		bg = Image.open("fun.png")
		bg = ImageTk.PhotoImage(bg)
		lbl1 = Label(window, image=bg)
		lbl1.image = bg
		lbl1.place(x=30, y=10)

	except Exception as e:
		messagebox.showwarning('Ошибка', 'Неправильно заданная функция')



		

window = Tk()  
window.title("Построение графиков без смс и регистрации")
window.configure(background="#333")
window.geometry('700x620')

bg = Image.new("RGB", (640, 480), '#fff')
bg = ImageTk.PhotoImage(bg)
lbl1 = Label(window, image=bg)
lbl1.image = bg
lbl1.place(x=30, y=10) 

lbl = Label(window, text="Введите функцию:", font=("Arial Bold", 15), background="#333")  
lbl.place(x=40, y=500)

funcL = Entry(window, width=40) 
funcL.place(x=40, y=533)

btn = Button(window, text="Построить", command=constructFunc)  
btn.place(x=300, y=530)

btn1 = Button(window, text="Примечание", command=info)  
btn1.place(x=380, y=530)

closeBtn = Button(window, text="Выйти", command=closeWindow)  
closeBtn.place(x=480, y=530)

lbl = Label(window, text="x = [", font=("Arial Bold", 15), background="#333")  
lbl.place(x=40, y=560)

x1 = Entry(window, width=10) 
x1.place(x=100, y=565)

lbl = Label(window, text=";", font=("Arial Bold", 15), background="#333")  
lbl.place(x=170, y=560)

x2 = Entry(window, width=10) 
x2.place(x=190, y=565)

lbl = Label(window, text="]  <= область значения", font=("Arial Bold", 15), background="#333")  
lbl.place(x=270, y=560)

window.mainloop()
