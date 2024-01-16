#MY CALCULATOR:-
from tkinter import*
from tkinter import ttk
r=Tk()
r.geometry("385x460")
r.title(" MY CALCULATOR")
r.configure(bg="black")
r.resizable(0,0)
equation=" "

def show(value):
    global equation
    equation+=value
    label_result.configure(text=equation)

#defining clear function to delete the given equation
def clear():
    global equation
    equation=""
    label_result.configure(text=equation)

#defining calculate function to evaluate the given equation
def calculate():
    global equation
    result=eval(equation)
    label_result.configure(text=result)

head=Label(r,text="MY CALCULATOR ",font=("harrington",20,"bold"),bg="black",fg="brown",width=35,height=1)
head.pack()

label_result=Label(r,width=20,height=3,text=" ",font=("source sans pro semibold",20))
label_result.place(x=26,y=50)

btn1=Button(r,text="C",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="orange",fg="white",command=lambda:clear())
btn1.place_configure(x=5,y=180)

btn2=Button(r,text="/",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="black",fg="white",command=lambda:show("/"))
btn2.place_configure(x=100,y=180)

btn3=Button(r,text="%",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="black",fg="white",command=lambda:show("%"))
btn3.place_configure(x=195,y=180)

btn4=Button(r,text="*",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="black",fg="white",command=lambda:show("*"))
btn4.place_configure(x=290,y=180)

btn5=Button(r,text="7",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="skyblue",fg="black",command=lambda:show("7"))
btn5.place_configure(x=5,y=235)

btn6=Button(r,text="8",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="skyblue",fg="black",command=lambda:show("8"))
btn6.place_configure(x=100,y=235)

btn7=Button(r,text="9",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="skyblue",fg="black",command=lambda:show("9"))
btn7.place_configure(x=195,y=235)

btn8=Button(r,text="+",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="black",fg="white",command=lambda:show("+"))
btn8.place_configure(x=290,y=235)

btn9=Button(r,text="4",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="skyblue",fg="black",command=lambda:show("4"))
btn9.place_configure(x=5,y=290)

btn10=Button(r,text="5",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="skyblue",fg="black",command=lambda:show("5"))
btn10.place_configure(x=100,y=290)

btn11=Button(r,text="6",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="skyblue",fg="black",command=lambda:show("6"))
btn11.place_configure(x=195,y=290)

btn12=Button(r,text="-",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="black",fg="white",command=lambda:show("-"))
btn12.place_configure(x=290,y=290)

btn13=Button(r,text="1",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="skyblue",fg="black",command=lambda:show("1"))
btn13.place_configure(x=5,y=345)

btn14=Button(r,text="2",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="skyblue",fg="black",command=lambda:show("2"))
btn14.place_configure(x=100,y=345)

btn15=Button(r,text="3",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="skyblue",fg="black",command=lambda:show("3"))
btn15.place_configure(x=195,y=345)

btn16=Button(r,text="**",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="black",fg="white",command=lambda:show("**"))
btn16.place_configure(x=290,y=345)

btn17=Button(r,text="0",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="skyblue",fg="black",command=lambda:show("0"))
btn17.place_configure(x=5,y=400)

btn18=Button(r,text="//",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="skyblue",fg="black",command=lambda:show("//"))
btn18.place_configure(x=100,y=400)

btn19=Button(r,text=".",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="skyblue",fg="black",command=lambda:show("."))
btn19.place_configure(x=195,y=400)

btn20=Button(r,text="=",width=10,height=2,font=("source sans pro semibold",10,"bold"),bg="green",fg="black",command=lambda:calculate())
btn20.place_configure(x=290,y=400)
