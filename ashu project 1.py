from tkinter import*
root=Tk()
root.geometry("500x500")
root.configure(bg="red")

alabel=Label(root,text="WELCOME TO FITNESS CALCULATOR",fg="black",bg="red",font=('castellar','30'))
alabel.pack(side="top")
bcimage=PhotoImage(file="giphy (1).gif")


frame1=Frame(root)
frame1.pack()
Label(frame1,image=bcimage,width=250,height=250).pack(side=LEFT)
but1=Button(root,text="click here to proceed" ,font=('times','20'),height=2,width=30,bg="grey",fg="black").place(x=150,y=400)

root.mainloop()
