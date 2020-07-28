from Tkinter import *
from tkMessageBox import *
import sqlite3
con=sqlite3.Connection('Phonebook2')
cur=con.cursor()
cur.execute('create table if not exists contact(contact_id integer PRIMARY KEY AUTOINCREMENT,fname varchar(50),mname varchar(50),lname varchar(50),comp varchar(50), addr varchar(50),city varchar(50),pin number(10),website varchar(50),dob number(15))')
cur.execute('create table if not exists phone(contact_id integer PRIMARY KEY AUTOINCREMENT,contact_type varchar(20),pno char(15))')
cur.execute('create table if not exists email(contact_id integer PRIMARY KEY AUTOINCREMENT,email_type varchar(20),m_id varchar(32))')

root1=Tk()
root1.title('Introduction')
Label(root1,text="Project Title: PHONEBOOK",font='times 20 bold',fg='#FF0033').grid(row=0,column=0)
Label(root1,text="Project of Python & Database",font='times 20 bold',fg='#EA4335').grid(row=1,column=1)
Label(root1,text="Developed By: Chandan Kumar",font='times 20 bold',fg='#4285F4').grid(row=2,column=1)
Label(root1,text="---------------------------------------------",fg='#34A853').grid(row=3,column=1)
Label(root1,text="Make mouse moment over this screen to close",font='times 10 bold',fg='Red').grid(row=3,column=1)
def close(e=1):
    root1.destroy()
root1.bind('<Motion>',close)
root1.mainloop()
root=Tk()
root.title("Phone Book")
Label(root,text="PHONEBOOK",font='roman 25 bold',fg='#123456').grid(row=0,column=1)
pb=PhotoImage(file="F:\Programming\Python\PhoneBook\PB2.gif")
Label(root,image=pb).grid(row=1,column=1)
Label(root,text="First Name",font='calibri 10').grid(row=3,column=0)
fname=Entry(root)
fname.grid(row=3,column=1)
Label(root,text="Middle Name",font='calibri 10').grid(row=4,column=0)
mname=Entry(root)
mname.grid(row=4,column=1)
Label(root,text="Last Name",font='calibri 10').grid(row=5,column=0)
lname=Entry(root)
lname.grid(row=5,column=1)
Label(root,text="Company Name",font='calibri 10').grid(row=6,column=0)
comp=Entry(root)
comp.grid(row=6,column=1)
Label(root,text="Address",font='calibri 10').grid(row=7,column=0)
addr=Entry(root)
addr.grid(row=7,column=1)
Label(root,text="City",font='calibri 10').grid(row=8,column=0)
city=Entry(root)
city.grid(row=8,column=1)
Label(root,text="Pin Code",font='calibri 10').grid(row=9,column=0)
pin=Entry(root)
pin.grid(row=9,column=1)
Label(root,text="Website URL",font='calibri 10').grid(row=10,column=0)
web=Entry(root)
web.grid(row=10,column=1)
Label(root,text="Date of Birth",font='calibri 10').grid(row=11,column=0)
dob=Entry(root)
dob.grid(row=11,column=1)
Label(root,text="Select Phone Type",font='calibri 10').grid(row=12,column=0)
v1=StringVar()
r1=Radiobutton(root,text="Office",variable=v1,value="Office")
r1.grid(row=12,column=1)
r2=Radiobutton(root,text="Home",variable=v1,value="Home")
r2.grid(row=12,column=2)
r3=Radiobutton(root,text="Mobile",variable=v1,value="Mobile")
r3.grid(row=12,column=3)

Label(root,text="Phone Number:",font='calibri 10').grid(row=13,column=0)
pno=Entry(root)
pno.grid(row=13,column=1)

Label(root,text="Select Email Type",font='calibri 10').grid(row=14,column=0)
v2=StringVar()
r4=Radiobutton(root,text="Office",variable=v2,value="Office")
r4.grid(row=14,column=1)
r5=Radiobutton(root,text="Personal",variable=v2,value="Personal")
r5.grid(row=14,column=2)

Label(root,text="Email ID",font='calibri 10').grid(row=15,column=0)
eid=Entry(root)
eid.grid(row=15,column=1)
def save(e=1):
    cur.execute('insert into contact(fname,mname,lname,comp,addr,city,pin,website,dob) values(?, ?, ?, ?, ?, ?, ?, ?, ?)',(fname.get(),mname.get(),lname.get(),comp.get(),addr.get(),city.get(),pin.get(),web.get(),dob.get()))
    cur.execute('insert into phone(contact_type, pno) values(?, ?)',(v1.get(),pno.get()))
    cur.execute('insert into email(email_type, m_id) values(?, ?)',(v2.get(),eid.get()))
    cur.execute('select * from contact')
    print cur.fetchall()
    cur.execute('select * from phone')
    print cur.fetchall()
    cur.execute('select * from email')
    print cur.fetchall()
    con.commit()
    fname.delete(first=0,last=50)
    mname.delete(first=0,last=50)
    lname.delete(first=0,last=50)
    comp.delete(first=0,last=50)
    addr.delete(first=0,last=50)
    city.delete(first=0,last=50)
    pin.delete(first=0,last=50)
    web.delete(first=0,last=50)
    dob.delete(first=0,last=50)
    pno.delete(first=0,last=50)
    eid.delete(first=0,last=50)
    r1.deselect()
    r2.deselect()
    r3.deselect()
    r4.deselect()
    r5.deselect()
    showinfo('Save','ls Successfully Saved')


Button(root,text="Save",command=save).grid(row=16,column=0)

def search(e=1):
    lst1=[]
    data=0
    root1=Tk()
    root1.title('Search')
    root1.geometry('445x550')
    Label(root1,text='Search Contacts',font='Arial 14').grid(row=0,column=2,columnspan=3)
    #Label(root1,text='',font='Arial',width=24).grid(row=1,column=1)
    ent=Entry(root1)
    ent.grid(row=1,column=2,columnspan=5)
    
    def display(data):
        def delete():
            cur.execute('delete from contact where contact_id=?',(data,))
            cur.execute('delete from phone where contact_id=?',(data,))
            cur.execute('delete from email where contact_id=?',(data,))
            con.commit()
            showinfo("Removed","Record Deleted From Phone Book")
            root1.destroy()
        def edit1():
            root1.destroy()
            edit(lst1,lst3,lst4)
        
        root1=Tk()
        lst2=['','Fisrt Name : ','Mid Name : ','Last Name : ','Company Name : ','Address : ','City : ','Pin Code : ','Website URL : ','Date of Birth : ']
        lb=Listbox(root1,height=22)
        lb.grid(row=1,column=1,columnspan=3,sticky=E+W)
        lb.configure(font='Arial 14 bold',fg='grey')
        Button(root1,text='Close',width=22,command=root1.destroy).grid(row=3,column=1)
        Button(root1,text='Edit',width=22,command=edit1).grid(row=3,column=2)
        Button(root1,text='Delete',width=22,command=delete).grid(row=3,column=3)
        cur.execute('select * from contact where contact_id=?',(data,))
        ls=cur.fetchall()
        for y in ls[0]:
            lst1.append(str(y))
        for j in range(10):
            if lst1[j]!='' and lst2[j]!='':
                line=lst2[j]+lst1[j]
                lb.insert(END,line)
        cur.execute('select * from phone where contact_id = ?',(data,))
        ls=cur.fetchall()
        lst3=[]
        if ls!=[]:
            lb.insert(END,'Phone contacts....')
            for x in ls:
                lst3.append((x[1],x[2]))
                line=x[1]+' : '+x[2]
                lb.insert(END,line)
        cur.execute('select * from email where contact_id = ?',(data,))
        ls=cur.fetchall()
        lst4=[]
        if ls!=[]:
            lb.insert(END,'Email contacts....')
            for x in ls:
                lst4.append((x[1],x[2]))
                line=x[1]+' : '+x[2]
                lb.insert(END,line)

    def open(e):
        m=e.widget
        index=int(m.curselection()[0])
        display(ls[index][0])

    #def onselect(evt):
    #    w = evt.widget
    #    index = int(w.curselection()[0])
    #    show(ls[index][0])

    #lb=Listbox(root,height=22)
    #lb.bind('<<ListboxSelect>>', onselect)
    #lb.grid(row=3,column=1,columnspan=3,sticky=W+E+N+S)
    #lb.configure(font='Arial 14 bold',fg='blue')
    lb=Listbox(root1,height='20',width='40')
    lb.bind('<<ListboxSelect>>',open)
    lb.grid(row=2,column=2,columnspan=3,sticky=W+E+N+S)
    lb.configure(font='Arial 14',fg='blue')

    def find(e=1):
        lb.delete(0,END)
        cur.execute("select fname, lname from contact where fname LIKE '%{0}%' or mname LIKE '%{1}%' or lname LIKE '%{2}%'".format(ent.get(),ent.get(),ent.get()))
        global ls
        #global ls
        #ls1=cur.fetchall()
        ls=cur.fetchall()
        #print ls
        if ls==[]:
            lb.delete(0,END)
            lb.insert(1,'No Matching Results found')
        else:
            for i in ls:
                lb.insert(END,i)

    def close_search():
        root1.destroy()
    root1.bind('<KeyPress>',find)
    Button(root1,text='Close',command=close_search).grid(row=3,column=2,padx=200)
    root1.mainloop()

Button(root,text="Search",command=search).grid(row=16,column=1)
def edit(e=1):
    print 'This Feature is not available right now'
Button(root,text="Edit",command=edit).grid(row=16,column=2)
def closemain(e=1):
    root.destroy()
Button(root,text='Close',command=closemain).grid(row=16,column=3)
root.mainloop()