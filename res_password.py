from tkinter import *
from tkinter import messagebox
import pymysql
# from login import mail

def reset_pass():
    new_pass = reset.get()
    if new_pass=='':
        messagebox.showerror('Error', 'Enter a new password')
    else:
        try:
            email = mail.get()
            con = pymysql.connect(host='localhost', user='root', database='emp')
            cur = con.cursor()
            cur.execute('update emp1 set pass=%s,conf_pass=%s where email=%s', (new_pass, new_pass, email))
            row = cur.fetchone()
            con.close()
            root4.destroy()

        except Exception as e:
            messagebox.showerror('Error', f'Error: {e}')

root4=Tk()

root4.geometry('560x320+395+160')
root4.title('Reset Password')

passFrame=Frame(root4, width=560, height=320,bg='white')
passFrame.place(x=0, y=0)

maillabel=Label(passFrame, text='Email',font=('arial',22,'bold'),bg='white')
maillabel.place(x=240,y=30)
mail=Entry(passFrame,font=('arial',20),bg='white')
mail.place(x=130, y=80)

resetlabel=Label(passFrame, text='New Password',font=('arial',22,'bold'),bg='white')
resetlabel.place(x=180,y=140)
reset=Entry(passFrame,font=('arial',22),bg='white')
reset.place(x=130, y=190)

resetBt=Button(passFrame,text='Reset', bd=0, font=('times new roman',14,'bold'),bg='gold', borderwidth=5,relief='ridge',cursor='hand2',command=reset_pass)
resetBt.place(x=260,y=250)

root4.mainloop()