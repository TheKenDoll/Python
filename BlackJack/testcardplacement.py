from tkinter import *
from tkinter import ttk

root = Tk()
pic1 = PhotoImage(file = 'D:\\Python\\Programs\\BlackJack\\Cards\\cace.png')
pic2 = PhotoImage(file = 'D:\\Python\\Programs\\BlackJack\\Cards\\dace.png')

label1 = Label(image=pic1)
label1.place(x=100, y=0)

#use place to over lap it the last to exucute is the last placed
label2 = Label(image=pic2)
label2.place(x=200, y=0)

