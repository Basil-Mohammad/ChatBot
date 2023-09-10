from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def login_user():
    if adminnameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')

    else:
        try:
            con=pymysql.connect(host='localhost', user='root', password='0000')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query = 'use admindata'
        mycursor.execute(query)
        query='select * from admintable where adminname=%s and password=%s'
        mycursor.execute(query,(adminnameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row== None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            #messagebox.showinfo('Welcome','Login is sucessful')
            admin_window.destroy()
            import Note


def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def admin_enter(event):
    if adminnameEntry.get()=='Admin Name':
        adminnameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)


#GUI Part
admin_window = Tk()
admin_window.geometry('990x660+50+50')
admin_window.resizable(0,0)
admin_window.title('Admin Page')
#bgImage=ImageTk.PhotoImage(file='bgv1.jpg')
bgImage=ImageTk.PhotoImage(file='addpcs.jpg')

bgLabel=Label(admin_window, image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(admin_window, text='ADMIN LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white', fg='firebrick1')
heading.place(x=605, y=120)

adminnameEntry=Entry(admin_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
adminnameEntry.place(x=580, y=200)
adminnameEntry.insert(0, 'Admin Name')

adminnameEntry.bind('<FocusIn>', admin_enter)

frame1=Frame(admin_window, width=250, height=2, bg='firebrick1')
frame1.place(x=580,y=222)

passwordEntry=Entry(admin_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', password_enter)

frame2=Frame(admin_window, width=250, height=2, bg='firebrick1')
frame2.place(x=580,y=282)
openeye=PhotoImage(file='openeye.png')
eyeButton=Button(admin_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=800,y=255)

#forgetButton=Button(admin_window, text='Forgot Password', bd=0, bg='white', activebackground='white', cursor='hand2', font=('Microsoft Yahei UI Light', 9, 'bold'), fg='firebrick1', activeforeground='firebrick1', command=forget_pass)
#forgetButton.place(x=715,y=295)

loginButton=Button(admin_window,text='Login', font=('Open Sans',16,'bold'), fg='white', bg='firebrick1', activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0,width=19, command=login_user)
loginButton.place(x=578,y=350)



admin_window.mainloop()