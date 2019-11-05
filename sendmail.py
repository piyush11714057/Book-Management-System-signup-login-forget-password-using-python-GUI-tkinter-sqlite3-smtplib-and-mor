toemail='randompiyush456@gmail.com'
fname='Harish'
sname='golu'
from random import randint

otp=str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
# dont change anything as i have used this file in BMS directly if this changes that wont work
n=1
def fun(toemail,fname,sname,otp,n):
    
    import smtplib
    import secretfile as s
    import socket
    socket.getaddrinfo('localhost', 8080)

    if n==1:
        name=fname+' '+sname
        sender='BOOKrey-Book Management System'
        sub='OTP for email confirmation'
        content=''' Hello '''+name+''' 
        BOOKrey-BMS welcomes you to be its member. Sign-in using OTP: '''+otp+''' .Thanks for choosing us :) 
        '''
    elif n==2:
        name=fname+' '+sname
        sender='BOOKrey-Book Management System'
        sub='OTP for Password change'
        content=''' Hello '''+name+''' 
        BOOKrey-BMS cares for you if you've forgot your pass
        just enter this '''+otp+''' as OTP and change your password.
        Thanks for choosing us :) 
        '''
        
    header='To:'+name+'\n'+'From: '+sender+'\n'+'\n'+'Subject:'+sub+'\n'
    content=header+content
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo() # identify computer
    mail.starttls() # transport layer security takes care of encription and decryption
    mail.login(s.email,s.passw)
    mail.sendmail(s.email,toemail,content)
    mail.close()
'''
if __name__=='__main__':
    
    member(b.root)
'''
