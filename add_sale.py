import datetime
import tkinter as tk

import mysql.connector
import mysql.connector as con
import sys
import subprocess
root = tk.Tk()
root.configure(background="#FFE7A0", height=200, width=200)
root.geometry("600x580")
eid= sys.argv[1]
check=True
saleID=0
def add_product():
    done.place(x=2000, y=4300)
    global check
    check=False
    connection = con.connect(host="localhost", user="root", password="password", database="supermarket")
    cursor = connection.cursor()
    query = "INSERT INTO sales (customerID,employeeID, payment_method,total,time) VALUES ('" + str(
        customerEntry.get()) + "','" + (
                str(eid)) + "','" + str(paymentEntry.get()) + "','" + str(totalEntry.cget("text")) + "','" + str(
        datetime.date.today()) + "')"
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    connection = con.connect(host="localhost", user="root", password="password", database="supermarket")
    cursor = connection.cursor()
    query2 = "SELECT saleID FROM sales ORDER BY saleID DESC LIMIT 1"
    cursor.execute(query2)
    data = cursor.fetchall()
    global saleID
    saleID = data[0][0]
    connection.commit()
    cursor.close()
    connection.close()

    connection = con.connect(host="localhost", user="root", password="password", database="supermarket")
    cursor = connection.cursor()
    query2="SELECT saleID FROM sales ORDER BY saleID DESC LIMIT 1"
    cursor.execute(query2)
    data = cursor.fetchall()
    saleID=data[0][0]
    connection.commit()
    cursor.close()
    connection.close()
    subprocess.run(["python","add_product_in_sale.py",str(saleID)])



customerID = tk.Label(root)
customerID.configure(background="#00C4FF", text='CUSTOMERID')
customerID.place(anchor="nw", relheight=0.1, relwidth=0.25, relx=0.25, rely=0.02)

payment = tk.Label(root)
payment.configure(background="#00C4FF", text='PAYMENT METHOD')
payment.place(anchor="nw", relheight=0.1, relwidth=0.25, relx=0.25, rely=0.21)

def revelPrice():
    done.place(x=2000, y=4300)
    print(check)
    if check:
        totalEntry.configure(text="0")
    else:
        connection = con.connect(host="localhost", user="root", password="password", database="supermarket")
        cursor = connection.cursor()
        query ="SELECT sum(price) FROM solditem where saleID="+str(saleID)
        cursor.execute(query)
        data = cursor.fetchall()
        totalPrice = data[0][0]
        if totalPrice is None:
            pass
        else:
            totalEntry.configure(text="" + str(totalPrice))
        connection.commit()
        cursor.close()
        connection.close()


total = tk.Button(root)
total.configure(background="#00C4FF", justify="left",command=lambda: revelPrice() ,text='TOTAL PRICE')
total.place(anchor="nw", relheight=0.1, relwidth=0.25, relx=0.25, rely=0.57)

customerEntry = tk.Entry(root)
customerEntry.configure(background="#FFF5B8")
customerEntry.place(anchor="nw", relheight=0.1, relwidth=0.4, relx=0.501, rely=0.02)

paymentEntry = tk.Entry(root)
paymentEntry.configure(background="#FFF5B8")
paymentEntry.place(anchor="nw", relheight=0.1, relwidth=0.4, relx=0.501, rely=0.21)

totalEntry = tk.Label(root)
totalEntry.configure(background="#00C4FF",text="0")
totalEntry.place(anchor="nw", relheight=0.1, relwidth=0.4, relx=0.501, rely=0.57)

confirmbt = tk.Button(root)
confirmbt.configure(background="#30A2FF", default="normal",command=lambda:add_sale(), state="normal", text='confirm')
confirmbt.place(anchor="nw", relheight=0.1, relwidth=0.3, relx=0.4, rely=0.89)
addProduct = tk.Button(root)
addProduct.configure(background="#30A2FF", default="normal",command =lambda : add_product(), state="normal", text='ADD PRODUCTS')
addProduct.place(anchor="nw", relheight=0.1, relwidth=0.3, relx=0.25, rely=0.41)
done = tk.Label(root)
def add_sale():
   if customerEntry.get() == "" and paymentEntry.get()=="":
       done.configure(background="#00C4FF", text='make sure to provide all data feilds', font=("Arial", 18))
       done.place(x=150,y=430)
   elif check :
       done.configure(background="#00C4FF", text='make sure to add products to your sale', font=("Arial", 18))
       done.place(x=150,y=430)

   else:
       connection = con.connect(host="localhost", user="root", password="password", database="supermarket")
       cursor = connection.cursor()
       try:
           query = "SELECT sum(price) FROM solditem where saleID=" + str(saleID)
           cursor.execute(query)
       except mysql.connector.Error as error :
           print(f"Error executing MySQL query: {error}")
       data = cursor.fetchall()
       connection.commit()
       cursor.close()
       connection.close()
       connection = con.connect(host="localhost", user="root", password="password", database="supermarket")
       cursor = connection.cursor()

       try:
           query="UPDATE sales SET total=0"+str(data[0][0]) +" WHERE saleID=" + str(saleID)
           if data[0][0] == None:
                query = "UPDATE sales SET total=0"+ " WHERE saleID=" + str(saleID)
           cursor.execute(query)
       except mysql.connector.Error as error :
                print(f"Error executing MySQL query: {error}")
       connection.commit()
       cursor.close()
       connection.close()
       done.configure(background="#00C4FF", text='sale has been added!!', font=("Arial", 18))
       done.place(x=200,y=430)
       root.after(1000, root.destroy)
alarm = tk.Label(root)
alarm.configure(background="#FFE7A0")
alarm.pack(fill="x", side="top")
root.mainloop()