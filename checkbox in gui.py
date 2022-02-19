from tkinter import*
top=Tk()
var1=IntVar()
var2=IntVar()
C1=Checkbutton(top,text="music",variable=var1,onvalue=1,offvalue=0)
C2=Checkbutton(top,text="video",variable=var2,onvalue=1,offvalue=0)
C1.grid(row=0,column=0)
C2.grid(row=0,column=1)

top.mainloop()
