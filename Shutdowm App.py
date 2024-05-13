from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logged_out():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")


st=Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(background="blue")

r_button=Button(st,text="Restart",font=("Time New Roman",30,"bold")
                ,relief=RAISED,cursor="plus",command=restart)
r_button.place(x=135,y=70,height=45,width=200)
rt_button=Button(st,text="Restart Time",font=("Time New Roman",30,"bold"),
                 relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=105,y=170,height=45,width=250)
lg_button=Button(st,text="Logged Out",font=("Time New Roman",30,"bold"),
                 relief=RAISED,cursor="plus",command=logged_out)
lg_button.place(x=105,y=270,height=50,width=250)
st_button=Button(st,text="ShutDown",font=("Time New Roman",30,"bold"),
                 relief=RAISED,cursor="plus",command=shutdown)
st_button.place(x=105,y=370,height=47,width=250)


st.mainloop()