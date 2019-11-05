from tkinter import *
from tkinter import ttk
root=Tk()
style = ttk.Style()
photo1=PhotoImage(file='cat.gif')
style.theme_use('winnative')
root.title('Book Management System')
root.iconbitmap('books.ico') # use only.ico files
root.geometry("1600x800")

root.configure(background='powder blue',relief=RIDGE)
hf=Frame(root,bd=5,padx=20,pady=20,bg='blue',relief=RIDGE)
hf.pack(fill=X)
mf=Frame(root,bd=5,padx=20,pady=20,bg='powder blue')
mf.pack()

Label(hf,image=photo1,bg='black').grid(row=0,column=0,sticky=E)

headl=Label(hf,text='Book Management System',bg='blue',font=('',44),padx=15,pady=5).grid(row=0,column=4)
Label(hf,text='Learn explore teach... with Book-ray',bg='blue',fg='white',font=('',18)).grid(row=1,column=7)
infol=Label(mf,text='Say hello to the worlds largest online book store',bg='white',fg='blue').pack()

