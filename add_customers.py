import tkinter as tk
import mysql.connector as con
import sys

root2 = tk.Tk()
root2.configure(background="#FFE7A0", height=200, width=200)
root2.geometry("500x400")
name = tk.Label(root2)
name.configure(background="#00C4FF", text='NAME')
name.place(anchor="nw", relheight=0.1, relwidth=0.25, relx=0.25, rely=0.2)
phone = tk.Label(root2)
phone.configure(background="#00C4FF", text='PHONE')
phone.place(anchor="nw", relheight=0.1, relwidth=0.25, relx=0.25, rely=0.4)

email = tk.Label(root2)
email.configure(background="#00C4FF", justify="left", text='EMAIL')
email.place(anchor="nw", relheight=0.1, relwidth=0.25, relx=0.25, rely=0.6)

nameEntry = tk.Entry(root2)
nameEntry.configure(background="#FFF5B8")
nameEntry.place(anchor="nw", relheight=0.1, relwidth=0.4, relx=0.501, rely=0.2)

phoneEntry = tk.Entry(root2)
phoneEntry.configure(background="#FFF5B8")
phoneEntry.place(anchor="nw", relheight=0.1, relwidth=0.4, relx=0.501, rely=0.4)

emailEntry = tk.Entry(root2)
emailEntry.configure(background="#FFF5B8")
emailEntry.place(anchor="nw", relheight=0.1, relwidth=0.4, relx=0.501, rely=0.6)

confirmbt = tk.Button(root2)
confirmbt.configure(background="#30A2FF", default="normal", state="normal", text='confirm',
                    command=lambda: add_Customer())
confirmbt.place(anchor="nw", relheight=0.1, relwidth=0.3, relx=0.4, rely=0.8)


def exit():
    root2.destroy()


exitt = tk.Button(root2, width=10, height=1)
exitt.configure(background="#30A2FF", default="normal", command=lambda: exit(), state="normal", text='exit')
exitt.place(x=0, y=325)


def add_Customer():
    done = tk.Label(root2)
    connection = con.connect(host="localhost", user="root", password="password", database="supermarket")
    cursor = connection.cursor()
    query = "INSERT INTO customers (name,phone, email) VALUES ('" + nameEntry.get() + "','" + phoneEntry.get() + "','" + emailEntry.get() + "')"
    if nameEntry.get() == "" or phoneEntry.get() == "" or emailEntry.get() == "":
        done.configure(background="#00C4FF", text='make sure to provide all data fields')
        done.place(x=200, y=20)
    else:
        query2 = "SELECT * FROM customers WHERE phone = '" + phoneEntry.get() + "'"
        cursor.execute(query2)
        result = cursor.fetchall()
        if len(result) > 0:
            done.configure(background="#00C4FF", text='this phone number already exists')
            done.place(x=200, y=20)
        else:
            print(query)
            cursor.execute(query)
            connection.commit()
            done.configure(background="#00C4FF", text='the customer has been added')
            done.place(x=200, y=20)
            print("the Query executed successfully!")


alarm = tk.Label(root2)
alarm.configure(background="#FFE7A0")
alarm.pack(fill="x", side="top")
root2.mainloop()
