import tkinter
def test():
    import sys
    top=tkinter.Tk()
    top.title('date')
    da=Calendar(firstweekday=calendar.SUNDAY)
    da.pack(expand=1,fill='both')
    x=da.selection()
    print('x is :',x)
    if 'win' not in sys.platform:
        style=ttk.Style()
        style.theme_use('calm')
        top.mainloop()


if __name__ =='__main__':
    test()
