import mysql
import mysql.connector as con
import tkinter as tk

root = tk.Tk()
root.configure(background="#F2BE22", height=200, width=200)
root.geometry("850x650")

usernamelbl = tk.Label(root)
usernamelbl.configure(background="#22A699", text='username')
usernamelbl.place(anchor="nw", relwidth=0.1, relx=0.05, rely=0.2)

usernametxt = tk.Entry(root)
usernametxt.configure(background="#F29727")
usernametxt.place(anchor="nw", relx=0.16, rely=0.2, x=0, y=0, relwidth=0.3)

namelbl = tk.Label(root)
namelbl.configure(background="#22A699", text='name')
namelbl.place(anchor="nw", relwidth=0.1, relx=0.54, rely=0.2)

nametxt = tk.Entry(root)
nametxt.configure(background="#F29727")
nametxt.place(anchor="nw", relx=0.65, rely=0.2, x=0, y=0, relwidth=0.3)

passwordlbl = tk.Label(root)
passwordlbl.configure(background="#22A699", text='password')
passwordlbl.place(anchor="nw", relwidth=0.1, relx=0.05, rely=0.4)

passwordtxt = tk.Entry(root)
passwordtxt.configure(background="#F29727", show="•")
passwordtxt.place(anchor="nw", relx=0.16, rely=0.4, x=0, y=0, relwidth=0.3)

emaillbl = tk.Label(root)
emaillbl.configure(background="#22A699", text='email')
emaillbl.place(anchor="nw", relwidth=0.1, relx=0.54, rely=0.4)

emailtxt = tk.Entry(root)
emailtxt.configure(background="#F29727")
emailtxt.place(anchor="nw", relx=0.65, rely=0.4, x=0, y=0, relwidth=0.3)

phonelbl = tk.Label(root)
phonelbl.configure(background="#22A699", text='phone')
phonelbl.place(anchor="nw", relwidth=0.1, relx=0.05, rely=0.6)

phonetxt = tk.Entry(root)
phonetxt.configure(background="#F29727")
phonetxt.place(anchor="nw", relx=0.16, rely=0.6, x=0, y=0, relwidth=0.3)

agelbl = tk.Label(root)
agelbl.configure(background="#22A699", text='age')
agelbl.place(anchor="nw", relwidth=0.1, relx=0.54, rely=0.6)

agetxt = tk.Entry(root)
agetxt.configure(background="#F29727")
agetxt.place(anchor="nw", relx=0.65, rely=0.6, x=0, y=0, relwidth=0.3)

addEmployeebt = tk.Button(root)
addEmployeebt.configure(background="#F24C3D", text='Add Employee', command=lambda: add_employee())
addEmployeebt.place(anchor="nw", relheight=0.1, relwidth=0.2, relx=0.4, rely=0.8)

alarm = tk.Label(root)
alarm.configure(background="#F2BE22", justify="center")
alarm.place(anchor="nw", relheight=0.1, relwidth=1, x=0, y=0)

def add_employee():
    connection = con.connect(host='localhost', database='supermarket', user='root', password='password', port='3306')
    cursor = connection.cursor()

    query = "INSERT INTO employee (username, name, password, email, phone, age, title) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (usernametxt.get(), nametxt.get(), passwordtxt.get(), emailtxt.get(), phonetxt.get(), agetxt.get(), "employee")

    if usernametxt.get() == '' or nametxt.get() == '' or passwordtxt.get() == '' or emailtxt.get() == '' or phonetxt.get() == '' or agetxt.get() == '':
        alarm.configure(text="Please fill the empty fields", fg="red", font=("bold", 20))
    else:
        cursor.execute("select * from employee")
        temprows = cursor.fetchall()
        try:
            flag = 1
            for row in temprows:
                if usernametxt.get() in row:
                    flag = 0
                    alarm.configure(text="Username already exists", fg="red", font=("bold", 20))
                elif emailtxt.get() in row:
                    flag = 0
                    alarm.configure(text="Email already exists", fg="red", font=("bold", 20))
                elif phonetxt.get() in row:
                    flag = 0
                    alarm.configure(text="Phone already exists", fg="red", font=("bold", 20))

            if flag == 1:
                cursor.execute(query, values)
                connection.commit()
                alarm.configure(text="Employee added successfully", fg="green", font=("bold", 20))
        except mysql.connector.Error as error:
            alarm.configure(text="Failed to add employee {}".format(error), fg="red", font=("bold", 20))

        cursor.close()
        connection.close()

root.mainloop()