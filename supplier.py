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

def show_suppliers():
    datatxt.configure(state='normal')
    connection = con.connect(host="localhost", user="root", password="password", database="supermarket", port="3306")
    cursor = connection.cursor()
    datatxt.delete('1.0', tk.END)

    supplierid = supplieridentry.get()
    phone = phoneentry.get()
    name = nameentry.get()
    category = categoryentry.get()

    query = "SELECT * FROM suppliers WHERE 1=1"

    if supplierid:
        query += f" AND SupplierID = '{supplierid}'"
    if phone:
        query += f" AND Phone = '{phone}'"
    if name:
        query += f" AND Name = '{name}'"
    if category:
        query += f" AND Category = '{category}'"

    try:
        cursor.execute(query)
    except:
        datatxt.insert(tk.END, "Invalid query or no suppliers found")

    try:
        data = cursor.fetchall()
        datatxt.insert('1.0', "SupplierID\t\tName\t\tPhone\t\tCategory\n")
        if len(data) != 0:
            for row in data:
                line = str(row[0]) + "\t\t" + row[1] + "\t\t" + row[2] + "\t\t" + row[3]
                datatxt.insert(tk.END, line + "\n")
        datatxt.configure(state='disabled')
    except:
        datatxt.insert(tk.INSERT, "Couldn't fetch data!\n")
    cursor.close()
    connection.close()

def add_supplier():
    name = nameentry.get()
    phone = phoneentry.get()
    category = categoryentry.get()

    if name == '' or phone == '' or category == '':
        messagebox.showerror("Error", "Please fill in all the fields.")
        return

    connection = con.connect(host="localhost", user="root", password="password", database="supermarket", port="3306")
    cursor = connection.cursor()

    query = "INSERT INTO suppliers (name, phone, category) VALUES (%s, %s, %s)"
    values = (name, phone, category)

    try:
        cursor.execute(query, values)
        connection.commit()

        messagebox.showinfo("Success", "Supplier added successfully")

        nameentry.delete(0, tk.END)
        phoneentry.delete(0, tk.END)
        categoryentry.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Failed to add supplier")

    cursor.close()
    connection.close()

def edit_supplier():
    supplier_id = supplieridentry.get()
    phone = phoneentry.get()
    category = categoryentry.get()
    name = nameentry.get()

    if supplier_id == '' or phone == '' or category == '' or name == '':
        messagebox.showerror("Error", "Please fill in all the fields.")
        return

    connection = con.connect(host="localhost", user="root", password="password", database="supermarket", port="3306")
    cursor = connection.cursor()

    query = "UPDATE suppliers SET phone = %s, category = %s, name = %s WHERE supplierID = %s"
    values = (phone, category, name, supplier_id)

    try:
        cursor.execute(query, values)
        connection.commit()

        messagebox.showinfo("Success", "Supplier updated successfully")

        supplieridentry.delete(0, tk.END)
        phoneentry.delete(0, tk.END)
        categoryentry.delete(0, tk.END)
        nameentry.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Failed to update supplier")

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

supplieridlbl = tk.Label(root)
supplieridlbl.configure(text='Supplier ID', background="#393E46")
supplieridlbl.place(anchor="nw", relwidth=0.1, relx=0.05, rely=0.65)

supplieridentry = tk.Entry(root, background="#EEEEEE")
supplieridentry.place(anchor="nw", relwidth=0.15, relx=0.15, rely=0.65)

namelbl = tk.Label(root, background="#393E46")
namelbl.configure(text='Name')
namelbl.place(anchor="nw", relwidth=0.1, relx=0.05, rely=0.75)

nameentry = tk.Entry(root, background="#EEEEEE")
nameentry.place(anchor="nw", relwidth=0.15, relx=0.15, rely=0.75)

phonelbl = tk.Label(root, background="#393E46")
phonelbl.configure(text='Phone')
phonelbl.place(anchor="nw", relwidth=0.1, relx=0.4, rely=0.65)

phoneentry = tk.Entry(root, background="#EEEEEE")
phoneentry.place(anchor="nw", relwidth=0.15, relx=0.5, rely=0.65)

categorylbl = tk.Label(root, background="#393E46")
categorylbl.configure(text='Category')
categorylbl.place(anchor="nw", relwidth=0.1, relx=0.4, rely=0.75)

categoryentry = tk.Entry(root, background="#EEEEEE")
categoryentry.place(anchor="nw", relwidth=0.15, relx=0.5, rely=0.75)

showSuppliersbt = tk.Button(root, command=show_suppliers, background="#00ADB5")
showSuppliersbt.configure(text='Show Suppliers')
showSuppliersbt.place(anchor="nw", relwidth=0.2, relx=0.05, rely=0.9)

addSupplierbt = tk.Button(root, command=add_supplier, background="#00ADB5")
addSupplierbt.configure(text='Add Supplier')
addSupplierbt.place(anchor="nw", relwidth=0.2, relx=0.3, rely=0.9)

editSupplierbt = tk.Button(root, command=edit_supplier, background="#00ADB5")
editSupplierbt.configure(text='Edit Supplier')
editSupplierbt.place(anchor="nw", relwidth=0.2, relx=0.55, rely=0.9)

backbt = tk.Button(root, command=lambda: go_back(username, title, eid), background="#00ADB5")
backbt.configure(text='Back')
backbt.place(anchor="nw", relwidth=0.2, relx=0.8, rely=0.9)

root.mainloop()
