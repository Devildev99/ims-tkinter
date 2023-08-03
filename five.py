import tkinter as tk
from PIL import Image, ImageTk
import pymysql
from tkinter import *
from tkinter import ttk

def update(id):
    global frame1
    global table1
    global v1
    global frame2
    v1=str(v1.get())
    frame1.destroy()
    frame2.destroy()
    import six
    six.disp(v1,id)
    

def delete(id):
    global frame1
 
    global v1
    global frame2
    v1=str(v1.get())
    frame1.destroy()
    frame2.destroy()
    import seven
    seven.disp(v1,id)

'''def doubleclick(*args):
    global table1
    global frame1
    frame=Toplevel(frame1)
    frame.geometry('150x150')
    frame.title("Choose an Option")
    frame.grab_set()'''
def doubleclick(event):
    global table1
    global frame1
    global v1
    item = table1.selection()[0]
    #print("you clicked on",table1.item(item, "values")[0] )
    id=table1.item(item, "values")[0]
    global frame2
    frame2=tk.Tk () 
    btn1=Button(frame2,text="Update",fg="black",bg="yellow",font=("Arial",10,'bold'),command=lambda:update(id)).place(x=50,y=40,width=55,height=40)
    btn2=Button(frame2,text="Delete",fg="black",bg="Red",font=("Arial",10,'bold'),command=lambda:delete(id)).place(x=50,y=90,width=55,height=40)

    frame2.mainloop()
     
def logout():
    global frame1
    frame1.destroy()
 
    import two
    two.disp("successfully logout")

def addstudent(v1):
    v1=str(v1.get())
    global frame1
    frame1.destroy()
    import four
    four.disp(v1)
    


def disp(s1):
    global frame1
    global table1
    frame1=tk.Tk ()

    frame1.geometry ("600x600")
    frame1.config(bg="white")
    frame1.title("Add Student")
    global v1
    v1=tk.StringVar()
    v1.set(s1)
    v2=tk.StringVar()#name
    v3=tk.StringVar()#roll
    v4=tk.StringVar()#email
    v5=tk.StringVar()#phone


    tk.Label(text="Welcome",fg="brown",bg="white",bd=2,font=("Arial",12,'bold')).place(x=170,y=20)
    tk.Label(text="",fg="dark red",bg="white",bd=2,font=("Arial",12,'bold'),textvariable=v1).place(x=250,y=20)

    

    tk.Button(text="Log Out",fg="white",bg="blue",bd=2,font=("Arial",12),command=logout).place(x=250,y=540,width=100,height=25)
    table1 = ttk.Treeview(frame1)

    table1['columns'] = ('id', 'name','roll', 'email', 'phone')
    table1.column("#0", width=0,  stretch=NO)
    table1.column("id",anchor=CENTER, width=80)
    table1.column("name",anchor=CENTER,width=80)
    table1.column("roll",anchor=CENTER,width=80)

    table1.column("email",anchor=CENTER,width=80)
    table1.column("phone",anchor=CENTER,width=80)
    
    table1.heading("#0",text="",anchor=CENTER)
    table1.heading("id",text="Id",anchor=CENTER)
    table1.heading("name",text="Name",anchor=CENTER)
    table1.heading("roll",text="Roll",anchor=CENTER)

    table1.heading("email",text="Email",anchor=CENTER)
    table1.heading("phone",text="Phone",anchor=CENTER)
    
    try:
        conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="dba")
        cur=conn.cursor()
        q1="select * from `student`"
        res=cur.execute(q1)
        y=0
        for x in cur:
            table1.insert(parent='',index='end',iid=y,text='',values=x)
            y=y+1
            table1.bind("<Double-1>",doubleclick)
            table1.place(relx=0,rely=0.1,relwidth=1,relheight=0.65)
    except:
        pass

    
    
    
    
    B2=tk.Button(frame1,text="Add Student",fg="white",bg="red",bd=2,font=("Arial",12),command=lambda:addstudent(v1)).place(x=250,y=480,width=100,height=25)

    
    frame1.mainloop()

#disp("Dev")   
