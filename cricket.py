from tkinter import font
from tkinter.constants import NW
import cv2
import tkinter
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import imutils
import time
from playsound import playsound


stream = cv2.VideoCapture("drsvideo.mp4")

flag = True
def play(speed):
    global flag
    print(f"You clicked on play.Speed is {speed}")
    
    
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
    
    
    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor = tkinter.NW)
    if flag:
        canvas.create_text(150,30,fill="white",font="Times 30 bold",text="Decision Pending")
    flag = not flag

def pending(decision):
    # Display decision pending image
    frame = cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image =frame
    canvas.create_image(0,0, image = frame, anchor = tkinter.NW)
    # wait for 1 sec
    time.sleep(1)

    # Display sponsor Image
    frame = cv2.cvtColor(cv2.imread("sponsor.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image =frame
    canvas.create_image(0,0, image = frame, anchor = tkinter.NW)

    # Wait for 1.5 sec
    time.sleep(2)

    # Display result
    if decision == 'out':
        decisionimg = "out.png"
    else:
        decisionimg = "not_out.png"
    frame = cv2.cvtColor(cv2.imread(decisionimg),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image =frame
    canvas.create_image(0,0, image = frame, anchor = tkinter.NW)



def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("You are Out")

def not_out():
    thread = threading.Thread(target=pending, args=("Not Out",))
    thread.daemon = 1
    thread.start()
    print("Player is Not Out")





# width and height main screen
SET_WIDTH = 800
SET_HEIGHT = 400

#tkinter gui starts here
window = tkinter.Tk()
window.title("UDIT BHASKAR- THIRD UMPIRE DRS SYSTEM")
canvas = tkinter.Canvas(window, width=SET_WIDTH,height=SET_HEIGHT)
cv_img = cv2.cvtColor(cv2.imread("welcome.png"),cv2.COLOR_BGR2RGB)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()


#buttons to control playback
btn = tkinter.Button(window,text="< <REWIND (Fast)",foreground="white", background="black", width=50,command = partial(play, -5))
btn.pack()
btn = tkinter.Button(window,text="<< REWIND (Slow)",foreground="white", background="black",width=50,command = partial(play, -2))
btn.pack()
btn = tkinter.Button(window,text="FORWARD >> (Fast)",foreground="white",background="black",width=50,command = partial(play, 5))
btn.pack()
btn = tkinter.Button(window,text="FORWARD >> (Slow)",foreground="white",background="black",width=50,command = partial(play, 1))
btn.pack()
btn = tkinter.Button(window,text="Out",width=50,foreground="white",background="red",command=out)
btn.pack()
btn = tkinter.Button(window,text="Not Out",foreground="white", background="green",width=50, command= not_out)
btn.pack()

window.mainloop()
