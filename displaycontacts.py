from tkinter import *
from tkinter import messagebox
import sqlite3


conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()

class DisplayContacts(Toplevel):
    def __init__(self,person_id):
        Toplevel.__init__(self)
        self.geometry("650x650+600+200")
        self.title("Contacts")
        self.resizable(False,False)
        self.top = Frame(self, height=80, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height= 500, bg = 'gray')
        self.bottom.pack(fill=X)
        self.heading = Label(self.top, text="display person", font='Helvetica 20 bold', bg='white')
        self.heading.place(x=250, y =50)

        query = "select * from phonebook where id = '{}'".format(person_id) 
        result = cur.execute(query).fetchone()  
        self.person_id = person_id
        fname = result[1] 
        lname = result[2] 
        phone = result[3] 
        address = result[4] 
        print(fname, lname, phone, address)
        #first name
        self.first_name_label = Label(self.bottom, text="FirstName", font="Helvetica 20 bold", bg='white')
        self.first_name_label.place(x=49, y=40)
        self.first_name = Entry(self.bottom, width=30, bd=4)
        self.first_name.insert(0, fname)
        self.first_name.config(state="disabled")
        self.first_name.place(x=200, y=40)

        #last name
        self.last_name_label = Label(self.bottom, text="LastName", font="Helvetica 20 bold", bg='white')
        self.last_name_label.place(x=40, y=80)
        self.last_name = Entry(self.bottom, width=30, bd=4)
        self.last_name.insert(0, lname)
        self.last_name.config(state="disabled")
        self.last_name.place(x=200, y=80)

        #phone number
        self.phone_num_label = Label(self.bottom, text="PhoneNo", font="Helvetica 20 bold", bg='white')
        self.phone_num_label.place(x=40, y=160)
        self.phone_num = Entry(self.bottom, width=30, bd=4)
        self.phone_num.insert(0, phone)
        self.phone_num.config(state="disabled")
        self.phone_num.place(x=200, y=160)

        #address
        self.address_label = Label(self.bottom, text="Address", font="Helvetica 20 bold", bg='white')
        self.address_label.place(x=40, y=200)
        self.address = Entry(self.bottom, width=30, bd=4)
        self.address.insert(0, address)
        self.address.config(state="disabled")
        self.address.place(x=200, y=200)

    
   
