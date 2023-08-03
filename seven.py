import tkinter as tk
from PIL import Image, ImageTk
import pymysql

def logout():
    global frame1
    frame1.destroy()
    #print("successfully logout")
    import two
    two.disp("successfully logout")
def delete(id,v2,v3,v4,v5):
    global frame1
    global v1
    v1=str(v1.get())
    nm=str(v2.get())
    roll=str(v3.get())
    em=str(v4.get())
    ph=str(v5.get())
    #frame1.destroy()
    conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="dba")
    try:
        cur=conn.cursor()
        q1="DELETE FROM `student` where `id`='"+id+"'"
        res=cur.execute(q1)
        if(res):
            conn.commit()
            conn.close()
            frame1.destroy()
            import five
            five.disp(v1)
    
    except:
        conn.close()
    
def back():
    global frame1
    global v1
    v1=str(v1.get())
    frame1.destroy()
    import five
    five.disp(v1) 
       
def allstudent(v1):
    v1=str(v1.get())
    global frame1
    frame1.destroy()
    import five
    five.disp(v1)
    


def disp(s1,id):
    global frame1
    frame1=tk.Tk ()

    frame1.geometry ("400x400")
    frame1.config(bg="white")
    frame1.title("Delete Student")
    global v1
    v1=tk.StringVar()
    v1.set(s1)
    v2=tk.StringVar()#name
    v3=tk.StringVar()#email
    v4=tk.StringVar()#phone
    v5=tk.StringVar()#msg
    id=str(id)
    try:
        conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="dba")
        cur=conn.cursor()
        q1="select * from `student` where `id`='"+id+"'"
        res=cur.execute(q1)
        for x in cur:
            v2.set(x[1])
            v3.set(x[2])
            v4.set(x[3])
            v5.set(x[4])
    except:
        pass
    tk.Label(text="Welcome",fg="brown",bg="white",bd=2,font=("Arial",12,'bold')).place(x=170,y=20)
    tk.Label(text="",fg="dark red",bg="white",bd=2,font=("Arial",12,'bold'),textvariable=v1).place(x=250,y=20)
    tk.Button( tk.Button(text="Log Out",fg="white",bg="blue",bd=2,font=("Arial",12),command=logout).place(x=250,y=350,width=100,height=25))
    tk.Button( tk.Button(text="Back",fg="white",bg="blue",bd=2,font=("Arial",12),command=back).place(x=50,y=350,width=100,height=25))
    tk.Button( tk.Button(text="Delete",fg="white",bg="red",bd=2,font=("Arial",12),command=lambda:delete(id,v2,v3,v4,v5)).place(x=150,y=250,width=100,height=25))
    tk.Button( tk.Button(text="All Student",fg="white",bg="yellow",bd=2,font=("Arial",12),command=lambda:allstudent(v1)).place(x=150,y=300,width=100,height=25))
    tk.Label(frame1,text="Name",fg="purple",bg="white",bd=2,font=("Arial",10,'bold')).place(x=150,y=50)
    tk.Label(frame1,text="Roll",fg="purple",bg="white",bd=2,font=("Arial",10,'bold')).place(x=150,y=90)
    tk.Label(frame1,text="Email",fg="purple",bg="white",bd=2,font=("Arial",10,'bold')).place(x=150,y=130)
    tk.Label(frame1,text="Phone No",fg="purple",bg="white",bd=2,font=("Arial",10,'bold')).place(x=150,y=170)
    tk.Entry(frame1,text="",fg="black",bg="white",bd=2,font=("Arial",10),textvariable=v2).place(x=140,y=70)
    tk.Entry(frame1,text="",fg="black",bg="white",bd=2,font=("Arial",10),textvariable=v3).place(x=140,y=110)
    tk.Entry(frame1,text="",fg="black",bg="white",bd=2,font=("Arial",10),textvariable=v4).place(x=140,y=150)
    tk.Entry(frame1,text="",fg="black",bg="white",bd=2,font=("Arial",10),textvariable=v5).place(x=140,y=190)
    
    
    frame1.mainloop()
#disp("Dev",4)
