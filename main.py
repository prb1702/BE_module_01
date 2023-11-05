from tkinter import *


# root3=Tk()
#
# root3.geometry('1350x710+10+10')
# root3.title('Main Page')
#
# bgImage=PhotoImage(file='bg3.png')
# bgLabel=Label(root3,image=bgImage)
# bgLabel.place(x=0,y=0)
#
# loginFrame=Frame(root3, width=560, height=320,bg='white')
# loginFrame.place(x=395, y=148)
#



root3=Tk()

root3.geometry('1350x710+10+10')
root3.title('Main')

mainFrame=Frame(root3, width=560, height=320,bg='white')
mainFrame.place(x=395, y=148)

suc=Label(mainFrame, text='Successful',font=('arial',22,'bold'),bg='white')
suc.place(x=220,y=32)

root3.mainloop()