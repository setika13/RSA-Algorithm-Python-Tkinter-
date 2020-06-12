from tkinter import *
root =Tk()
root.title("RSA")
root.geometry("640x460")
heading=Label(root,text="RSA WITH PYTHON").pack()
label1=Label(root,text="enter the value of p").place(x=10,y=50)
label1=Label(root,text="enter the value of q").place(x=10,y=100)
label1=Label(root,text="enter the message").place(x=10,y=150)
p=StringVar()
q=StringVar()
r=StringVar()
e1=Entry(root,textvariable=p).place(x=170,y=50)
e2=Entry(root,textvariable=q).place(x=170,y=100)
e3=Entry(root,textvariable=r).place(x=170,y=150)
def rsa():
    root1 =Tk()
    root1.title("RSA RESULT")
    root1.geometry("640x460")
    Label(root1,text="RSA ALGORITHM").place(x=200,y=25)
    p1=int(p.get())
    q1=int(q.get())
    m=int(r.get())
    n=p1*q1
    Label(root1,text="n=>p*q="+str(n)).place(x=10,y=50)
    phi=(p1-1)*(q1-1)
    Label(root1,text="Eucler's function (phi) ="+str(phi)).place(x=10,y=75)
    def gcd(a,b):
        if(b==0):
            return a
        else:
            return gcd(b,a%b)
    for e in  range(2,phi):
        if(gcd(e,phi)==1):
            break
    Label(root1,text="e="+str(e)).place(x=10,y=100)
    for i in range(1,10):
        x=1+i*phi
        if(x%e==0):
            d=int(x/e)
            break
    Label(root1,text="d="+str(d)).place(x=10,y=125)
    public_key=(e,n)
    private_key=(d,n)
    Label(root1,text="Public_Key="+str(public_key)).place(x=10,y=150)
    Label(root1,text="Private Key="+str(private_key)).place(x=10,y=175)
    c=(m**e)%n
    Label(root1,text="Encrypted Message="+str(c)).place(x=10,y=200)
    m1=(c**d)%n
    Label(root1,text="Decrypted Message="+str(m1)).place(x=10,y=225)
b1=Button(root,text="ENTER",command=rsa).place(x=150,y=200)
root.mainloop()