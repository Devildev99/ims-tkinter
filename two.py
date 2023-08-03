import pymysql as py
import tkinter as tk
import three

def login(v1,v2,v3):
    global frame
    s1=v1.get()
    s2=v2.get()
    if(s1=="" and s2==""):
        v3.set("Filled Properly")
    else:
        try:
            conn=py.connect(host="localhost",user="root",port=3306,passwd="",db="dba")
            cur=conn.cursor()
            res=cur.execute("select * from `admin` where `username`='"+s1+"' and `password`='"+s2+"'")
            if res:
                conn.commit()
                frame.destroy()
                three.disp(s1)
            else:
                v3.set("Wrong Information")
        except:
            v3.set("Something Wrong")
        finally:
            conn.close()

        
def disp(s1):
    global frame
    frame=tk.Tk()
    frame.geometry("400x400")
    frame.resizable(False,False)
    frame.title("Admin Login")
    frame.config(bg="white")
    v1=tk.StringVar()
    v2=tk.StringVar()
    v3=tk.StringVar()
    v3.set(s1)
    tk.Label(frame,text="User-id",fg="red",bg="white",font=('Arial',14,'bold')).place(x=170,y=50)
    tk.Label(frame,text="Password",fg="red",bg="white",font=('Arial',14,'bold')).place(x=170,y=150)

    tk.Button(frame,text="login",fg="white",bg="blue",font=('Arial',13,'bold'),command=lambda:login(v1,v2,v3)).place(x=270,y=340,width=63,height=30)
    tk.Entry(frame,text="",fg="black",bg="white",font=('Arial',13),bd=2,textvariable=v1).place(x=130,y=100,height=40)
    tk.Entry(frame,text="",show="*",fg="black",bg="white",font=('Arial',13),bd=2,textvariable=v2).place(x=130,y=200,height=40)
    tk.Label(frame,text="msg",fg="black",bg="white",font=('Arial',13,'bold'),textvariable=v3).place(x=130,y=280,height=30)
    frame.mainloop()
#disp()
