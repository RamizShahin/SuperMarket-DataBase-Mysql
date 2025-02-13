import mysql
import mysql.connector as con
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import subprocess
import sys

def go_back(username, title, eid):
    root.destroy()
    if(title == 'employee'):
        subprocess.run(["python", "employee_page.py", username, title, str(eid)])
    else:
        subprocess.run(["python", "manager_page.py", username, title, str(eid)])

username = sys.argv[1]
title = sys.argv[2]
eid = int(sys.argv[3])

root = tk.Tk()
root.configure(background="#116A7B", height=200, width=200)
root.geometry("1050x600")
root.geometry("+100+20")

datatxt = ScrolledText(root, background="#ECE5C7")
datatxt.place(anchor="nw", relheight=0.6, relwidth=1.0)

sidtxt = tk.Entry(root, background="#ECE5C7")
sidtxt.place(anchor="nw", relwidth=0.16, relx=0.14, rely=0.7, x=0, y=0)

cidtxt = tk.Entry(root, background="#ECE5C7")
cidtxt.place(anchor="nw", relwidth=0.16, relx=0.45, rely=0.7, x=0, y=0)

sidlbl = tk.Label(root)
sidlbl.configure(text='saleid', background="#CDC2AE")
sidlbl.place(anchor="nw", relwidth=0.08, relx=0.02, rely=0.7)

cidlbl = tk.Label(root, background="#CDC2AE")
cidlbl.configure(text='customerid')
cidlbl.place(anchor="nw", relwidth=0.08, relx=0.34, rely=0.7)

sdatelbl = tk.Label(root, background="#CDC2AE")
sdatelbl.configure(text='time')
sdatelbl.place(anchor="nw", relwidth=0.08, relx=0.02, rely=0.85)

sdatetxt = tk.Entry(root, background="#ECE5C7")
sdatetxt.place(anchor="nw", relwidth=0.16, relx=0.14, rely=0.85)

itemsbt = tk.Button(root, command= lambda: show_sold_items(title, eid), background="#C2DEDC")
itemsbt.configure(text='show sold items')
itemsbt.place(anchor="nw", relwidth=0.2, relx=0.7, rely=0.77)

salesbt = tk.Button(root, command= lambda: show_sales(title, eid), background="#C2DEDC")
salesbt.configure(text='show sales')
salesbt.place(anchor="nw", relwidth=0.2, relx=0.7, rely=0.64)

backbt = tk.Button(root, command= lambda: go_back(username, title, eid), background="#C2DEDC")
backbt.configure(text='back')
backbt.place(anchor="nw", relwidth=0.2, relx=0.7, rely=0.9)

if(title == 'manager'):
    eidlbl = tk.Label(root, background="#CDC2AE")
    eidlbl.configure(text='employeeid')
    eidlbl.place(anchor="nw", relwidth=0.08, relx=0.34, rely=0.85)

    eidtxt = tk.Entry(root, background="#ECE5C7")
    eidtxt.place(anchor="nw", relwidth=0.16, relx=0.45, rely=0.85)

def show_sales(title, eid):
    datatxt.configure(state='normal')
    connection = con.connect(host="localhost", user="root", password="password", database="supermarket", port="3306")
    cursor = connection.cursor()
    datatxt.delete('1.0', tk.END)

    if(title == 'manager'):
        query = "select * from sales"
        try:
            if (sidtxt.get() != ''):
                query += " where saleid = %s"
                cursor.execute(query, (sidtxt.get(),))
            elif (cidtxt.get() != '' and sdatetxt.get() != ''):
                query += " where customerid = %s and time = %s"
                cursor.execute(query, (cidtxt.get(), sdatetxt.get(),))
            elif (eidtxt.get() != '' and sdatetxt.get() != ''):
                query += " where employeeid = %s and time = %s"
                cursor.execute(query, (eidtxt.get(), sdatetxt.get(),))
            elif (eidtxt.get() != '' and cidtxt.get() != ''):
                query += " where employeeid = %s and customerid = %s"
                cursor.execute(query, (eidtxt.get(), cidtxt.get(),))
            elif (cidtxt.get() != '' and sdatetxt.get() != '' and eidtxt.get() != ''):
                query += " where customerid = %s and time = %s and employeeid = %s"
                cursor.execute(query, (cidtxt.get(), sdatetxt.get(),))
            elif (eidtxt.get() != ''):
                query += " where employeeid = %s"
                cursor.execute(query, (eidtxt.get(),))
            elif (cidtxt.get() != ''):
                query += " where customerid = %s"
                cursor.execute(query, (cidtxt.get(),))
            elif (sdatetxt.get() != ''):
                query += " where time = %s"
                cursor.execute(query, (sdatetxt.get(),))
            else:
                cursor.execute(query)
        except:
            datatxt.insert(tk.INSERT, "invalid filters\n")

    else:
        query = "select * from sales where employeeid = %s"
        try:
            if (sidtxt.get() != ''):
                query += " and saleid = %s"
                cursor.execute(query, (eid, sidtxt.get(),))
            elif (cidtxt.get() != '' and sdatetxt.get() != ''):
                query += " and customerid = %s and time = %s"
                cursor.execute(query, (eid, cidtxt.get(), sdatetxt.get(),))
            elif (cidtxt.get() != ''):
                query += " and customerid = %s"
                cursor.execute(query, (eid, cidtxt.get(),))
            elif (sdatetxt.get() != ''):
                query += " and time = %s"
                cursor.execute(query, (eid, sdatetxt.get(),))
            else:
                cursor.execute(query, (eid,))
        except:
            datatxt.insert(tk.INSERT, "invalid filters\n")

    try:
        data = cursor.fetchall()
        datatxt.insert('1.0', "saleid\t\tcustomerid\t\temployeeid\t\tpayment_method\t\ttotal\t\ttime\n")
        if (len(data) != 0):
            for row in data:
                line = "\t\t".join(str(element) for element in row)
                datatxt.insert(tk.END, line + "\n")
        datatxt.configure(state='disabled')
    except:
        datatxt.insert(tk.INSERT, "couldn't fetch data!\n")
    cursor.close()
    connection.close()

def show_sold_items(title, eid):
    datatxt.configure(state='normal')
    connection = con.connect(host="localhost", user="root", password="password", database="supermarket", port="3306")
    cursor = connection.cursor()

    if(title == 'employee'):
        query = "select * from solditem where saleid in (select saleid from sales where employeeid = %s)"
        try:
            if (sidtxt.get() != ''):
                query += " and saleid = %s"
                cursor.execute(query, (eid, sidtxt.get(),))
            elif (cidtxt.get() != ''):
                query = "select * from solditem where saleid in (select saleid from sales where employeeid = %s and customerid = %s)"
                cursor.execute(query, (eid, cidtxt.get(),))
            else:
                cursor.execute(query, (eid,))
        except:
            datatxt.insert(tk.INSERT, "invalid filters\n")

    else:
        query = "select * from solditem"
        try:
            if (sidtxt.get() != ''):
                query += " where saleid = %s"
                cursor.execute(query, (sidtxt.get(),))
            elif (cidtxt.get() != '' and eidtxt.get() != ''):
                query += " where saleid in (select saleid from sales where customerid = %s and employeeid = %s)"
                cursor.execute(query, (cidtxt.get(), eidtxt.get(),))
            elif (cidtxt.get() != ''):
                query += " where saleid in (select saleid from sales where customerid = %s)"
                cursor.execute(query, (cidtxt.get(),))
            elif (eidtxt.get() != ''):
                query += " where saleid in (select saleid from sales where employeeid = %s)"
                cursor.execute(query, (eidtxt.get(),))
            else:
                cursor.execute(query)
        except:
            datatxt.insert(tk.INSERT, "invalid filters\n")

    try:
        data = cursor.fetchall()
        datatxt.delete('1.0', tk.END)
        datatxt.insert('1.0', "siid\t\tp_name\t\tpid\t\tsid\t\tquantity\t\tprice\n")
        if (len(data) != 0):
            for row in data:
                line = "\t\t".join(str(element) for element in row)
                datatxt.insert(tk.END, line)
                datatxt.insert(tk.END, "\n")
    except mysql.connector.errors.InterfaceError:
        datatxt.delete('1.0', tk.END)
        datatxt.insert('1.0', "no results found")
    finally:
        datatxt.configure(state='disabled')
        cursor.close()
        connection.close()

root.mainloop()