from tkinter import messagebox
import mysql
import mysql.connector as con
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import subprocess
import datetime
import sys

def go_back(username, title, eid):
    root.destroy()
    subprocess.run(["python", "manager_page.py", username, title, str(eid)])

def show_customers():
    datatxt.configure(state='normal')
    connection = con.connect(host="localhost", user="root", password="password", database="supermarket", port="3306")
    cursor = connection.cursor()
    datatxt.delete('1.0', tk.END)

    customerID = customeridtxt.get()
    phone = phonetxt.get()
    name = nametxt.get()
    email = emailtxt.get()

    query = "SELECT * FROM customers WHERE 1=1"

    if customerID:
        query += f" AND CustomerID = '{customerID}'"
    if phone:
        query += f" AND Phone = '{phone}'"
    if name:
        query += f" AND Name = '{name}'"
    if email:
        query += f" AND Email = '{email}'"

    try:
        cursor.execute(query)
    except:
        datatxt.insert(tk.END, "Invalid query or no customers found")

    try:
        data = cursor.fetchall()
        datatxt.insert('1.0', "CustomerID\t\tName\t\tPhone\t\tEmail\n")
        if len(data) != 0:
            for row in data:
                line = str(row[0]) + "\t\t" + row[1] + "\t\t" + row[2] + "\t\t" + row[3]
                datatxt.insert(tk.END, line + "\n")
        datatxt.configure(state='disabled')
    except:
        datatxt.insert(tk.INSERT, "Couldn't fetch data!\n")
    cursor.close()
    connection.close()

def edit_customer():
    customerID = customeridtxt.get()
    phone = phonetxt.get()
    name = nametxt.get()
    email = emailtxt.get()

    if customerID == '' or phone == '' or name == '' or email == '':
        messagebox.showerror("Error", "Please fill in all the fields.")
        return

    try:
        customerID = int(customerID)
    except:
        messagebox.showerror("Error", "Invalid input format for Customer ID.")
        return

    connection = con.connect(host="localhost", user="root", password="password", database="supermarket", port="3306")
    cursor = connection.cursor()

    query = f"UPDATE customers SET Phone = '{phone}', Name = '{name}', Email = '{email}' WHERE CustomerID = {customerID}"

    try:
        cursor.execute(query)
        connection.commit()

        messagebox.showinfo("Success", "Customer edited successfully")

        customeridtxt.delete(0, tk.END)
        phonetxt.delete(0, tk.END)
        nametxt.delete(0, tk.END)
        emailtxt.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Failed to edit customer")

    cursor.close()
    connection.close()

username = sys.argv[1]
title = sys.argv[2]
eid = int(sys.argv[3])

root = tk.Tk()
root.configure(background="#222831", height=200, width=200)
root.geometry("1050x600")
root.geometry("+100+20")

datatxt = ScrolledText(root, background="#ECE5C7")
datatxt.place(anchor="nw", relheight=0.6, relwidth=1.0)

customeridlbl = tk.Label(root, background="#393E46")
customeridlbl.configure(text='Customer ID:')
customeridlbl.place(anchor="nw", relwidth=0.15, relx=0.02, rely=0.7)

customeridtxt = tk.Entry(root, background="#EEEEEE")
customeridtxt.place(anchor="nw", relwidth=0.2, relx=0.17, rely=0.7)

phonelbl = tk.Label(root, background="#393E46")
phonelbl.configure(text='Phone:')
phonelbl.place(anchor="nw", relwidth=0.1, relx=0.4, rely=0.7)

phonetxt = tk.Entry(root, background="#EEEEEE")
phonetxt.place(anchor="nw", relwidth=0.19, relx=0.5, rely=0.7)

namelbl = tk.Label(root, background="#393E46")
namelbl.configure(text='Name:')
namelbl.place(anchor="nw", relwidth=0.1, relx=0.4, rely=0.75)

nametxt = tk.Entry(root, background="#EEEEEE")
nametxt.place(anchor="nw", relwidth=0.19, relx=0.5, rely=0.75)

emaillbl = tk.Label(root, background="#393E46")
emaillbl.configure(text='Email:')
emaillbl.place(anchor="nw", relwidth=0.15, relx=0.02, rely=0.75)

emailtxt = tk.Entry(root, background="#EEEEEE")
emailtxt.place(anchor="nw", relwidth=0.2, relx=0.17, rely=0.75)

editCustomerbt = tk.Button(root, background="#00ADB5", command=lambda: edit_customer())
editCustomerbt.configure(text='Edit Customer')
editCustomerbt.place(anchor="nw", relwidth=0.2, relx=0.7, rely=0.7)

showCustomersbt = tk.Button(root, command=lambda: show_customers(), background="#00ADB5")
showCustomersbt.configure(text='Show Customers')
showCustomersbt.place(anchor="nw", relwidth=0.2, relx=0.7, rely=0.75)

backbt = tk.Button(root, command=lambda: go_back(username, title, eid), background="#00ADB5")
backbt.configure(text='Back')
backbt.place(anchor="nw", relwidth=0.2, relx=0.7, rely=0.8)

root.mainloop()
