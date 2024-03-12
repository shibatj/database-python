import sqlite3

conn = sqlite3.connect('member.sqlite3')
c=conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS member(
           ID INTEGER PRIMARY KEY AUTOINCREMENT,
           membercode TEXT,
           fullname TEXT,
           tel TEXT,
           usertype TEXT,
           point INTEGER)""")

def insert_member (membercode,fullname,tel,usertype,point):
    with conn:
        command = 'INSERT INTO member VALUES(?,?,?,?,?,?)'
        c.execute(command,(None,membercode,fullname,tel,usertype,point))
    conn.commit()
    print("SAVE!!!")

def delete_member(ID):
    with conn:
        command = 'DELETE FROM member WHERE ID =(?)'
        c.execute(command,([ID]))
        conn.commit()
        print("DELETED!!!")

def update_member(ID,field,newvalue):
    with conn:
        command = 'UPDATE member SET {} = (?) WHERE ID=(?)'.format(field)
        c.execute(command,([newvalue,ID]))
        conn.commit()
        print("UPDATED!!!")

def view_member():
    with conn:
        command = 'SELECT * FROM member'
        c.execute(command)
        result = c.fetchall()
        return result

# insert_member('M-002','Phanuwat1','08455555','SUPER-VIP',50)
# delete_member(2)
# update_member(1,'fullname','Prayut')
# show = view_member()
# print(show[0])


# import tkinter as tk
# from tkinter import ttk
# import sqlite3

# conn = sqlite3.connect('member.sqlite3')
# c = conn.cursor()

# # Functions to interact with the database
# def insert_member():
#     membercode = entry_membercode.get()
#     fullname = entry_fullname.get()
#     tel = entry_tel.get()
#     usertype = entry_usertype.get()
#     point = entry_point.get()

#     with conn:
#         command = 'INSERT INTO member VALUES(NULL,?,?,?,?,?)'
#         c.execute(command, (membercode, fullname, tel, usertype, point))
#         conn.commit()
#         print("Data inserted!")

# def view_data():
#     c.execute('SELECT * FROM member')
#     data = c.fetchall()
#     for index, row in enumerate(data):
#         text_box.insert(tk.END, f"ID: {row[0]}, Member Code: {row[1]}, Full Name: {row[2]}, Telephone: {row[3]}, User Type: {row[4]}, Point: {row[5]}\n")

#     for record in treeview.get_children():
#         treeview.delete(record)
    
#     for row in data:
#         treeview.insert("", "end", values=row)
#     print("Data displayed!")


# def delete_member(ID):
#     with conn:
#         command = 'DELETE FROM member WHERE ID =(?)'
#         c.execute(command,([ID]))
#         conn.commit()
#         print("DELETED!!!")

# # GUI setup
# root = tk.Tk()
# root.title("Insert Data")

# label_membercode = tk.Label(root, text="Member Code:")
# label_membercode.grid(row=0, column=0)
# entry_membercode = tk.Entry(root)
# entry_membercode.grid(row=0, column=1)

# label_fullname = tk.Label(root, text="Full Name:")
# label_fullname.grid(row=1, column=0)
# entry_fullname = tk.Entry(root)
# entry_fullname.grid(row=1, column=1)

# label_tel = tk.Label(root, text="Telephone:")
# label_tel.grid(row=2, column=0)
# entry_tel = tk.Entry(root)
# entry_tel.grid(row=2, column=1)

# label_usertype = tk.Label(root, text="User Type:")
# label_usertype.grid(row=3, column=0)
# entry_usertype = tk.Entry(root)
# entry_usertype.grid(row=3, column=1)

# label_point = tk.Label(root, text="Point:")
# label_point.grid(row=4, column=0)
# entry_point = tk.Entry(root)
# entry_point.grid(row=4, column=1)

# insert_button = tk.Button(root, text="Insert Data", command=insert_member)
# insert_button.grid(row=5, columnspan=2)

# entry_membercode.delete(0, tk.END)
# entry_fullname.delete(0, tk.END)
# entry_tel.delete(0, tk.END)
# entry_usertype.delete(0, tk.END)
# entry_point.delete(0, tk.END)

# text_box = tk.Text(root, height=10, width=50)

# view_button = tk.Button(root, text="View Data", command=view_data)
# view_button.grid(row=9, columnspan=2)

# columns = ('ID', 'Member Code', 'Full Name', 'Telephone', 'User Type', 'Point')
# treeview = ttk.Treeview(root, columns=columns, show='headings')
# treeview.grid(row=6, column=1, columnspan=2)


# label_delete = tk.Label(root, text="Enter ID to Delete:")
# label_delete.grid(row=0, column=2)
# entry_delete = tk.Entry(root)
# entry_delete.grid(row=1, column=2)

# delete_button = tk.Button(root, text="Delete", command=delete_member)
# delete_button.grid(row=3, column=2)


# root.mainloop()