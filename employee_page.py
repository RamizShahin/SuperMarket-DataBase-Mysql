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

def add_customers():
    subprocess.run(["python", "add_customers.py"])

def add_sale(eid):
    subprocess.run(["python", "add_sale.py", str(eid)])

username = sys.argv[1]
title = sys.argv[2]
eid = int(sys.argv[3])

root = tk.Tk()
root.configure(background="#0A4D68")
root.geometry("1050x600")
root.geometry("+100+20")

welcomelb = tk.Label(root)
welcomelb.configure(background="#088395", font=('bold', 20), text=f'welcome {username} {emoji.emojize(":beaming_face_with_smiling_eyes:")}!')
welcomelb.place(anchor="nw", relheight=0.3, relwidth=1.0)

addCustomerbt = tk.Button(root)
addCustomerbt.configure(background="#00FFCA", cursor="arrow", default="normal", text='Add Customer', command=lambda: add_customers())
addCustomerbt.place(relheight=0.15, relwidth=0.2, relx=0.1, rely=0.45)

addSalebt = tk.Button(root)
addSalebt.configure(background="#00FFCA", text='Add Sale', command=lambda: add_sale(eid))
addSalebt.place(relheight=0.15, relwidth=0.2, relx=0.4, rely=0.45)

salebt = tk.Button(root, command= lambda: open_sales(username, eid, title))
salebt.configure(background="#00FFCA", text='Sales')
salebt.place(relheight=0.15, relwidth=0.2, relx=0.7, rely=0.45)

changePassbt = tk.Button(root)
changePassbt.configure(background="#00FFCA", default="normal", state="normal", text='change password', command=lambda: open_password_change(username))
changePassbt.place(relheight=0.15, relwidth=0.2, relx=0.1, rely=0.7)

logoutbt = tk.Button(root)
logoutbt.configure(background="#00FFCA", default="normal", state="normal", text='Log Out', command=lambda: logout())
logoutbt.place(relheight=0.15, relwidth=0.2, relx=0.7, rely=0.7)

root.mainloop()