from tkinter import *
import time
import ttkthemes 
from tkinter import ttk,messagebox
import pymysql

#Def Fuction untuk Functional Part pada button
def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
       root.destroy()
    else:
       pass

def toplevel_data(title,button_text,command):
    global idEntry,NamaEntry,NomerEntry,emailEntry,alamatEntry,JKEntry,DOBEntry,screen
    screen=Toplevel()
    screen.title(title)
    screen.resizable(False,False)
    screen.grab_set
    idLabel=Label(screen,text='id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=15)

    NamaLabel=Label(screen,text='Nama',font=('times new roman',20,'bold'))
    NamaLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    NamaEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    NamaEntry.grid(row=1,column=1,pady=15,padx=15)

    NomerLabel=Label(screen,text='Nomer HP',font=('times new roman',20,'bold'))
    NomerLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    NomerEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    NomerEntry.grid(row=2,column=1,pady=15,padx=15)

    emailLabel=Label(screen,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,pady=15,padx=15)
    
    alamatLabel=Label(screen,text='Alamat',font=('times new roman',20,'bold'))
    alamatLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    alamatEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    alamatEntry.grid(row=5,column=1,pady=15,padx=15)
   
    JKLabel=Label(screen,text='Jenis Kelamin',font=('times new roman',20,'bold'))
    JKLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    JKEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    JKEntry.grid(row=4,column=1,pady=15,padx=15)

    DOBLabel=Label(screen,text='D.O.B',font=('times new roman',20,'bold'))
    DOBLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    DOBEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    DOBEntry.grid(row=6,column=1,pady=15,padx=15)

    button=ttk.Button(screen,text=button_text,command=command)
    button.grid(row=7,columnspan=2,pady=15)
    
    if title =='Update Student':
        indexing=studentTable.focus()
        content=studentTable.item(indexing)
        listdata=content['values']
        idEntry.insert(0,listdata[0])
        NamaEntry.insert(0,listdata[1])
        NomerEntry.insert(0,listdata[2])
        emailEntry.insert(0,listdata[3])
        alamatEntry.insert(0,listdata[4])
        JKEntry.insert(0,listdata[5])
        DOBEntry.insert(0,listdata[6])


def update_data():
    query='Update student set Nama=%s,Nomer=%s,email=%s,Alamat=%s,Jenis_kelamin=%s,dob=%s,date=%s,time=%s where id=%s'
    mycursor.execute(query,(NamaEntry.get(),NomerEntry.get(),emailEntry.get(),alamatEntry.get(),
    JKEntry.get(),DOBEntry.get(),date,cureenttime,idEntry.get()))

    con.commit()
    messagebox.showinfo('succes',f'id{idEntry.get()} berhasil diubah',parent=screen)
    screen.destroy()
    show_student()
    

def show_student():
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)

def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'This {content_id} is deleted succesfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)



def search_data():
      query='select *from student where id=%s or Nama=%s or Nomer=%s or email=%s or Alamat=%s or jenis_kelamin=%s or dob=%s'
      mycursor.execute(query,(idEntry.get(),NamaEntry.get(),NomerEntry.get(),emailEntry.get(),alamatEntry.get(),JKEntry.get(),DOBEntry.get()))
      studentTable.delete(*studentTable.get_children())
      fetched_data=mycursor.fetchall()
      for data in fetched_data:
          studentTable.insert('',END,values=data)


    

def add_data():
  if idEntry.get()=='' or NamaEntry.get()==''or NomerEntry.get()==''or emailEntry.get()=='' or JKEntry.get()==''or alamatEntry.get()=='' or DOBEntry.get()=='':
      messagebox.showerror('error','all feilds are requiered',parent=screen)

  else:
      try:
        query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        mycursor.execute(query,(idEntry.get(),NamaEntry.get(),NomerEntry.get(),emailEntry.get(),JKEntry.get(),alamatEntry.get(),DOBEntry.get(),
                        date,cureenttime))
        con.commit()
        result=messagebox.askyesno('Confirm','Data added succes .Do you want to clean the form?',parent=screen)
        if result:
            idEntry.delete(0,END)
            NamaEntry.delete(0,END)
            NomerEntry.delete(0,END)
            emailEntry.delete(0,END)
            alamatEntry.delete(0,END)
            JKEntry.delete(0,END)
            DOBEntry.delete(0,END)
        else:
            pass
      except:
          messagebox.showerror('error','id cannot be repeated',parent=screen)
          return



      query='select *from student'
      mycursor.execute(query)
      fetched_data=mycursor.fetchall()
      studentTable.delete(*studentTable.get_children())
      for data in fetched_data:
          studentTable.insert('',END,values=data)

#Membuat dan menghubungkan database
def connect_database():
    def connect():
      global mycursor,con
      try:
        con=pymysql.connect(host=hostEntry.get(),user=usernameEntry.get(),password=passwordEntry.get())
        mycursor=con.cursor()
        messagebox.showinfo('Succes','Database Connection succesfull',parent=connectWindow)
      except:
        messagebox.showerror('error','invalid Details',parent=connectWindow)
        return
      try:
        query='create database studentmanagementsystem'
        mycursor.execute(query)
        query='use studentmanagementsystem'
        mycursor.execute(query)
        query='create table student(id int not null primary key, Nama varchar (30),Nomer varchar(30),email varchar(30),'\
              'Alamat varchar(100),Jenis_kelamin varchar(20),dob varchar(20),date varchar(50), time varchar(50)) '
        mycursor.execute(query)
      except:
        query='use studentmanagementsystem'
        mycursor.execute(query)
      messagebox.showinfo('Succes','Database Connection succesfull',parent=connectWindow)
      connectWindow.destroy()
      addstudentButton.config(state=NORMAL)
      searchstudentButton.config(state=NORMAL)
      updatestudentButton.config(state=NORMAL)
      showstudentButton.config(state=NORMAL)
      exportstudentButton.config(state=NORMAL)
      DeletestudentButton.config(state=NORMAL)
      

    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

#
    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel=Label(connectWindow,text='User Name',font=('arial',20,'bold'))
    usernameLabel.grid(row=1,column=0)

    usernameEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    usernameEntry.grid(row=1,column=1,padx=40,pady=20)

    passwordLabel=Label(connectWindow,text='Password',font=('arial',20,'bold'))
    passwordLabel.grid(row=2,column=0)

    passwordEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)




count=0
text=''
def slider():
    global text,count
    # if count==len(s):
    #     count=0
    #     text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)

def clock():
    global date,cureenttime
    date=time.strftime('%d/%m/%Y')
    cureenttime= time.strftime('%H:%H:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {cureenttime}')
    datetimeLabel.after(1000,clock)

#GUI Part
root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')
root.wm_iconbitmap('logotkinter.ico')
root.geometry('1174x680+0+0')
root.resizable(0,0)
root.title('Sistem Managemen Siswa')


datetimeLabel=Label(root,text='hello',font=('Times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()

s='Sistem management siswa' #s[count]=t when count is 1
sliderLabel=Label(root,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()

connectButton=ttk.Button(root,text='Connect database',command=connect_database)
connectButton.place(x=980,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image = PhotoImage(file='students.png')
logo_Label = Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=lambda:toplevel_data('Add Student','Add',add_data))
addstudentButton.grid(row=1,column=0,pady=20) 

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=lambda:toplevel_data('Search Student','Search',search_data))
searchstudentButton.grid(row=2,column=0,pady=20) 

DeletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
DeletestudentButton.grid(row=3,column=0,pady=20) 

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=lambda:toplevel_data('Update Student','Update',update_data))
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton=ttk.Button(leftFrame,text='Export Student',width=25,state=DISABLED)
exportstudentButton.grid(row=6,column=0,pady=20)

exitstudentButton=ttk.Button(leftFrame,text='EXIT',width=25,command=iexit)
exitstudentButton.grid(row=7,column=0,pady=20) 

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollbarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,column=('id','Nama','Nomer HP','Email','Jenis kelamin',
                            'D.0.B','Added Date', 'Added Time'),
                            xscrollcommand=scrollbarX.set,yscrollcommand=scrollbarY.set)

scrollbarX.config(command=studentTable.xview)
scrollbarY.config(command=studentTable.yview)                         

scrollbarX.pack(side=BOTTOM,fill=X)
scrollbarY.pack(side=RIGHT,fill=Y)
studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('id',text='id')
studentTable.heading('Nama',text='Nama')
studentTable.heading('Nomer HP',text='Nomer HP')
studentTable.heading('Email',text='Email')
studentTable.heading('Jenis kelamin',text='Jenis kelamin')
studentTable.heading('D.0.B',text='D.0.B')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

studentTable.config(show='headings')
root.mainloop()