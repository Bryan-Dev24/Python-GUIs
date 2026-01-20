from tkinter import *
from PIL import ImageTk, Image
window = Tk()
name = Label(window,text='PythonX - Learn Python',bg='white',fg='Blue',font=('Serif',16))
img = Image.open('python.png')
logo = ImageTk.PhotoImage(img)
image = Label(window,image=logo)
frame = Frame(window)
username = Label(frame,text='Username',font=('Serif',12))
inputBox = Entry(frame)
button = Button(window,text='Lets Start')

name.pack()
image.pack()
frame.pack()
username.pack(side=LEFT)
inputBox.pack(side=RIGHT)
button.pack(side=BOTTOM)

window.mainloop()
