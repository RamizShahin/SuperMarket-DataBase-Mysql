import tkinter as tk
import mysql.connector as con
import sys
import emoji
import subprocess

def open_password_change(user):
    subprocess.run(["python", "change_password.py", user])

def logout():
    root.destroy()
    subprocess.run(["python", "main.py"])

def open_sales(username, eid, title):
    root.destroy()
    subprocess.run(["python", "sales.py", username, title, str(eid)])
def open_show_customers(username, eid, title):
    root.destroy()
    subprocess.run(["python", "show_customers.py", username, title, str(eid)])
def open_employees(username, eid, title):
    root.destroy()
    subprocess.run(["python", "employees.py", username, title, str(eid)])
def open_prodcut(username, eid, title):
    root.destroy()
    subprocess.run(["python", "product.py", username, title, str(eid)])
def add_product():
    subprocess.run(["python", "add_product.py"])
def add_customers():
    subprocess.run(["python", "add_customers.py"])
def add_employee():
    subprocess.run(["python", "add_employee.py"])
def add_sale(eid):
    subprocess.run(["python", "add_sale.py", str(eid)])
def Suppliers():
    root.destroy()
    subprocess.run(["python", "supplier.py", username, title, str(eid)])
username = sys.argv[1]
title = sys.argv[2]
eid = int(sys.argv[3])

root = tk.Tk()
root.configure(background="#27374D", cursor="arrow")
root.geometry("1050x600")
root.geometry("+100+20")

welcomelb = tk.Label(background="#DDE6ED", cursor="arrow", font=('bold', 20), justify="left", relief="flat", text=f'welcome {username} {emoji.emojize(":beaming_face_with_smiling_eyes:")}!')
welcomelb.place(anchor="nw", relheight=0.23, relwidth=1.0, relx=0.0, x=0, y=0)

addEmployeebt = tk.Button(background="#9DB2BF", text='Add Employee', command=lambda: add_employee())
addEmployeebt.place(anchor="nw", relx=0.06, rely=0.33, relwidth=0.2, relheight=0.15)

addCustomerbt = tk.Button(background="#9DB2BF", text='Add Customer', command=lambda: add_customers())
addCustomerbt.place(anchor="nw", relx=0.29, rely=0.33, relwidth=0.2, relheight=0.15)

addSalebt = tk.Button(background="#9DB2BF", text='Add Sale', command=lambda: add_sale(eid))
addSalebt.place(anchor="nw", relx=0.52, rely=0.33, relwidth=0.2, relheight=0.15)

addProductbt = tk.Button(background="#9DB2BF", text='Add Product', command=lambda: add_product())
addProductbt.place(anchor="nw", relx=0.75, rely=0.33, relwidth=0.2, relheight=0.15)

updateInvbt = tk.Button(background="#9DB2BF", text='Suppliers',command=lambda:  Suppliers())
updateInvbt.place(anchor="nw", relx=0.29, rely=0.77, relwidth=0.2, relheight=0.15)

customersbt = tk.Button(background="#9DB2BF", text='Customers', command=lambda:open_show_customers(username, eid, title))
customersbt.place(anchor="nw", relx=0.29, rely=0.55, relwidth=0.2, relheight=0.15)

employeesbt = tk.Button(background="#9DB2BF", text='Employees', command=lambda: open_employees(username, eid, title))
employeesbt.place(anchor="nw", relx=0.06, rely=0.55, relwidth=0.2, relheight=0.15)

productsbt = tk.Button(background="#9DB2BF", text='Products',command =lambda:open_prodcut(username, eid, title))
productsbt.place(anchor="nw", relx=0.75, rely=0.55, relwidth=0.2, relheight=0.15)

changePassbt = tk.Button(root, text='change password', bg="#9DB2BF", command=lambda: open_password_change(username))
changePassbt.place(anchor="nw", relx=0.52, rely=0.77, relwidth=0.2, relheight=0.15)

salesbt = tk.Button(root, text='sales', bg="#9DB2BF", command=lambda: open_sales(username, eid, title))
salesbt.place(anchor="nw", relx=0.52, rely=0.55, relwidth=0.2, relheight=0.15)

logoutbt = tk.Button(root)
logoutbt.configure(background="#9DB2BF", default="normal", state="normal", text='Log Out', command=lambda: logout())
logoutbt.place(anchor="nw", relx=0.75, rely=0.77, relwidth=0.2, relheight=0.15)

root.mainloop()