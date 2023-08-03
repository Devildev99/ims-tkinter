import tkinter as tk
import pymysql as py
from tkinter import messagebox

def back(v1):
    global frame
    v1=str(v1.get())
    frame.destroy()
    import three
    three.disp(v1)

def allstudent(v1):
    global frame
    v1=str(v1.get())
    frame.destroy()
    import five
    five.disp(v1)    

def logout():
    global frame
    frame.destroy()
    #print("successfully logout")
    import two
    two.disp("successfully logout")


def submit(v2,v3,v4,v5):
    global frame
    try:
        nm=str(v2.get())
        roll=str(v3.get())
        em=str(v4.get())
        ph=str(v5.get())
        conn=py.connect(host="localhost",user="root",port=3306,passwd="",db="dba")
        cur=conn.cursor()
        res=cur.execute("INSERT INTO `student`(`name`, `roll`, `email`, `phone`) VALUES ('"+nm+"','"+roll+"','"+em+"','"+ph+"')")
        if res:
            messagebox.showinfo("Inserted Successfully")
            conn.commit()
        else:
            messagebox.showinfo("Error Occured!")
            #conn.close()
    except:
        messagebox.showinfo("Connection Error!")
    finally:        
        conn.close()
    
def disp(s1):
    global frame
    frame=tk.Tk()
    frame.geometry("400x400")
    frame.resizable(False,False)
    frame.title("Profile")
    frame.config(bg="white")
    v1=tk.StringVar()
    
    v1.set(s1)
    v2=tk.StringVar()
    v3=tk.StringVar()
    v4=tk.StringVar()
    v5=tk.StringVar()
    tk.Label(text="Welcome",fg="brown",bg="white",bd=2,font=("Arial",12,'bold')).place(x=170,y=20)
    tk.Label(text="",fg="dark red",bg="white",bd=2,font=("Arial",12,'bold'),textvariable=v1).place(x=250,y=20)
    tk.Button( tk.Button(text="Log Out",fg="white",bg="blue",bd=2,font=("Arial",12),command=logout).place(x=250,y=350,width=100,height=25))
    tk.Button( tk.Button(text="Back",fg="white",bg="blue",bd=2,font=("Arial",12),command=lambda:back(v1)).place(x=50,y=350,width=100,height=25))
    tk.Button( tk.Button(text="Submit",fg="white",bg="orange",bd=2,font=("Arial",12),command=lambda:submit(v2,v3,v4,v5)).place(x=150,y=250,width=100,height=25))
    tk.Button( tk.Button(text="All Student",fg="white",bg="yellow",bd=2,font=("Arial",12),command=lambda:allstudent(v1)).place(x=150,y=300,width=100,height=25))
    tk.Label(frame,text="Name",fg="purple",bg="white",bd=2,font=("Arial",10,'bold')).place(x=150,y=50)
    tk.Label(frame,text="Roll",fg="purple",bg="white",bd=2,font=("Arial",10,'bold')).place(x=150,y=90)
    tk.Label(frame,text="Email",fg="purple",bg="white",bd=2,font=("Arial",10,'bold')).place(x=150,y=130)
    tk.Label(frame,text="Phone No",fg="purple",bg="white",bd=2,font=("Arial",10,'bold')).place(x=150,y=170)
    tk.Entry(frame,text="",fg="black",bg="white",bd=2,font=("Arial",10),textvariable=v2).place(x=140,y=70)
    tk.Entry(frame,text="",fg="black",bg="white",bd=2,font=("Arial",10),textvariable=v3).place(x=140,y=110)
    tk.Entry(frame,text="",fg="black",bg="white",bd=2,font=("Arial",10),textvariable=v4).place(x=140,y=150)
    tk.Entry(frame,text="",fg="black",bg="white",bd=2,font=("Arial",10),textvariable=v5).place(x=140,y=190)
    
    frame.mainloop()

#disp("Dev")    
