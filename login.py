from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Password Tidak Boleh Kosong')
    elif usernameEntry.get()=='Ikhsan'and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','welcome')
    elif usernameEntry.get()=='admin'and passwordEntry.get()=='admin':
        messagebox.showinfo('Success','welcome')
        window.destroy()
        import sms
    else:
        messagebox.showerror('error','Tolong masukan password yang benar')
window = Tk()

window.geometry('1280x700+0+0')
window.title('Sistem management siswa')
window.geometry('1280x700+0+0')
window.resizable(False,False)
window.wm_iconbitmap('logotkinter.ico')

backgroundImage=ImageTk.PhotoImage(file = 'bg.jpg')

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

loginFrame=Frame(window,bg='white')
loginFrame.place(x=400,y=150)

logoImage=PhotoImage(file='logo.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)
usernameImage=PhotoImage(file='user.png')
usernameLabel =Label (loginFrame,image=usernameImage,text='Username',compound=LEFT
,font=('times new roman',20,'bold'),bg='white')

usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

logoImage=PhotoImage(file='logo.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)
passwordImage=PhotoImage(file='password.png')
passwordLabel =Label (loginFrame,image=passwordImage,text='password',compound=LEFT
,font=('times new roman',20,'bold'),bg='white')

passwordLabel.grid(row=2,column=0,pady=10,padx=20)

passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

LoginButton=Button(loginFrame,text='Login',font=('times new roman',20,'bold'),width=15
,fg='white',bg='cornflowerblue',activebackground='cornflowerblue',activeforeground='black',cursor='hand2',command=login)
LoginButton.grid(row=3,column=1,pady=10)


window.mainloop()