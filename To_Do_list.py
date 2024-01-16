#To-Do List:-
from tkinter import*
r=Tk()
r.geometry("550x450")
r.title("To-Do List")
r.configure(bg="lavender")
r.resizable(9,9)

def addtask():
    task=label_tasks_entry.get()
    listbox_tasks.insert(END,task)

def edittask():
    label_tasks_entry.delete(0,END)

def cleartask():
    task=label_tasks_entry.get()
    listbox_tasks.delete(END)

def deletetask():
    task=label_tasks_entry.get()
    listbox_tasks.delete(0,END)

head=Label(r,text="To-Do List",font=("harrington",20,"bold"),bg="lavender",fg="purple",width=35,height=1)
head.place(x=8,y=35)

head1=Label(r,text="__________",font=("curlz mt",20,"bold"),bg="lavender",fg="brown",width=38,height=1)
head1.place(x=1,y=1)


main=Label(r,text="Enter the Task:",font=("source sans pro semibold",15),bg="lavender",fg="black",width=12,height=1)
main.place(x=25,y=90)

listbox_tasks=Listbox(r,width=38,height=19)
listbox_tasks.place(x=270,y=120)

label_tasks_entry=Entry(r,width=20,bg="white",font=20)
label_tasks_entry.place(x=25,y=120)

add_tasks=Button(r,text="Add task",width=10,height=1,fg="black",bg="white",font=("source sans pro semibold",15,"bold"),command=lambda:addtask())
add_tasks.place(x=25,y=170)

edit_tasks=Button(r,text="Edit task",width=10,height=1,fg="black",bg="white",font=("source sans pro semibold",15,"bold"),command=lambda:edittask())
edit_tasks.place(x=25,y=240)

clear_task=Button(r,text="Clear task",width=10,height=1,fg="black",bg="white",font=("source sans pro semibold",15,"bold"),command=lambda:cleartask())
clear_task.place(x=25,y=310)

delete_task=Button(r,text="Delete task",width=10,height=1,fg="black",bg="white",font=("source sans pro semibold",15,"bold"),command=lambda:deletetask())
delete_task.place(x=25,y=380)
