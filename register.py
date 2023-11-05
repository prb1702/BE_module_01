from tkinter import *
from tkinter import messagebox
import pymysql

# Functions

    root.destroy()
    import login


def clear():
    entryfirstname.delete(0,END)
    entrylastname.delete(0,END)
    entryemail.delete(0,END)
    entrypassword.delete(0,END)
    entryconfpass.delete(0,END)
    entryfam1.delete(0,END)
    entryfam2.delete(0,END)
    entrycontact.delete(0,END)

def register():
    if entryfirstname.get()=='' or entrylastname.get()=='' or entrycontact.get()=='' or entrypassword=='' or entryemail.get()=='' or entryconfpass=='':
        messagebox.showerror('Error', 'All Fields are required')
    elif entryfam1.get()=='' and entryfam2.get()=='':
        messagebox.showerror('Error', 'Contact Number of at least one friend is required')
    elif entrypassword.get()!=entryconfpass.get():
        messagebox.showerror('Error', 'Password Mismatched')
    elif check.get()==0:
        messagebox.showerror('Error', 'Please agree to our terms and conditions')
    else:
        try:
            con=pymysql.connect(host='localhost', user='root',database='emp')
            cur=con.cursor()
            cur.execute('select * from emp1 where email=%s',entryemail.get())
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror('Error', 'User Already Exists')
                clear()
            else:
                cur.execute('insert into emp1(f_name,l_name,contact,email,contact1,contact2,pass,conf_pass) values(%s,%s,%s,%s,%s,%s,%s,%s)',(entryfirstname.get(),entrylastname.get(),entrycontact.get(),entryemail.get(),entryfam1.get(),entryfam2.get(),entrypassword.get(),entryconfpass.get()))
                con.commit()
                con.close()

                messagebox.showerror('Success','Succesfully Registered')
                clear()
                login_window()

        except Exception as e:
            messagebox.showerror('error', f'Error due to {e}')



#GUI

root = Tk()
root.geometry('1350x710+10+10')
root.title('Registration Page')

bgImage=PhotoImage(file='bg3.png')
bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)

registerFrame=Frame(root, width=650, height=650)
registerFrame.place(x=350, y=30)

titleLabel=Label(registerFrame, text='Register',font=('arial', 22 ,'bold'),fg='gold')
titleLabel.place(x=260,y=20)

firstnameLabel=Label(registerFrame, text='First Name',font=('times new roman',18,'bold'), fg='gray20')
firstnameLabel.place(x=30, y=80)
entryfirstname=Entry(registerFrame, font=('times new roman', 16),bg='lightgray')
entryfirstname.place(x=30, y=115)

lastnameLabel=Label(registerFrame, text='Last Name',font=('times new roman', 18, 'bold'), fg='gray20')
lastnameLabel.place(x=370, y=80)
entrylastname=Entry(registerFrame, font=('times new roman', 16), bg='lightgray')
entrylastname.place(x=370, y=115)

contactLabel=Label(registerFrame, text='Contact',font=('times new roman',18,'bold'), fg='gray20')
contactLabel.place(x=30, y=200)
entrycontact=Entry(registerFrame, font=('times new roman', 16),bg='lightgray')
entrycontact.place(x=30, y=235)

emailLabel=Label(registerFrame, text='Email',font=('times new roman', 18, 'bold'), fg='gray20')
emailLabel.place(x=370, y=200)
entryemail=Entry(registerFrame, font=('times new roman', 16), bg='lightgray')
entryemail.place(x=370, y=235)

fam1Label=Label(registerFrame, text='Contact1 (Friend 1)',font=('times new roman',18,'bold'), fg='gray20')
fam1Label.place(x=30, y=320)
entryfam1=Entry(registerFrame, font=('times new roman', 16),bg='lightgray')
entryfam1.place(x=30, y=355)

fam2Label=Label(registerFrame, text='Contact2 (Friend 2)',font=('times new roman', 18, 'bold'), fg='gray20')
fam2Label.place(x=370, y=320)
entryfam2=Entry(registerFrame, font=('times new roman', 16), bg='lightgray')
entryfam2.place(x=370, y=355)

passwordLabel=Label(registerFrame, text='Password',font=('times new roman',18,'bold'), fg='gray20')
passwordLabel.place(x=30, y=440)
entrypassword=Entry(registerFrame, font=('times new roman', 16),bg='lightgray', show='*')
entrypassword.place(x=30, y=475)

confpassLabel=Label(registerFrame, text='Confirm Password',font=('times new roman', 18, 'bold'), fg='gray20')
confpassLabel.place(x=370, y=440)
entryconfpass=Entry(registerFrame, font=('times new roman', 16), bg='lightgray', show='*')
entryconfpass.place(x=370, y=475)

check=IntVar()
checkButton=Checkbutton(registerFrame, text='I Agree all the Terms & Conditions',onvalue=1,offvalue=0, variable=check, font=('times new roman',14,'bold'))
checkButton.place(x=30,y=530)


# buttonimage=PhotoImage(file='button.png')
registerButton=Button(registerFrame,text='Register',bd=0,font=('times new roman',14,'bold'),bg='gold',borderwidth=5,relief='ridge',cursor='hand2',command=register)
registerButton.place(x=400,y=590)

loginButton=Button(registerFrame,text='Login',bd=0,font=('times new roman',14,'bold'),bg='gold',borderwidth=5,relief='ridge',cursor='hand2',command=login_window)
loginButton.place(x=150,y=590)



root.mainloop()


