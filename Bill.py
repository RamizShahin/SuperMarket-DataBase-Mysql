# import datetime
import tkinter as tk
import mysql.connector
import mysql.connector as con
from tkinter import font
from tkinter import ttk


root = tk.Tk()
root.configure(background="#C0C0C0", height=200, width=200)
root.geometry("600x580")

connection = con.connect(host="localhost", user="root", password="password", database="supermarket")
cursor = connection.cursor()
query ="SELECT saleID FROM sales ORDER BY saleID DESC LIMIT 1"
cursor.execute(query)
data = cursor.fetchall()
saleID=data[0][0]
connection.commit()
cursor.close()
connection.close()


connection = con.connect(host="localhost", user="root", password="password", database="supermarket")
cursor = connection.cursor()
query ="SELECT customerID,total,payment_method,time FROM sales where saleID="+str(saleID)
cursor.execute(query)
data = cursor.fetchall()
cstomerID=data[0][0]
total=data[0][1]
pay=data[0][2]
date=data[0][3]
connection.commit()
cursor.close()
connection.close()

connection = con.connect(host="localhost", user="root", password="password", database="supermarket")
cursor = connection.cursor()
query ="SELECT name FROM customers where customerID="+str(cstomerID)
cursor.execute(query)
data = cursor.fetchall()
name=data[0][0]
connection.commit()
cursor.close()
connection.close()



font2 = font.Font(family="Arial", size=13)

font = font.Font(family="Arial", weight="bold", size=18)
welcome = tk.Label(root)
welcome.configure(text="welcome to khayyatt supermarket",background="#00C4FF",font=font)
welcome.pack(anchor="n")


style=ttk.Style()
style.theme_use("clam")
style.configure("Custom.Treeview",background="silver",rowheight=35,foreground="black",fieldbackground="silver")
style.map("Treeview",background=[("selected","blue")])
table = ttk.Treeview(style="Custom.Treeview")
table.place(x=297,y=90)
table.configure(height=10)

table.tag_configure("heading",background="red",foreground="white")
table["columns"] = ("PRODUCT NAME", "QUANTITY", "PRICE")
table.column("#0",width=0)
table.column("PRODUCT NAME", width=100)
table.column("QUANTITY", width=100)
table.column("PRICE", width=100)

table.heading("#0",anchor="n",text="")
table.heading("PRODUCT NAME", anchor="nw",text="PRODUCT NAME")
table.heading("QUANTITY",anchor="nw", text="QUANTITY")
table.heading("PRICE", anchor="nw", text="PRICE")
style = ttk.Style()
style.configure("table.Heading", background="gray",)

connection = mysql.connector.connect(host="localhost", user="root",
password="password", database="supermarket")

cursor = connection.cursor()
query="select productName,quantity,price from solditem where saleID="+str(saleID)
cursor.execute(query)
data = cursor.fetchall()
cursor.close()
connection.close()
for item in table.get_children():
        table.delete(item)
for row in data:
        table.insert("", tk.END, values=row)

background="#00C4FF"
total = tk.Label(root,text="Total PRICE = "+str(total))
total.configure(background="#00C4FF",font=font2)
total.place(x=0,y=160)

payment = tk.Label(root,text="PAYMENT METHOD = "+pay)
payment.configure(background="#00C4FF",font=font2)
payment.place(x=0,y=200)

date = tk.Label(root,text="DATE= "+str(date))
date.configure(background="#00C4FF",font=font2)
date.place(x=0,y=240)

saleid = tk.Label(root,text="SALE NUMBER= "+str(saleID))
saleid.configure(background="#00C4FF",font=font2)
saleid.place(x=0,y=275)
customer = tk.Label(root,text="CUSTOMER NUMBER="+str(cstomerID))
customer.configure(background="#00C4FF",font=font2)
customer.place(x=0,y=310)

thank = tk.Label(root,text="THANK YOU !! SEE YOU AGAIN")
thank.configure(background="#00C4FF",font=("Arial",27))
thank.place(x=0,y=500)



info = tk.Label(root,text="INFORMATION : ")
info.configure(background="#00C4FF",font=font)
info.place(x=0,y=90)





root.mainloop()

