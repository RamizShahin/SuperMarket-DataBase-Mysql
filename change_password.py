import tkinter as tk
import mysql.connector as con
import sys

def change_password():
    connection = con.connect(host="localhost", user="root", password="password", database="supermarket", port="3306")
    cursor = connection.cursor()
    query = "SELECT * FROM employee WHERE username = %s"
    cursor.execute(query, (username,))
    data = cursor.fetchall()
    if data[0][3] == oldPasstxt.get():
        if newPasstxt.get() == newPassContxt.get() and newPasstxt.get() != "":
            query = "UPDATE employee SET password = %s WHERE username = %s"
            cursor.execute(query, (newPasstxt.get(), username,))
            alarm.config(text="password changed successfully!", bg="#404040", font=("bold", 20), fg="green")
            alarm.pack()
        else:
            alarm.config(text="passwords do not match or password not specified", bg="#404040", font=("bold", 20), fg="red")
            alarm.pack()
    else:
        alarm.config(text="old password is incorrect", bg="#404040", font=("bold", 20), fg="red")
        alarm.pack()
    connection.commit()
    cursor.close()
    connection.close()

username = sys.argv[1]

root = tk.Tk()
root.configure(background="#FFE7A0", height=200, width=200)
root.geometry("500x400")

oldPasslb = tk.Label(root)
oldPasslb.configure(background="#00C4FF", text='old password')
oldPasslb.place(anchor="nw", relheight=0.1, relwidth=0.25, relx=0.25, rely=0.2)

newPasslb = tk.Label(root)
newPasslb.configure(background="#00C4FF", text='new password')
newPasslb.place(anchor="nw", relheight=0.1, relwidth=0.25, relx=0.25, rely=0.4)

newPassConlb = tk.Label(root)
newPassConlb.configure(background="#00C4FF", justify="left", text='Confirm password')
newPassConlb.place(anchor="nw", relheight=0.1, relwidth=0.25, relx=0.25, rely=0.6)

oldPasstxt = tk.Entry(root)
oldPasstxt.configure(background="#FFF5B8", show="*")
oldPasstxt.place(anchor="nw", relheight=0.1, relwidth=0.4, relx=0.501, rely=0.2)

newPasstxt = tk.Entry(root)
newPasstxt.configure(background="#FFF5B8", show="*")
newPasstxt.place(anchor="nw", relheight=0.1, relwidth=0.4, relx=0.501, rely=0.4)

newPassContxt = tk.Entry(root)
newPassContxt.configure(background="#FFF5B8", show="*")
newPassContxt.place(anchor="nw", relheight=0.1, relwidth=0.4, relx=0.501, rely=0.6)

confirmbt = tk.Button(root)
confirmbt.configure(background="#30A2FF", default="normal", state="normal", text='confirm', command= lambda: change_password())
confirmbt.place(anchor="nw", relheight=0.1, relwidth=0.3, relx=0.4, rely=0.8)

alarm = tk.Label(root)
alarm.configure(background="#FFE7A0")
alarm.pack(fill="x", side="top")

root.mainloop()