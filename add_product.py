import mysql.connector as con
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.configure(background="#F2BE22", height=200, width=200)
root.geometry("850x650")

name_lbl = tk.Label(root)
name_lbl.configure(background="#22A699", text='Name')
name_lbl.place(anchor="nw", relwidth=0.1, relx=0.05, rely=0.2)

name_txt = tk.Entry(root)
name_txt.configure(background="#F29727")
name_txt.place(anchor="nw", relx=0.16, rely=0.2, x=0, y=0, relwidth=0.3)

unit_lbl = tk.Label(root)
unit_lbl.configure(background="#22A699", text='Unit')
unit_lbl.place(anchor="nw", relwidth=0.1, relx=0.54, rely=0.2)

unit_txt = tk.Entry(root)
unit_txt.configure(background="#F29727")
unit_txt.place(anchor="nw", relx=0.65, rely=0.2, x=0, y=0, relwidth=0.3)

quantity_lbl = tk.Label(root)
quantity_lbl.configure(background="#22A699", text='Quantity')
quantity_lbl.place(anchor="nw", relwidth=0.1, relx=0.05, rely=0.4)

quantity_txt = tk.Entry(root)
quantity_txt.configure(background="#F29727")
quantity_txt.place(anchor="nw", relx=0.16, rely=0.4, x=0, y=0, relwidth=0.3)

category_lbl = tk.Label(root)
category_lbl.configure(background="#22A699", text='Category')
category_lbl.place(anchor="nw", relwidth=0.1, relx=0.54, rely=0.4)

category_txt = tk.Entry(root)
category_txt.configure(background="#F29727")
category_txt.place(anchor="nw", relx=0.65, rely=0.4, x=0, y=0, relwidth=0.3)

supplier_id_lbl = tk.Label(root)
supplier_id_lbl.configure(background="#22A699", text='Supplier ID')
supplier_id_lbl.place(anchor="nw", relwidth=0.1, relx=0.05, rely=0.6)

supplier_id_txt = tk.Entry(root)
supplier_id_txt.configure(background="#F29727")
supplier_id_txt.place(anchor="nw", relx=0.16, rely=0.6, x=0, y=0, relwidth=0.3)

price_lbl = tk.Label(root)
price_lbl.configure(background="#22A699", text='Price')
price_lbl.place(anchor="nw", relwidth=0.1, relx=0.54, rely=0.6)

price_txt = tk.Entry(root)
price_txt.configure(background="#F29727")
price_txt.place(anchor="nw", relx=0.65, rely=0.6, x=0, y=0, relwidth=0.3)

add_product_bt = tk.Button(root)
add_product_bt.configure(background="#F24C3D", text='Add Product', command=lambda: add_product())
add_product_bt.place(anchor="nw", relheight=0.1, relwidth=0.2, relx=0.4, rely=0.8)

alarm = tk.Label(root)
alarm.configure(background="#F2BE22", justify="center")
alarm.place(anchor="nw", relheight=0.1, relwidth=1, x=0, y=0)

def add_product():
    connection = con.connect(host='localhost', database='supermarket', user='root', password='password', port='3306')
    cursor = connection.cursor()

    query = "INSERT INTO products (name, quantity, category, supplierID, price, unit) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (name_txt.get(), quantity_txt.get(), category_txt.get(), supplier_id_txt.get(), price_txt.get(), unit_txt.get())

    if (
        name_txt.get() == ''
        or quantity_txt.get() == ''
        or category_txt.get() == ''
        or supplier_id_txt.get() == ''
        or price_txt.get() == ''
        or unit_txt.get() == ''
    ):
        messagebox.showerror("Error", "Please fill all the fields")
    else:
        try:
            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Success", "Product added successfully")
        except con.Error as error:
            messagebox.showerror("Error", f"Failed to add product: {error}")

    cursor.close()
    connection.close()

root.mainloop()
