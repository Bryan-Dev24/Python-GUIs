from tkinter import *
window = Tk()
lbl = Label(window,text='Choose your favorite programming languages:')
frame = Frame(window)
python = Checkbutton(frame,text='Python')
java = Checkbutton (frame,text='Java')
js = Checkbutton (frame,text='JavaScript')
cpp = Checkbutton (frame,text='C++')

lbl.pack()
frame.pack()
python.pack()
java.pack()
js.pack()
cpp.pack()

window.mainloop()
    
