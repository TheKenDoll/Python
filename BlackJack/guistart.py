from tkinter import *
from tkinter import ttk
root = Tk()
card = 'sace' + '.png'
image = PhotoImage(file = 'D:\\Python\\Programs\\BlackJack\\Cards\\%s' % card)
#if the pixle rate of the image is too high it comes out way too big in the gui
#i changed the size to with of 500 pixles it still maybe a bit big
#change the pixle rate in the photo editor PIXLR just in broser you go to image/image size   to change the size of the image
label = Label(image=image)
label.pack()


