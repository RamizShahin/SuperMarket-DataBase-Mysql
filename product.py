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

def show_products():
    datatxt.configure(state='normal')
    connection = con.connect(host="localhost", user="root", password="password", database="supermarket", port="3306")
    cursor = connection.cursor()
    datatxt.delete('1.0', tk.END)

    productID = pidtxt.get()
    quantity = quantitytxt.get()
    price = pricetxt.get()
    name = nametxt.get()
    category = categorytxt.get()
    supplierID = supplieridtxt.get()

    query = "SELECT * FROM products WHERE 1=1"

    if productID:
        query += " AND productID = %s"
    if quantity:
        if quantity.startswith("<"):
            query += f" AND quantity < {quantity[1:]}"
        elif quantity.startswith(">"):
            query += f" AND quantity > {quantity[1:]}"
        else:
            query += " AND quantity = %s"
    if price:
        if price.startswith("<"):
            query += f" AND price < {price[1:]}"
        elif price.startswith(">"):
            query += f" AND price > {price[1:]}"
        else:
            query += " AND price = %s"
    if name:
        query += " AND name = %s"
    if category:
        query += " AND category = %s"
    if supplierID:
        query += " AND supplierID = %s"

    try:
        cursor.execute(query)
    except:
        datatxt.insert(tk.END, "Invalid query or product does not exist")

    try:
        data = cursor.fetchall()
        datatxt.insert('1.0', "productID\t\tname\t\tquantity\t\tunit\t\tcategory\t\tsupplier_id\t\tprice\n")
        if len(data) != 0:
            for row in data:
                line = str(row[0]) + "\t\t" + row[1] + "\t\t" + str(row[2]) + "\t\t" + str(row[3]) + "\t\t" + row[4] + "\t\t" + str(row[5]) + "\t\t" + str(row[6])
                datatxt.insert(tk.END, line + "\n")
        datatxt.configure(state='disabled')
    except:
        datatxt.insert(tk.INSERT, "Couldn't fetch data!\n")
    cursor.close()
    connection.close()

def edit_product():
    productID = pidtxt.get()
    quantity = quantitytxt.get()
    price = pricetxt.get()
    supplierID = supplieridtxt.get()
    name = nametxt.get()
    category = categorytxt.get()

    if productID == '' or quantity == '':
        messagebox.showerror("Error", "Please fill in the productID and quantity fields.")
        return

    try:
        productID = int(productID)
        quantity = int(quantity)
        if price:
            price = float(price)
        if supplierID:
            supplierID = int(supplierID)
    except:
        messagebox.showerror("Error", "Invalid input format for productID, quantity, supplier_id, or price.")
        return

    connection = con.connect(host="localhost", user="root", password="password", database="supermarket", port="3306")
    cursor = connection.cursor()

    query = f"UPDATE products SET quantity = {quantity}"
    if price:
        query += f", price = {price}"
    if supplierID:
        query += f", supplierID = {supplierID}"
    if name:
        query += f", name = '{name}'"
    if category:
        query += f", category = '{category}'"

    query += f" WHERE productID = {productID}"

    try:
        cursor.execute(query)
        connection.commit()

        messagebox.showinfo("Success", "Product edited successfully")

        pidtxt.delete(0, tk.END)
        quantitytxt.delete(0, tk.END)
        pricetxt.delete(0, tk.END)
        supplieridtxt.delete(0, tk.END)
        nametxt.delete(0, tk.END)
        categorytxt.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Failed to edit product")

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

pidlbl = tk.Label(root)
pidlbl.configure(text='productID', background="#393E46")
pidlbl.place(anchor="nw", relwidth=0.08, relx=0.02, rely=0.7)

pidtxt = tk.Entry(root, background="#EEEEEE")
pidtxt.place(anchor="nw", relwidth=0.16, relx=0.14, rely=0.7, x=0, y=0)

quantitylbl = tk.Label(root, background="#393E46")
quantitylbl.configure(text='quantity')
quantitylbl.place(anchor="nw", relwidth=0.08, relx=0.34, rely=0.7)

quantitytxt = tk.Entry(root, background="#EEEEEE")
quantitytxt.place(anchor="nw", relwidth=0.16, relx=0.45, rely=0.7, x=0, y=0)

pricelbl = tk.Label(root, background="#393E46")
pricelbl.configure(text='price')
pricelbl.place(anchor="nw", relwidth=0.08, relx=0.02, rely=0.8)

pricetxt = tk.Entry(root, background="#EEEEEE")
pricetxt.place(anchor="nw", relwidth=0.16, relx=0.14, rely=0.8)

supplieridlbl = tk.Label(root, background="#393E46")
supplieridlbl.configure(text='supplierID')
supplieridlbl.place(anchor="nw", relwidth=0.08, relx=0.34, rely=0.8)

supplieridtxt = tk.Entry(root, background="#EEEEEE")
supplieridtxt.place(anchor="nw", relwidth=0.16, relx=0.45, rely=0.8)

namelbl = tk.Label(root)
namelbl.configure(text='Name', background="#393E46")
namelbl.place(anchor="nw", relwidth=0.08, relx=0.02, rely=0.9)

nametxt = tk.Entry(root, background="#EEEEEE")
nametxt.place(anchor="nw", relwidth=0.16, relx=0.14, rely=0.9, x=0, y=0)

categorylbl = tk.Label(root, background="#393E46")
categorylbl.configure(text='Category')
categorylbl.place(anchor="nw", relwidth=0.08, relx=0.34, rely=0.9)

categorytxt = tk.Entry(root, background="#EEEEEE")
categorytxt.place(anchor="nw", relwidth=0.16, relx=0.45, rely=0.9)

showProductsbt = tk.Button(root, command=lambda: show_products(), background="#00ADB5")
showProductsbt.configure(text='Show Products')
showProductsbt.place(anchor="nw", relwidth=0.2, relx=0.7, rely=0.65)

editProductbt = tk.Button(root, background="#00ADB5", command=lambda: edit_product())
editProductbt.configure(text='Edit Product')
editProductbt.place(anchor="nw", relwidth=0.2, relx=0.7, rely=0.75)

backbt = tk.Button(root, command=lambda: go_back(username, title, eid), background="#00ADB5")
backbt.configure(text='Back')
backbt.place(anchor="nw", relwidth=0.2, relx=0.7, rely=0.94)

root.mainloop()
