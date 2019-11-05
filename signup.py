from tkinter import *
from tkinter import messagebox as ms
import basic as b
import sqlite3
#import re
from random import randint
# add forget password option and write functions and code :)
#after confirm pass page redirect to login page and continue
with sqlite3.connect('experiment.db') as db: #or simply db= sqlit3.connect()
    c=db.cursor()

#c.execute('''drop table user''')   

c.execute('''
CREATE TABLE IF NOT EXISTS user(regno INTEGER PRIMARY KEY AUTOINCREMENT,fname VARCHAR(55) NOT NULL,
lname VARCHAR(55) NOT NULL,email VARCHAR(55),phnno VARCHAR(10) NOT NULL,pass NOT NULL
) ''')
#CONSTRAINT phnemailcheck CHECK (phnno not like '%[^0-9]%' and email like '%@%.com%' )
insert=''' insert into user (fname,lname,email ,phnno,pass ) values
(?,?,?,?,?) '''          
#c.execute(insert,[('piyush'),('bhambhani'),('bhambhanipiyush4@gmail.com'),('9106647896'),('piyush')])


#c.execute(''' insert into user values ('11714057','piyush','bhambhani','bhambhanipiyush4@gmail.com','9106647896','piyush') ''')
#c.execute(''' select * from user''')
#print(c.fetchone())
db.commit
db.close()

# now i have to send email to newly signed up user to give a otp for first time login


class member:
    def __init__( self,master=None):
        self.master=master
        self.fname = StringVar()
        self.lname=StringVar()
        #self.regno=StringVar()
        self.email=StringVar()
        self.phnno=StringVar()
        self.lemail=StringVar()
        self.pass1=StringVar()
        self.pass2=StringVar()
        self.lpass=StringVar()
        self.oemail=StringVar()
        self.femail=StringVar()
        self.foemail=StringVar()
        self.eotp=StringVar()
        self.fotp=StringVar()
        self.ans=StringVar()
        self.otp=StringVar()
        self.otp2=StringVar()
        self.widgets()
    def new_user(self,frame=None):
        
            
        with sqlite3.connect('experiment.db') as db: #or simply db= sqlit3.connect()
            c=db.cursor()
        find_user=('SELECT * FROM user WHERE email=?')
        c.execute(find_user,[(self.email.get())])
        if c.fetchall(): 
            ms.showerror('Email error','You are already registered sir, so please go to login')
        else:
            if not self.email.get() or not self.phnno.get() or not self.fname.get() :
                ms.showinfo('incomplete info','Please fill all info')
            else:
                 # here i have to check email , phone using regex module if self.email.get()
                self.sendmail()
                db.commit()
                db.close()
        
                #if( mail is valid and send and mail is valid and sent)
                ms.showinfo('success','We have sent you an otp check your mail')
                self.enterotp(self.ofc)
    def login(self):
        self.rf.pack_forget()
        self.pf.pack_forget()
        self.head['text']='Login'
        self.lf.pack()
        self.lemail.set('')
        self.lpass.set('')
        #self.logged_in()
        

    def logged_in(self):
        with sqlite3.connect('experiment.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE email = ? and pass = ?')
        c.execute(find_user,[(self.lemail.get()),(self.lpass.get())])
        result = c.fetchone()
        if result:
            reg_no,name1,name2,mail,phn,p=result
            self.lf.pack_forget()
            b.hf.pack_forget()
            b.mf.pack_forget()
            self.pf.pack_forget()
            self.head.pack_forget()
            from logged_in_list import fun
            fun(b.root,name1,name2,mail,phn)
           
        else:
            ms.showerror('Oops!','Username Not Found.')
                
        db.commit
        db.close()
            
    def enterpass(self,a,frame):
        frame.pack_forget()
        if self.ofc:
            self.ofc.pack_forget()
        self.head['text']='Secure with password'
        self.pf.pack()
        self.pass1.set('')
        self.pass2.set('')
    
        
        
    def saveindb(self):
        
        with sqlite3.connect('experiment.db') as db: #or simply db= sqlit3.connect()
                c=db.cursor()
        if(self.pass1.get()==self.pass2.get()):
            if self.ans==self.otp:
                insert=''' insert into user (fname,lname,email ,phnno,pass ) values
                          (?,?,?,?,?) '''          
                c.execute(insert,[(self.fname.get()),(self.lname.get()),(self.email.get()),(self.phnno.get()),(self.pass2.get())])
                db.commit()
                db.close()
                ms.showinfo('Welcome','Account Created !')
            else:    
            # it implies its otp2, forget pass otp
                insert='''update user set pass=? where email=? '''
                c.execute(insert,[self.pass2.get(),self.femail.get(),])
                db.commit()
                db.close()
                ms.showinfo('Congrats','Password changed !')
            #redirect to login page now
            self.login()           
        else:
                ms.showerror('Error!','Passwords should match !') 



    def sendmail(self):
        self.otp=str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
        from sendmail import fun
        fun(self.email.get(),self.fname.get(),self.lname.get(),self.otp,1)
    def enterotp(self,frame):
        
        self.rf.pack_forget()
        self.head['text']='Enter otp'
        frame.pack()
        self.oemail.set(self.email.get())
        self.eotp.set('')
        
        
       
    def chkotp(self,a,b,frame):
        if(a==b):
            self.ans=a
            
            ms.showinfo('OTP verified','moving to password page')
            self.enterpass(a,frame)
            
                
                
            
        else:
                    ms.showerror('Error!','otp did not match')
                    self.chkotp()
    
    def fpf(self):
        self.lf.pack_forget()
        self.head['text']='Recover account'
        self.fp.pack()
        
    def fpo(self):
        db = sqlite3.connect("experiment.db")

        c=db.cursor()


        c.execute('select fname,lname  from user where email= ?',(self.femail.get(),))
        p=c.fetchone()
        
        if p==None:
            ms.showerror('Error!','please register first')
            self.fp.pack_forget()
            self.signupf()
        else:
            a,b=p
            self.otp2=str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
            from sendmail import fun
            fun(self.femail.get(),a,b,self.otp2,2)

            self.fp.pack_forget()
            self.head['text']='Enter otp'
            self.fof.pack()
            self.foemail.set(self.femail.get())
            self.fotp.set('')
            
        
        
    def rf1(self,frame=None):
        if frame!=None:
            frame.pack_forget()
        self.head['text']='Register now'
        self.rf.pack()
        


       
    def widgets(self):
        self.head=Label(self.master,text='Register Now !',bg='powder blue',relief=RAISED,font=('',35))
        self.head.pack()
        self.rf=Frame(self.master,bg='powder blue',padx=10,pady=10,relief=RAISED)

        Label(self.rf,text='First Name',font=('',20),padx=5,pady=5,bg='powder blue').grid(sticky=W)
        Entry(self.rf,textvariable = self.fname,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.rf,text='Last Name',bg='powder blue',font=('',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.rf,textvariable = self.lname,bd = 5,font = ('',15)).grid(row=1,column=1)
        Label(self.rf,text='Email',bg='powder blue',font=('',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.rf,textvariable = self.email,bd = 5,font = ('',15)).grid(row=2,column=1)
        Label(self.rf,text='phone no',bg='powder blue',font=('',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.rf,textvariable = self.phnno,bd = 5,font = ('',15)).grid(row=3,column=1)
        Button(self.rf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid()
        Button(self.rf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid(row=4,column=1,sticky=E)
        self.rf1()

        
   
        self.of=Frame(self.master,padx=10,pady=10,bg='powder blue',relief=RAISED)
        Label(self.of,text='Email:',bg='powder blue',font=('',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.of,textvariable = self.oemail,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.of,text='Enter OTP:',bg='powder blue',font=('',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.of,textvariable = self.eotp,bd = 5,font = ('',15)).grid(row=1,column=1)
        Button(self.of,text = 'Resend OTP',bd = 3 ,font = ('',15),padx=5,pady=5,command= self.fpo).grid() # sendmail fun should be there if we come from 1st otp
        Button(self.of,text = 'Next',bd = 3 ,font = ('',15),padx=5,pady=5,command=lambda: self.chkotp(self.eotp.get(),self.otp,self.of)).grid(row=2,column=1,sticky=E)

        self.ofc=Frame(self.master,padx=10,pady=10,bg='powder blue',relief=RAISED)
        Label(self.ofc,text='Email:',bg='powder blue',font=('',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.ofc,textvariable = self.oemail,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.ofc,text='Enter OTP:',bg='powder blue',font=('',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.ofc,textvariable = self.eotp,bd = 5,font = ('',15)).grid(row=1,column=1)
        Button(self.ofc,text = 'Resend OTP',bd = 3 ,font = ('',15),padx=5,pady=5,command= self.sendmail).grid() # sendmail fun should be there if we come from 1st otp
        Button(self.ofc,text = 'Next',bd = 3 ,font = ('',15),padx=5,pady=5,command=lambda: self.chkotp(self.eotp.get(),self.otp,self.of)).grid(row=2,column=1,sticky=E)

        self.pf=Frame(self.master,padx=10,pady=10,bg='powder blue')
        Label(self.pf,text='Enter password:',font=('',20),padx=5,pady=5,bg='powder blue').grid(sticky=W)
        Entry(self.pf,textvariable = self.pass1,bd = 5,font = ('',15),show = '*').grid(row=0,column=1)
        Label(self.pf,text='Confirm password:',bg='powder blue',font=('',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.pf,textvariable = self.pass2,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.pf,text = 'Go to Signup',bd = 3 ,font = ('',15),padx=5,pady=5,command=lambda: self.rf1(self.lf)).grid() 
        p=Button(self.pf,text = 'Next',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.saveindb).grid(row=2,column=1,sticky=E)

        self.lf=Frame(self.master,padx=10,pady=10,bg='powder blue')
        Label(self.lf,text='Enter email:',font=('',20),padx=5,pady=5,bg='powder blue').grid(sticky=W)
        Entry(self.lf,textvariable = self.lemail,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.lf,text='Enter password:',bg='powder blue',font=('',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.lf,textvariable = self.lpass,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.lf,text = 'Go to Signup',bd = 3 ,font = ('',15),padx=5,pady=5,command=lambda: self.rf1(self.lf)).grid(sticky=W) 
        Button(self.lf,text='Forgot pass ?',bd=3,font=('',15),padx=5,pady=5,command=self.fpf).grid(row=2,column=1,sticky=W)

        Button(self.lf,text = 'Next',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.logged_in).grid(row=2,column=2,sticky=W)

        self.fp=Frame(self.master,padx=10,pady=10,bg='powder blue')
        Label(self.fp,text='Enter email:',font=('',20),padx=5,pady=5,bg='powder blue').grid(sticky=W)
        Entry(self.fp,textvariable = self.femail,bd = 5,font = ('',15)).grid(row=0,column=1)
        
        Button(self.fp,text = 'Go to Signup',bd = 3 ,font = ('',15),padx=5,pady=5,command=lambda: self.rf1(self.fp)).grid(sticky=W)
        Button(self.fp,text = 'Next',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.fpo).grid(row=1,column=1,sticky=E)



        self.fof=Frame(self.master,padx=10,pady=10,bg='powder blue')
        Label(self.fof,text='Email:',bg='powder blue',font=('',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.fof,textvariable = self.foemail,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.fof,text='Enter OTP:',bg='powder blue',font=('',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.fof,textvariable = self.fotp,bd = 5,font = ('',15)).grid(row=1,column=1)
        Button(self.fof,text = 'Resend OTP',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.fpo).grid() # change command
        Button(self.fof,text = 'Next',bd = 3 ,font = ('',15),padx=5,pady=5,command=lambda: self.chkotp(self.fotp.get(),self.otp2,self.fof)).grid(row=2,column=1,sticky=E)
        




if __name__=='__main__':
    
    member(b.root)
