from tkinter import *
ws = Tk()
ws.title('PythonGudes')
ws.geometry('200x100')

def switchState():
    if cb1.get() == 1:
       disp_Lb.config(text='ON')
        
    elif cb1.get() == 0:
        disp_Lb.config(text='OFF')
    else:
        disp_Lb.config(text='error!')

switch_on = PhotoImage(width=50, height=50)
switch_off = PhotoImage(width=50, height=50)

switch_on.put(("green",), to=(0, 0, 23,23))
switch_off.put(("red",), to=(24, 0, 47, 23))
cb1 = IntVar()
Checkbutton(ws, image=switch_off, selectimage=switch_on, onvalue=1, offvalue=0, variable=cb1, indicatoron=False, command=switchState).pack(padx=20, pady=10)
disp_Lb = Label(ws)
disp_Lb.pack()
ws.mainloop()
