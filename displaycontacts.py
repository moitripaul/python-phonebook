from tkinter import *
from tkinter import messagebox
import sqlite3


conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()

class AddContacts(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+600+200")
        self.title("Contacts")
        self.resizable(False,False)
        self.top = Frame(self, height=80, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height= 500, bg = 'gray')
        self.bottom.pack(fill=X)
        self.heading = Label(self.top, text="Add person", font='Helvetica 20 bold', bg='white')
        self.heading.place(x=250, y =50)

        #first name
        self.first_name_label = Label(self.bottom, text="FirstName", font="Helvetica 20 bold", bg='white')
        self.first_name_label.place(x=49, y=40)
        self.first_name = Entry(self.bottom, width=30, bd=4)
        self.first_name.place(x=200, y=40)

        #last name
        self.last_name_label = Label(self.bottom, text="LastName", font="Helvetica 20 bold", bg='white')
        self.last_name_label.place(x=40, y=80)
        self.last_name = Entry(self.bottom, width=30, bd=4)
        self.last_name.place(x=200, y=80)

        #phone number
        self.phone_num_label = Label(self.bottom, text="PhoneNo", font="Helvetica 20 bold", bg='white')
        self.phone_num_label.place(x=40, y=160)
        self.phone_num = Entry(self.bottom, width=30, bd=4)
        self.phone_num.place(x=200, y=160)

        #address
        self.address_label = Label(self.bottom, text="Address", font="Helvetica 20 bold", bg='white')
        self.address_label.place(x=40, y=200)
        self.address = Entry(self.bottom, width=30, bd=4)
        self.address.place(x=200, y=200)

        #save contact
        savebtn = Button(self.bottom, text="Save", font="Helvetica 20 bold", bg='white', command=self.create_contact)
        savebtn.place(x=150, y=240)
    
    def create_contact(self):
        fname = self.first_name.get()
        lname = self.last_name.get()
        phonenum = self.phone_num.get()
        # address = self.address.get(1.0, 'end-lc')
        address = self.address.get()

        if fname and lname and phonenum and address !="":
            try:
                query ="insert into 'phonebook'(first_name, last_name, phonenumber, address) values(?,?,?,?)"
                cur.execute(query, (fname,lname,phonenum,address))
                conn.commit()
                messagebox.showinfo("success", "saved successfully")
            except EXCEPTION as e:
                messagebox.showerror("Error!",str(e))
        else:
            messagebox.showerror("Error!","fill all the fields")
