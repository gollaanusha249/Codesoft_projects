import tkinter as tk
from tkinter import messagebox

contacts = {}  

def populate_listbox():
    listbox.delete(0, tk.END)
    for name in contacts:
        listbox.insert(tk.END, name)

# Function to add a contact
def add_contact():
    name = entry1.get()
    phone = entry2.get()
    mail = entry3.get()
    address = entry4.get()

    if name and phone and mail and address:
        if name not in listbox.get(0, tk.END):
            contacts[name] = {"PhoneNo": phone, "Mail": mail, "Address": address}
            listbox.insert(tk.END, name)
            entry1.delete(0, tk.END)
            entry2.delete(0, tk.END)
            entry3.delete(0, tk.END)
            entry4.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Contact with this name already exists.")
    else:
        messagebox.showerror("Error", "Please enter all details.")

# Function to view contact details
def view_contact():
    selected_indices = listbox.curselection()
    if selected_indices:
        for selected_index in selected_indices:
            selected_item = listbox.get(selected_index)
            contact_details = contacts.get(selected_item)
            if contact_details:
                message = f"Name: {selected_item}\n"
                message += f"PhoneNo: {contact_details['PhoneNo']}\n"
                message += f"Mail: {contact_details['Mail']}\n"
                message += f"Address: {contact_details['Address']}\n\n"
                messagebox.showinfo("Contact Details", message)
            else:
                messagebox.showinfo("Contact Details", f"Contact '{selected_item}' not found.")

# Function to search for a contact
def search_contact():
    search_name = entry1.get()
    if search_name in contacts:
        messagebox.showinfo("Search Result", f"Contact '{search_name}' found.")
    else:
        messagebox.showinfo("Search Result", f"Contact '{search_name}' not found.")

# Function to update contact details
def update_contact():
    selected_index = listbox.curselection()
    if selected_index:
        selected_item = listbox.get(selected_index)
        updated_phone = entry2.get()
        updated_mail = entry3.get()
        updated_address = entry4.get()
        if selected_item and updated_phone and updated_mail and updated_address:
            contacts[selected_item[0]]["PhoneNo"] = updated_phone
            contacts[selected_item[0]]["Mail"] = updated_mail
            contacts[selected_item[0]]["Address"] = updated_address
            messagebox.showinfo("Update", f"Contact '{selected_item[0]}' updated.")
        else:
            messagebox.showerror("Update Error", "Please enter all details to update.")

# Function to delete the selected contact
def delete_contact():
    selected_indices = listbox.curselection()
    if selected_indices:
        for selected_index in selected_indices:
            selected_item = listbox.get(selected_index)
            del contacts[selected_item]
            listbox.delete(selected_index)

# Function to delete all contacts
def delete_all():
    listbox.delete(0, tk.END)
    contacts.clear()

# Function to exit the program
def exit_program():
    root.destroy()

root = tk.Tk()
root.title("CONTACT BOOK")
root.geometry("450x450")
root.configure(bg="violet")

label = tk.Label(root, text="Contact Book", width=15, height=1,font="arial")
label.place(x=160, y=30)
label = tk.Label(root, text="Name", width=7, height=0)
label.place(x=6, y=90)
label = tk.Label(root, text="PhoneNo", width=7, height=0)
label.place(x=6, y=120)
label = tk.Label(root, text="Mail", width=7, height=0)
label.place(x=230, y=90)
label = tk.Label(root, text="Address", width=7, height=0)
label.place(x=230, y=120)

entry1 = tk.Entry(root,bg="white")  
entry1.place(x=70,y=90) 
entry2 = tk.Entry(root,bg="white")  
entry2.place(x=70,y=122) 
entry3 = tk.Entry(root,bg="white")  
entry3.place(x=300,y=90) 
entry4 = tk.Entry(root,bg="white")  
entry4.place(x=300,y=122) 

# Add buttons for View, Search, Update, Delete, Delete All, and Exit
tk.Button(root, text="ADD", width=10, height=0, bd=1, fg="black", bg="orange", font=("arial", 10, "bold"), command=add_contact).place(x=55, y=170)
tk.Button(root, text="VIEW", width=10, height=0, bd=1, fg="black", bg="orange", font=("arial", 10, "bold"), command=view_contact).place(x=55, y=200)
tk.Button(root, text="SEARCH", width=10, height=0, bd=1, fg="black", bg="orange", font=("arial", 10, "bold"), command=search_contact).place(x=55, y=230)
tk.Button(root, text="UPDATE", width=10, height=0, bd=1, fg="black", bg="orange", font=("arial", 10, "bold"), command=update_contact).place(x=55, y=260)
tk.Button(root, text="DELETE", width=10, height=0, bd=1, fg="black", bg="orange", font=("arial", 10, "bold"), command=delete_contact).place(x=55, y=290)
tk.Button(root, text="DELETE ALL", width=10, height=0, bd=1, fg="black", bg="orange", font=("arial", 10, "bold"), command=delete_all).place(x=55, y=320)
tk.Button(root, text="EXIT", width=10, height=0, bd=1, fg="black", bg="orange", font=("arial", 10, "bold"), command=exit_program).place(x=55, y=350)

listbox = tk.Listbox(root, height=11, bd=7, bg="yellow", width=22, font=("arial", 10,"bold"))
listbox.place(x=220, y=170)

scrollbar = tk.Scrollbar(root)
scrollbar.place(x=380,y=180)
listbox.config(yscrollcommand=scrollbar.set)

root.mainloop()