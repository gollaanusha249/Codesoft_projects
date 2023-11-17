import tkinter as tk

def add_item():
    item = entry.get()  
    if item:
        listbox.insert(tk.END, item) 
        entry.delete(0, tk.END)  
        
def delete_item():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)

def delete_all():
    listbox.delete(0, tk.END)

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x250+100+300")
root.configure(bg="skyblue")

label = tk.Label(root, text="To-Do List", width=15, height=1,font="arial")
label.place(x=120, y=20)

entry = tk.Entry(root,bg="white")  
entry.place(x=40,y=90)  

tk.Button(root,text = "ADD",width=10,height=0,bd=1,fg="black",bg="pink",font=("arial",10,"bold"),command=add_item).place(x=55,y=120)
tk.Button(root,text = "DELETE",width=10,height=0,bd=1,fg="black",bg="pink",font=("arial",10,"bold"),command=delete_item).place(x=55,y=150)
tk.Button(root, text = "DELETE ALL", width=10, height=0, bd=1, fg="black", bg="pink", font=("arial", 10, "bold"), command=delete_all).place(x=55, y=180)
tk.Button(root, text = "EXIT", width=10, height=0, bd=1, fg="black", bg="pink", font=("arial", 10, "bold"), command=exit_program).place(x=55, y=210)

listbox = tk.Listbox(root, height=8, bd=7, bg="lightgreen", width=22, font=("arial", 10,"bold"))
listbox.place(x = 220, y = 90)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side = tk.RIGHT)

listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)

root.mainloop()