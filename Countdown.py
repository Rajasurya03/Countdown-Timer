#Tkinter is the standard GUI library for Python

from tkinter import *
from playsound import playsound
import time

root=Tk()
root.title("Timer")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(False,False)

#Heading
heading=Label(root,text="Timer",font="arial 30 bold",bg="#000",fg="#ea3548")
heading.pack(pady=10)

#Clock
Label(root,font=("aril",15,"bold"),text="Current Time : ",bg="#000",fg="#fff").place(x=45,y=70)

def clock():
    clock_time=time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000,clock)

current_time=Label(root,font=("aril",15,"bold"),text="",fg="#000",bg="#fff")
current_time.place(x=190,y=70)
clock()

#Timer
hrs=StringVar()
Entry(root,textvariable=hrs,width=2,font="arial 50",bg="#000",fg="#fff",bd=0).place(x=30,y=155)
hrs.set("00")

mins=StringVar()
Entry(root,textvariable=mins,width=2,font="arial 50",bg="#000",fg="#fff",bd=0).place(x=150,y=155)
mins.set("00")

sec=StringVar()
Entry(root,textvariable=sec,width=2,font="arial 50",bg="#000",fg="#fff",bd=0).place(x=270,y=155)
sec.set("00")

#Labels
Label(root,text="hours",font="arial 12",bg="#000",fg="#fff").place(x=105,y=200)
Label(root,text="min",font="arial 12",bg="#000",fg="#fff").place(x=225,y=200)
Label(root,text="sec",font="arial 12",bg="#000",fg="#fff").place(x=345,y=200)

#Function Call from Start button
def Timer():
    times=int(hrs.get())*3600+int(mins.get())*60+int(sec.get())
    while times>-1:
        minute, second=(times//60,times%60)
        hour=0
        if minute>60:
            hour,minute=(minute//60,minute%60)
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        if(times==0):
            playsound("Ringtone.mp3")
            sec.set("00")
            mins.set("00")
            hrs.set("00")
        times -=1

#Function call from Brush Teeth
def brush():
    hrs.set("00")
    mins.set("02")
    sec.set("00")

#Function call from Face Mask
def face():
    hrs.set("00")
    mins.set("15")
    sec.set("00")

#Function call from Stream Eggs
def egg():
    hrs.set("00")
    mins.set("10")
    sec.set("00")

#Button -> Start
button=Button(root,text="Start",bg="#ea3548",bd=0,fg="#fff",width=20,height=2,font="arial 10 bold",command=Timer)
button.pack(padx=5,pady=40,side=BOTTOM)

#Brush Teeth Timer
Img1=PhotoImage(file="Brush.png")
button1=Button(root,image=Img1,bg="#000",bd=0,command=brush)
button1.place(x=7,y=300)

#Face Mask Timer
Img2=PhotoImage(file="Face_Mask.png")
button2=Button(root,image=Img2,bg="#000",bd=0,command=face)
button2.place(x=137,y=300)

#Stream Eggs Timer
Img3=PhotoImage(file="Stream.png")
button3=Button(root,image=Img3,bg="#000",bd=0,command=egg)
button3.place(x=267,y=300)

root.mainloop()
