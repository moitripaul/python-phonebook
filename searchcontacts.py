from tkinter import *
from tkinter import messagebox
import sqlite3


conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()

class SearchContacts(Toplevel):
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

        #search contact
        searchbtn = Button(self.bottom, text="Search", font="Helvetica 20 bold", bg='white')
        searchbtn.place(x=150, y=120)
