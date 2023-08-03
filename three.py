import pymysql
import tkinter as tk

def logout():
    global frame
    frame.destroy()
    #print("successfully logout")
    import two
    two.disp("successfully logout")

def addstudent(v1):
    v1=str(v1.get())
    #print(v1)
    global frame
    frame.destroy()
    import four
    four.disp(v1)
    ''' import addstudent
    addstudent.disp(v1)'''
    
def allstudent(v1):
    v1=str(v1.get())
    global frame
    frame.destroy()
    import five
    five.disp(v1)
    '''import allstudent
    allstudent.disp(v1)   '''

def disp(s1):
    global frame
    frame=tk.Tk()
    frame.geometry("400x400")
    frame.resizable(False,False)
    frame.title("Profile")
    frame.config(bg="white")
    v1=tk.StringVar()
    v1.set(s1)

    tk.Button(text="Log Out",fg="white",bg="blue",bd=2,font=("Arial",12),command=logout).place(x=250,y=350,width=100,height=25)
    tk.Label(text="Welcome",fg="brown",bg="white",bd=2,font=("Arial",12,'bold')).place(x=170,y=20)
    tk.Label(text="",fg="dark red",bg="white",bd=2,font=("Arial",12,'bold'),textvariable=v1).place(x=250,y=20)

    B2=tk.Button(frame,text="Add Student",fg="white",bg="red",bd=2,font=("Arial",12),command=lambda:addstudent(v1))
    B2.place(relx=0.20,rely=.50,relwidth=0.60,relheight=0.1)

    B3=tk.Button(frame,text="All Student",fg="white",bg="green",bd=2,font=("Arial",12),command=lambda:allstudent(v1))
    B3.place(relx=0.20,rely=.65,relwidth=0.60,relheight=0.1)
    frame.mainloop()
#disp("ram")    
