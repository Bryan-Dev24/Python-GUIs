from tkinter import *
window = Tk()
frame = Frame(window)
lbl = Label(frame,text='Inside the frame')
btn = Button(frame, text='Inside the frame')
frame.pack()
lbl.pack(side=TOP)
btn.pack(side=BOTTOM)
window.mainloop()
