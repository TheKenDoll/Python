from tkinter import *
from tkinter import ttk

root = Tk()
pic = PhotoImage(file = 'D:\\Python\\Programs\\BlackJack\\Cards\\cace.png')
#if the pixle rate of the image is too high it comes out way too big in the gui
#i changed the size to with of 500 pixles it still maybe a bit big
#change the pixle rate in the photo editor PIXLR just in broser you go to image/image size   to change the size of the image
frame1 = ttk.LabelFrame(root, height=500, width=300, text = 'Your Cards').pack(side=LEFT)
frame2 = ttk.Frame(root)
frame2.config(height = 400, width = 320,relief=RIDGE)
frame2.pack(side=RIGHT)
frame3 = ttk.Frame(root)
frame3.config(height = 100, width = 500,relief = RIDGE)
frame3.pack()

label = Label(frame1, image=pic).pack#puts the pic in the frame, but not in labeled frame???


