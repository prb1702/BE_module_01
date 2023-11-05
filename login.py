from tkinter import *
from tkinter import messagebox
import pymysql
import smtplib
import secrets
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Functions

def reset_pass():
    if mail.get()=='':
        messagebox.showerror('Error', 'Please enter the email address to reset your password')
    else:
        try:
            con=pymysql.connect(host='localhost', user='root', database='emp')
            cur=con.cursor()
            cur.execute('select * from emp1 where email=%s',mail.get())
            row=cur.fetchone()


            if row==None:
                messagebox.showerror('Error', 'Email address not found. Please enter a valid email address')
            else:
                # messagebox.showinfo('Status', 'Email found!')

                import res_password
                con.close()
                # sender_email = 'prajbhagat003@gmail.com'
                # sender_password = 'Praj1702*#'
                # msg = MIMEMultipart()
                # msg['From'] = sender_email
                # msg['To'] = mail.get()
                # msg['Subject'] = 'Password Reset Request'

        except Exception as e:
            messagebox.showerror('Error', f'Error: {e}')

def register_window():
    root2.destroy()
    import register
def signin():
    if mail.get()=='' or password.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',database='emp')
            cur=con.cursor()

            # login
            cur.execute('select * from emp1 where email=%s and pass=%s',(mail.get(),password.get()))
            row=cur.fetchone()

            if row==None:
                messagebox.showerror('Error','Invalid details')
            else:
                messagebox.showinfo('Success','Welcome')
                root2.destroy()
                import main
            con.close()
        except Exception as e:
            messagebox.showerror('Error',f'Error is due to {e}')

#
root2=Tk()

root2.geometry('1350x710+10+10')
root2.title('Login Page')

bgImage=PhotoImage(file='bg3.png')
bgLabel=Label(root2,image=bgImage)
bgLabel.place(x=0,y=0)

loginFrame=Frame(root2, width=560, height=320,bg='white')
loginFrame.place(x=395, y=148)

userimage=PhotoImage(file='user1.png')
userimageLabel=Label(loginFrame,image=userimage,bg='white')
userimageLabel.place(x=20, y=50)

maillabel=Label(loginFrame, text='Email',font=('arial',22,'bold'),bg='white')
maillabel.place(x=220,y=32)
mail=Entry(loginFrame,font=('arial',22),bg='white')
mail.place(x=220, y=70)

passwordlabel=Label(loginFrame,text='Password', font=('arial',22,'bold'),bg='white')
passwordlabel.place(x=220, y=120)
password=Entry(loginFrame, font=('arial',22),bg='white', show='*')
password.place(x=220, y=160)

registerBt=Button(loginFrame,text='Register New Account', bd=0, font=('times new roman',12), bg='white', cursor='hand2', activebackground='white', command=register_window)
registerBt.place(x=220,y=200)

forgetButton=Button(loginFrame, text='Forget Password?', font=('times new roman',12),bd=0,bg='white',activebackground='white',fg='red',activeforeground='red',cursor='hand2', command=reset_pass)
forgetButton.place(x=410,y=200)

loginBt=Button(loginFrame,text='Login', bd=0, font=('times new roman',14,'bold'),bg='gold', fg='white', borderwidth=5,relief='ridge',cursor='hand2',command=signin)
loginBt.place(x=220,y=240)


root2.mainloop()
