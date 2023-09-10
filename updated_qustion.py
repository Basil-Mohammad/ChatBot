from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql


def clear():
    qustionEntry.delete(0,END)
    answerEntry.delete(0,END)


def connect_database():
    if qustionEntry.get()=='' or answerEntry.get()=='' :
        messagebox.showerror('Error','All Fields Are Required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='0000')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return
        try:
           query='create database update_qustion'
           mycursor.execute(query)
           query='use update_qustion'
           mycursor.execute(query)
           query='create table answer(id int auto_increment primary key not null, user_qustion varchar(50), right_answer varchar(100))'
           mycursor.execute(query)
        except:
           mycursor.execute('use update_qustion')
        query = 'select * from answer where user_qustion=%s'
        mycursor.execute(query, (qustionEntry.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'The Qustion Already Exists ')
        else:
            query = 'insert into answer(user_qustion,right_answer) values(%s,%s)'
            mycursor.execute(query, (qustionEntry.get(), answerEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Thank you for helping us improve the level of service')
            clear()
            signup_window.destroy()
            import main

def login_page():
    update_window.destroy()
    import signin
update_window=Tk()

update_window.title('Update Page')
update_window.resizable(False,False)
#background=ImageTk.PhotoImage(file='a7.jpg')
background=ImageTk.PhotoImage(file='up2.jpg')


bgLabel=Label(update_window, image=background)
bgLabel.grid()

frame=Frame(update_window, bg='white')
frame.place(x=554,y=100)

heading=Label(frame, text='UPDATE THE ANSWER', font=('Microsoft Yahei UI Light', 18, 'bold'), bg='white', fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)


qustionLabel=Label(frame,text='The Qustion', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
qustionLabel.grid(row=1,column=0, sticky='w', padx=25, pady=(10,0))

qustionEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='firebrick1')
qustionEntry.grid(row=2,column=0,sticky='w', padx=25)

answerLabel=Label(frame,text='Write The Correct Answer', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
answerLabel.grid(row=7,column=0, sticky='w', padx=25, pady=(10,0))

answerEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='firebrick1')
answerEntry.grid(row=8,column=0,sticky='w', padx=25)

submitButton=Button(frame,text='Submit Answer', font=('Open Sans', 16, 'bold'),bd=0, bg='firebrick1', fg='white',activebackground='firebrick1',activeforeground='white', width=17, command=connect_database)
submitButton.grid(row=10,column=0, pady=10)

#submitButton=Button(frame,text='Submit Answer', font=('Open Sans', 16, 'bold'),bd=0, bg='firebrick1', fg='white',activebackground='firebrick1',activeforeground='white', width=17, command=connect_database)
#submitButton.grid(row=10,column=0, pady=10)

newaccountButton=Button(frame,text='Login', font=('Open Sans',9,'bold underline'), fg='blue', bg='white', activeforeground='blue', activebackground='white', cursor='hand2', bd=0, command=login_page)
#newaccountButton.place(x=400,y=450)
newaccountButton.grid(row=12,column=0, pady=10)

update_window.mainloop()
