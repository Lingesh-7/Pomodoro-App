from tkinter import *
import time


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "courier"
WORK_MIN = 1  
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    win.after_cancel(timer)
    
    camva.itemconfig(timertxt,text="00:00")
    la1.config(text="TIMER")
    la2.config(text="")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startimer():
    global reps
    reps+=1
    works=WORK_MIN*60
    shortsec=SHORT_BREAK_MIN*60
    longsec=LONG_BREAK_MIN*60

    if reps==1 or reps==3 or reps==5 or reps==7:
        #work-green
        la1.config(text="Work")
        countdown(works)
    elif reps==8:
        #break
        la1.config(text="Break",fg=RED)
        countdown(longsec)
    elif reps==2 or reps==4 or reps==6:
        #pink
        la1.config(text="Break",fg=PINK)
        countdown(shortsec)

    # countdown(1*10)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(c):
    cm=c//60
    cs=c%60
    #Dynamic Typing
    if cs<10:
        cs=f"0{cs}"
        
    # if cm==0:
    #     cm="00"

    camva.itemconfig(timertxt,text=f"{cm}:{cs}")
    if c>0:
        global timer
        timer=win.after(1000,countdown,c-1)
    
    else:
        startimer()
        marks=""
        for i in range(reps//2):
            marks+="✔️"
        la2.config(text=marks)





# ---------------------------- UI SETUP ------------------------------- #


win =Tk()
win.title("POMODORO APP")
win.config(padx=100,pady=50,bg=YELLOW)
# win.after(1000)


la1=Label(text="TIMER",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"bold"))
la1.grid(column=1,row=0)

camva=Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
img=PhotoImage(file=r"C:\Users\linge\Desktop\python 100 days\projects\pr-28\tomato.png")
camva.create_image(100,112,image=img)
timertxt=camva.create_text(103,130,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
camva.grid(column=1,row=1)
# 
# 



but1=Button(text='Start',bg=YELLOW,font=(FONT_NAME,10,"bold"),command=startimer)
# but1.place(x=-60,y=270)
but1.grid(column=0,row=2)

la2=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,15,"bold"),highlightthickness=0)
# la2.pack()
la2.grid(column=1,row=3)

but2=Button(text='Reset',bg=YELLOW,font=(FONT_NAME,10,"bold"),highlightthickness=0,command=reset_timer)
# but2.place(x=210,y=270)
but2.grid(column=2,row=2)







win.mainloop()