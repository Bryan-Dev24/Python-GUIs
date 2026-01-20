from tkinter import *
from PIL import ImageTk, Image

window = Tk()
name = Label(window,text='PythonX - Learn Python',bg='white',fg='Blue',font=('Serif',16))
img = Image.open('python.png')
logo = ImageTk.PhotoImage(img)
image = Label(window,image=logo)
name.pack()
image.pack()
window.mainloop()
