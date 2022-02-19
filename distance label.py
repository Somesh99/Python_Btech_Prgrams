from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
lbl = Label(window)
lbl.grid(column=1, row=0)
def clicked():
    lbl.configure(text="240 km",bg='orange',fg='black')
btn = Button(window, text="distance", command=clicked)
btn.grid(column=0, row=0)
window.mainloop()
