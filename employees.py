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

username = sys.argv[1]
title = sys.argv[2]
eid = int(sys.argv[3])

root = tk.Tk()
root.configure(background="#222831", height=200, width=200)
root.geometry("1050x600")
root.geometry("+100+20")

datatxt = ScrolledText(root, background="#ECE5C7")
datatxt.place(anchor="nw", relheight=0.6, relwidth=1.0)

eidlbl = tk.Label(root)
eidlbl.configure(text='employeeid', background="#393E46")
eidlbl.place(anchor="nw", relwidth=0.08, relx=0.02, rely=0.7)

eidtxt = tk.Entry(root, background="#EEEEEE")
eidtxt.place(anchor="nw", relwidth=0.16, relx=0.14, rely=0.7, x=0, y=0)

usernamelbl = tk.Label(root, background="#393E46")
usernamelbl.configure(text='username')
usernamelbl.place(anchor="nw", relwidth=0.08, relx=0.34, rely=0.7)

usernametxt = tk.Entry(root, background="#EEEEEE")
usernametxt.place(anchor="nw", relwidth=0.16, relx=0.45, rely=0.7, x=0, y=0)

namelbl = tk.Label(root, background="#393E46")
namelbl.configure(text='name')
namelbl.place(anchor="nw", relwidth=0.08, relx=0.02, rely=0.85)

nametxt = tk.Entry(root, background="#EEEEEE")
nametxt.place(anchor="nw", relwidth=0.16, relx=0.14, rely=0.85)

titlelbl = tk.Label(root, background="#393E46")
titlelbl.configure(text='title')
titlelbl.place(anchor="nw", relwidth=0.08, relx=0.34, rely=0.85)

titletxt = tk.Entry(root, background="#EEEEEE")
titletxt.place(anchor="nw", relwidth=0.16, relx=0.45, rely=0.85)

showEmployeesbt = tk.Button(root, command= lambda: show_employee(), background="#00ADB5")
showEmployeesbt.configure(text='show employees')
showEmployeesbt.place(anchor="nw", relwidth=0.2, relx=0.7, rely=0.64)

removeEmployeebt = tk.Button(root, background="#00ADB5", command= lambda:show_confirmation())
removeEmployeebt.configure(text='remove employee')
removeEmployeebt.place(anchor="nw", relwidth=0.2, relx=0.7, rely=0.77)

backbt = tk.Button(root, command= lambda: go_back(username, title, eid), background="#00ADB5")
backbt.configure(text='back')
backbt.place(anchor="nw", relwidth=0.2, relx=0.7, rely=0.9)

def show_employee():
    datatxt.configure(state='normal')
    connection = con.connect(host="localhost", user="root", password="password", database="supermarket", port="3306")
    cursor = connection.cursor()
    datatxt.delete('1.0', tk.END)

    query = "select employeeid,username,name,email,age,phone,title from employee"
    try:
        if(eidtxt.get() != ''):
            query += " where employeeid = " + eidtxt.get()
        elif(usernametxt.get() != ''):
            query += " where username = '" + usernametxt.get() + "'"
        elif(nametxt.get() != ''):
            query += " where name = '" + nametxt.get() + "'"
        elif(titletxt.get() != ''):
            query += " where title = '" + titletxt.get() + "'"
        cursor.execute(query)
    except:
        datatxt.insert(tk.END, "Invalid query or employee does not exist")

    try:
        data = cursor.fetchall()
        datatxt.insert('1.0', "employeeid\t\tusername\t\tname\t\temail\t\t\tage\t\tphone\t\ttitle\n")
        if (len(data) != 0):
            for row in data:
                line = str(row[0]) + "\t\t" + row[1] + "\t\t" + row[2] + "\t\t" + row[3] + "\t\t\t" + str(row[4]) + "\t\t" + row[5] + "\t\t" + row[6]
                datatxt.insert(tk.END, line + "\n")
        datatxt.configure(state='disabled')
    except:
        datatxt.insert(tk.INSERT, "couldn't fetch data!\n")
    cursor.close()
    connection.close()

def remove_employee():
    datatxt.configure(state='normal')
    connection = con.connect(host="localhost", user="root", password="password", database="supermarket", port="3306")
    cursor = connection.cursor()
    datatxt.delete('1.0', tk.END)

    query = "update employee set title = 'unemployed' where employeeid = '" + eidtxt.get() + "'"
    try:
        if(eidtxt.get() != ''):
            if(int(eidtxt.get()) == int(eid)):
                datatxt.insert(tk.END, "You cannot remove yourself")
            else:
                cursor.execute(query)
                connection.commit()
                datatxt.insert(tk.END, "employee removed successfully")
                datatxt.configure(state='disabled')
        else:
            datatxt.insert(tk.END, "employeeid field is empty or employee does not exist")
            datatxt.configure(state='disabled')
    except:
        datatxt.insert(tk.END, "Invalid query or employee does not exist")
    cursor.close()
    connection.close()

def show_confirmation():
    result = messagebox.askyesno("Confirmation", "Are you sure you want to remove employee?")
    if result:
        remove_employee()
    else:
        datatxt.configure(state='normal')
        datatxt.delete('1.0', tk.END)
        datatxt.insert(tk.END, "employee not removed")
        datatxt.configure(state='disabled')

root.mainloop()