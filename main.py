import mysql.connector as con
import tkinter as tk
import subprocess

def open_manager_page(user, title, eid):
    root.destroy()
    subprocess.run(["python", "manager_page.py", user, title, str(eid)])

def open_employee_page(user, title, eid):
    root.destroy()
    subprocess.run(["python", "employee_page.py", user, title, str(eid)])

root = tk.Tk()
root.geometry('1050x600')
root.configure(bg="#404040")
root.geometry("+100+20")

image1 = tk.PhotoImage(file="supermarket.png")
background_label = tk.Label(root, image=image1, bg="#404040")
background_label.place(anchor="nw", relx=0.05, rely=0.16, x=0, y=0)

labelLogin = tk.Label(text="LOG IN", bg="#404040", font=("bold", 30), fg="white")
labelLogin.place(anchor="nw", relheight=0.1, relwidth=0.2, relx=0.67, rely=0.35)

labelUsername = tk.Label(text="USERNAME", font=("Helvetica", 12), bg="#404040", fg="white")
labelUsername.place(anchor="nw", relheight=0.04, relwidth=0.1, relx=0.67, rely=0.5)

labelPassword = tk.Label(text="PASSWORD", font=("Helvetica", 12), bg="#404040", fg="white")
labelPassword.place(anchor="nw", relheight=0.04, relwidth=0.1, relx=0.67, rely=0.6)

entry1 = tk.Entry(root, bd=2, fg="black", font=("dark bold", 20))
entry1.place(anchor="nw", relheight=0.04, relwidth=0.15, relx=0.78, rely=0.5)

entry2 = tk.Entry(root, bd=2, font=("dark bold", 20), show="*")
entry2.place(anchor="nw", relheight=0.04, relwidth=0.15, relx=0.78, rely=0.6)

button = tk.Button(text="lets go", cursor="hand2",command =lambda: confirmLogIn() ,bg="#9BABB8", font=("dark bold", 20))
button.place(anchor="nw", relheight=0.1, relwidth=0.1, relx=0.73, rely=0.7)

alarm = tk.Label(root, text="")

def confirmLogIn():
    connection = con.connect(host="localhost", user="root", password="password", database="supermarket", port="3306")
    cursor = connection.cursor()
    query = "SELECT * FROM employee WHERE username = %s"
    cursor.execute(query, (entry1.get(),))
    data = cursor.fetchall()
    if entry1.get() == "" or entry2.get() == "" or len(data[0]) == 0:
        alarm.config(text="username not found or password incorrect!", bg="#404040", font=("bold", 20), fg="red")
        alarm.pack()
    else:
        title = data[0][7]
        eid = data[0][0]
        if data[0][7] == "manager" and data[0][3] == entry2.get():
            open_manager_page(entry1.get(), title, eid)
        elif data[0][7] == "employee" and data[0][3] == entry2.get():
            open_employee_page(entry1.get(), title, eid)
        elif data[0][7] == "manager" and data[0][3] != entry2.get():
            alarm.config(text="username not found or password incorrect!", bg="#404040", font=("bold", 20), fg="red")
            alarm.pack()
        elif data[0][7] == "employee" and data[0][3] != entry2.get():
            alarm.config(text="username not found or password incorrect!", bg="#404040", font=("bold", 20), fg="red")
            alarm.pack()
        else:
            alarm.config(text="user title unknown!", bg="#404040", font=("bold", 20), fg="red")
            alarm.pack()

    connection.commit()
    cursor.close()
    connection.close()

def activate_button(event):
    button.invoke()

root.bind("<Return>", activate_button)

root.mainloop()