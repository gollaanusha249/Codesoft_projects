import tkinter as tk
import math
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("570x640")
root.configure(bg="grey")

s=""
def show(value):
    global s
    s+=value
    label_result.config(text=s)

def sqrt(value):
    r = math.sqrt(int(value))
    label_result.config(text=r)

def clear():
    global s
    s=""
    label_result.config(text=s)

def delete():
    global s 
    s = s[:-1]  
    label_result.config(text=s)  

def calculate():
    global s,result
    result = ""
    if s !="":
        try:
            result = eval(s)
        except:
            result="error"
            s=""
    label_result.config(text=result)

label_result=tk.Label(root,width=22,height=1,text="",font=("arial",30),bg="lightblue",bd=8)
label_result.place(x=23,y=16)

tk.Button(root,text="AC",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="light coral",font=("arial",30,"bold"),command=lambda: clear()).place(x=10,y=100)
tk.Button(root,text="DEL",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="wheat",font=("arial",30,"bold"),command=lambda: delete()).place(x=150,y=100)
tk.Button(root,text="%",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="deep pink",font=("arial",30,"bold"),command=lambda: show("%")).place(x=290,y=100)
tk.Button(root,text="x",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="deep pink",font=("arial",30,"bold"),command=lambda: show("*")).place(x=430,y=100)

tk.Button(root,text="7",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="violet",font=("arial",30,"bold"),command=lambda: show("7")).place(x=10,y=200)
tk.Button(root,text="8",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="violet",font=("arial",30,"bold"),command=lambda: show("8")).place(x=150,y=200)
tk.Button(root,text="9",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="violet",font=("arial",30,"bold"),command=lambda: show("9")).place(x=290,y=200)
tk.Button(root,text="-",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="deep pink",font=("arial",30,"bold"),command=lambda: show("-")).place(x=430,y=200)

tk.Button(root,text="4",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="violet",font=("arial",30,"bold"),command=lambda: show("4")).place(x=10,y=300)
tk.Button(root,text="5",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="violet",font=("arial",30,"bold"),command=lambda: show("5")).place(x=150,y=300)
tk.Button(root,text="6",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="violet",font=("arial",30,"bold"),command=lambda: show("6")).place(x=290,y=300)
tk.Button(root,text="+",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="deep pink",font=("arial",30,"bold"),command=lambda: show("+")).place(x=430,y=300)

tk.Button(root,text="1",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="violet",font=("arial",30,"bold"),command=lambda: show("1")).place(x=10,y=400)
tk.Button(root,text="2",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="violet",font=("arial",30,"bold"),command=lambda: show("2")).place(x=150,y=400)
tk.Button(root,text="3",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="violet",font=("arial",30,"bold"),command=lambda: show("3")).place(x=290,y=400)
tk.Button(root,text="0",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="violet",font=("arial",30,"bold"),command=lambda: show("0")).place(x=10,y=500)

tk.Button(root,text="/",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="deep pink",font=("arial",30,"bold"),command=lambda: show("/")).place(x=430,y=400)

tk.Button(root,text=".",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="lightgreen",font=("arial",30,"bold"),command=lambda: show(".")).place(x=150,y=500)
tk.Button(root,text="=",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="orange",font=("arial",30,"bold"),command=lambda: calculate()).place(x=430,y=500)
tk.Button(root,text="x^y",width=5,height=1,bd=5,relief=tk.RAISED,fg="black",bg="lightgreen",font=("arial",30,"bold"),command=lambda: show("**")).place(x=290,y=500)

root.mainloop()
