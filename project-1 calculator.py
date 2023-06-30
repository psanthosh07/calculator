from tkinter import *
from sympy import *
from tkinter import messagebox
root=Tk()
root.title("Caclulator")
root.geometry("280x150")
dis=StringVar()
eq=""
def ad(n):
    global eq
    eq=eq+str(n)
    dis.set(eq)
def calc():
    try :
        global eq
        t=str(eval(eq))

        dis.set(t)
    except:
        messagebox.showwarning("ERROR","INVALID INPUT")
exp=Entry(root,textvariable=dis).grid(columnspan=6,ipadx=70)
n1=Button(root,text="1",height=1,width=7,command=lambda:ad(1)).grid(row=4,column=1)
n2=Button(root,text="2",height=1,width=7,command=lambda:ad(2)).grid(row=4,column=2)
n3=Button(root,text="3",height=1,width=7,command=lambda:ad(3)).grid(row=4,column=3)
n4=Button(root,text="4",height=1,width=7,command=lambda:ad(4)).grid(row=3,column=1)
n5=Button(root,text="5",height=1,width=7,command=lambda:ad(5)).grid(row=3,column=2)
n6=Button(root,text="6",height=1,width=7,command=lambda:ad(6)).grid(row=3,column=3)
n7=Button(root,text="7",height=1,width=7,command=lambda:ad(7)).grid(row=2,column=1)
n8=Button(root,text="8",height=1,width=7,command=lambda:ad(8)).grid(row=2,column=2)
n9=Button(root,text="9",height=1,width=7,command=lambda:ad(9)).grid(row=2,column=3)
n0=Button(root,text="0",height=1,width=7,command=lambda:ad(0)).grid(row=5,column=1)
n00=Button(root,text=".",height=1,width=7,command=lambda:ad('.')).grid(row=5,column=2)
ndot=Button(root,text="x",height=1,width=7,command=lambda:ad("*")).grid(row=5,column=3)
nadd=Button(root,text="+",height=1,width=7,command=lambda:ad("+")).grid(row=4,column=4)
nminus=Button(root,text="-",height=1,width=7,command=lambda:ad("-")).grid(row=3,column=4)
nmul=Button(root,text="=",height=1,width=7,command=lambda:calc()).grid(row=5,column=4)
ndiv=Button(root,text="÷",height=1,width=7,command=lambda:ad("/")).grid(row=2,column=4)
root.mainloop()