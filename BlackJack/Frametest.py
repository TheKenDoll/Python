from tkinter import *
from tkinter import ttk

root = Tk()
pic1 = PhotoImage(file = 'D:\\Python\\Programs\\BlackJack\\Cards\\cace.png')
pic2 = PhotoImage(file = 'D:\\Python\\Programs\\BlackJack\\Cards\\dace.png')
frame1=ttk.Frame(root)
frame1.config(relief=RIDGE)
frame1.place(x=100, y=0)
label1 = Label(frame1, image=pic1)
label1.pack()
frame2=ttk.Frame(root)
frame2.config(height=400, width=300, relief=RIDGE)
frame2.place(x=200, y=0)#use place to over lap it the last to exucute is the last placed
label2 = Label(frame2, image=pic2)
label2.pack()

