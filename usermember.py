from tkinter import *
from tkinter import ttk, messagebox
import main as db

root = Tk()
root.title("Register")
root.geometry("1200x800")

cf1 = Frame(root)
cf1.place(x=50,y=50)

v_membercode = StringVar()
v_membercode.set("M-1001")

L = Label(root,text="MemberCode : ", font=(None,16)).place(x=50,y=10)
Lcode = Label (root,textvariable=v_membercode, font=(None,16)).place(x=200,y=10)

v_name = StringVar()
l_name = ttk.Label(cf1,text="Fullname", font=(None,16))
l_name.pack()
e_name = ttk.Entry(cf1,textvariable=v_name, font=(None,16))
e_name.pack()

v_Tel = StringVar()
l_Tel = ttk.Label(cf1,text="Tel", font=(None,16))
l_Tel.pack()
e_Tel = ttk.Entry(cf1,textvariable=v_Tel, font=(None,16))
e_Tel.pack()


l_type = ttk.Label(cf1,text="User Type", font=(None,16))
l_type.pack()
options = ["Normal", "Bronze", "SIlver", "Gold", "Platinum", "Diamond", "Immortal", "Radiant"]
Click = StringVar()
Click.set(options[0])
dropdown = OptionMenu(cf1,Click,*options)
dropdown.pack()

v_id = IntVar()
v_point = StringVar()
l_point = ttk.Label(cf1,text="Point", font=(None,16))
l_point.pack()
e_point = ttk.Entry(cf1,textvariable=v_point, font=(None,16))
e_point.pack()

#######################################################################################################################################

cf2 = Frame(root)
cf2.place(x=500, y=50)

header = ['ID', 'MemberCode', 'FullName', 'Telephone', 'UserType', 'Point']
hwidth = [50,100,200,100,100,100]
table = ttk.Treeview(cf2, columns=header, show='headings', height=15, )
table.pack()

for hd,hw in zip(header,hwidth):
    table.heading(hd,text=hd)
    table.column(hd,width=hw)


last_member=''
allmember = {}
def UpdateTable():
    global last_member
    fr = db.view_member()
    table.delete(*table.get_children())
    for row in fr:
        table.insert('',0,value=row)
        code = row[0]
        allmember[code] = list(row)
    last_member = row[1]
    next_membercode = int(last_member.split('-')[1])+1
    v_membercode.set('M-{}'.format(next_membercode))

def SaveMamber():
    code = v_membercode.get()
    name = v_name.get()
    tel = v_Tel.get()
    type = Click.get()
    point = v_point.get()
    db.insert_member(code,name,tel,type,point)
    UpdateTable()
    v_name.set('')
    v_Tel.set('')
    v_point.set('')


B_Save = ttk.Button(cf1,text="Save",command=SaveMamber)
B_Save.pack()


def UpdateMember(event):
    select = table.selection()
    ID = table.item(select)['values'][0]
    v_id.set(ID)
    memberinfo = allmember[ID]
    v_membercode.set(memberinfo[1])
    v_name.set(memberinfo[2])
    v_Tel.set(memberinfo[3])
    Click.set(memberinfo[4])
    v_point.set(memberinfo[5])
    B_Save.state(['disabled'])
    B_E.state(['!disabled'])
table.bind('<Double-1>', UpdateMember)

def EditMember():
    ID = v_id.get()
    allmember[ID][2] = v_name.get()
    allmember[ID][3] = v_Tel.get()
    allmember[ID][4] = Click.get()
    allmember[ID][5] = v_point.get()
    db.update_member(ID,'fullname',v_name.get())
    db.update_member(ID,'tel',v_Tel.get())
    db.update_member(ID,'usertype',Click.get())
    db.update_member(ID,'point',v_point.get())
    UpdateTable()
    B_Save.state(['!disabled'])
    B_E.state(['disabled'])
    v_name.set('')
    v_Tel.set('')
    v_point.set('')

B_E = ttk.Button(cf1,text='Edit',command=EditMember)
B_E.place(x=170,y=233)

def deleteMember(event):
    check = messagebox.askyesno('Deleting','Delete Eli Bor??')
    select = table.selection()
    data = table.item(select)['values']
    if check == True:
        del allmember[data[0]]
        db.delete_member(data[0])
        UpdateTable()
    else:
        pass

table.bind('<d>', deleteMember)
UpdateTable()
root.mainloop()