from tkinter import *
from tkinter import messagebox
import os
f=open("database_proj",'a+')
root = Tk()
root.title("Book Store Managment System")
root.configure(width=1500,height=600,bg='BLACK')
var=-1

def additem():
    try:
        with open("database_proj", 'a+') as f:
            e1 = entry1.get()
            e2 = entry2.get()
            e3 = entry3.get()
            e4 = entry4.get()
            e5 = entry5.get()
            if not (e1 and e2 and e3 and e4 and e5):
                messagebox.showerror("Error", "Please fill in all fields.")
                return

            f.write('{0} {1} {2} {3} {4}\n'.format(str(e1), e2, e3, str(e4), e5))
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {e}")

def displaybookdetails(values):
    entry_list = [entry1, entry2, entry3, entry4, entry5]
    for entry, value in zip(entry_list, values):
        entry.delete(0, END)
        entry.insert(0, str(value))



def firstitem():
    global var
    var=0
    f.seek(var)
    c=f.readline()
    v=list(c.split(" "))
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry1.insert(0,str(v[0]))
    entry2.insert(0,str(v[1]))
    entry3.insert(0,str(v[2]))
    entry4.insert(0,str(v[3]))
    entry5.insert(0,str(v[4]))

def nextitem():
    global var
    var = var + 1
    f.seek(var)
    try:
        c=f.readlines()
        xyz = c[var]
        v = list(xyz.split(" "))
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry1.insert(0, str(v[0]))
        entry2.insert(0, str(v[1]))
        entry3.insert(0, str(v[2]))
        entry4.insert(0, str(v[3]))
        entry5.insert(0, str(v[4]))
    except:
        messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")
def previousitem():
        global var
        var=var-1
        f.seek(var)
        try:
            z = f.readlines()
            xyz=z[var]
            v = list(xyz.split(" "))
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)

            entry1.insert(0, str(v[0]))
            entry2.insert(0, str(v[1]))
            entry3.insert(0, str(v[2]))
            entry4.insert(0, str(v[3]))
            entry5.insert(0, str(v[4]))
        except:
            messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")


def lastitem():
    global var
    f4=open("database_proj",'r')
    x=f4.read().splitlines()
    last_line= x[-1]
    num_lines = 0
    with open("database_proj", 'r') as f8:
        for line in f8:
            num_lines += 1
    var=num_lines-1
    print(last_line)
    try:
        v = list(last_line.split(" "))
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)

        entry1.insert(0, str(v[0]))
        entry2.insert(0, str(v[1]))
        entry3.insert(0, str(v[2]))
        entry4.insert(0, str(v[3]))
        entry5.insert(0, str(v[4]))
    except:
        messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")


def updateitem():

    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    e5 = entry5.get()
    with open(r"database_proj") as f1, open(r"database_proj1", "w") as working:
        for line in f1:
            if str(e1) not in line:
                working.write(line)
            else:
                working.write('{0} {1} {2} {3} {4}'.format(str(e1), e2, e3, str(e4), e5))
    os.remove(r"database_proj")
    #brought to you by code-projects.org
    os.rename(r"database_proj1", r"database_proj")


def searchitem():
    i=0
    e11 = entry1.get()
    with open(r"database_proj") as working:
        for line in working:
            i=i+1
            if str(e11) in line:
                break
        try:
            v = list(line.split(" "))
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry1.insert(0, str(v[0]))
            entry2.insert(0, str(v[1]))
            entry3.insert(0, str(v[2]))
            entry4.insert(0, str(v[3]))
            entry5.insert(0, str(v[4]))
        except:
            messagebox.showinfo("Title", "error end of file")
    working.close()


def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
#fn1353
label0= Label(root,text="BOOK STORE MANAGEMENT SYSTEM ",bg="darkcyan",fg="white",font=("times", 34))
label1=Label(root,text="ENTER BOOK NAME",bg="darkcyan",relief="ridge",fg="white",font=("Times", 12),width=25)
entry1=Entry(root , font=("Times", 12))
label2=Label(root, text="ENTER BOOK PRICE",bd="2",relief="ridge",height="1",bg="darkcyan",fg="white", font=("Times", 12),width=25)
entry2= Entry(root, font=("Times", 12))
label3=Label(root, text="ENTER BOOK QUANTITY",bd="2",relief="ridge",bg="darkcyan",fg="white", font=("Times", 12),width=25)
entry3= Entry(root, font=("Times", 12))
label4=Label(root, text="ENTER BOOK CATEGORY",bd="2",relief="ridge",bg="darkcyan",fg="white", font=("Times", 12),width=25)
entry4= Entry(root, font=("Times", 12))
label5=Label(root, text="ENTER BOOK DISCOUNT",bg="darkcyan",relief="ridge",fg="white", font=("Times", 12),width=25)
entry5= Entry(root, font=("Times", 12))
button1= Button(root, text="ADD BOOK", bg="white", fg="black", width=20, font=("Times", 12),command=additem)
button2= Button(root, text="VIEW FIRST BOOK" , bg="white", fg="black", width =20, font=("Times", 12),command=firstitem)
button3= Button(root, text="VIEW NEXT BOOK" , bg="white", fg="black", width =20, font=("Times", 12), command=nextitem)
button4= Button(root, text="VIEW PREVIOUS BOOK", bg="white", fg="black", width =20, font=("Times", 12),command=previousitem)
button5= Button(root, text="VIEW LAST BOOK", bg="white", fg="black", width =20, font=("Times", 12),command=lastitem)
button6= Button(root, text="UPDATE BOOKS", bg="white", fg="black", width =20, font=("Times", 12),command=updateitem)
button7= Button(root, text="SEARCH BOOK", bg="white", fg="black", width =20, font=("Times", 12),command=searchitem)
button8= Button(root, text="CLEAR SCREEN", bg="white", fg="black", width=20, font=("Times", 12),command=clearitem)
label0.grid(columnspan=6, padx=10, pady=10)
label1.grid(row=1,column=0, sticky=W, padx=10, pady=10)
label2.grid(row=2,column=0, sticky=W, padx=10, pady=10)
label3.grid(row=3,column=0, sticky=W, padx=10, pady=10)
label4.grid(row=4,column=0, sticky=W, padx=10, pady=10)
label5.grid(row=5,column=0, sticky=W, padx=10, pady=10)
entry1.grid(row=1,column=1, padx=40, pady=10)
entry2.grid(row=2,column=1, padx=10, pady=10)
entry3.grid(row=3,column=1, padx=10, pady=10)
entry4.grid(row=4,column=1, padx=10, pady=10)
entry5.grid(row=5,column=1, padx=10, pady=10)
button1.grid(row=1,column=4, padx=40, pady=10)
button2.grid(row=2,column=4, padx=40, pady=10)
button3.grid(row=1,column=5, padx=40, pady=10)
button4.grid(row=2,column=5, padx=40, pady=10)
button5.grid(row=3,column=4, padx=40, pady=10)
button6.grid(row=3,column=5, padx=40, pady=10)
button7.grid(row=4,column=4, padx=40, pady=10)
button8.grid(row=4,column=5, padx=40, pady=10)
root.mainloop()

