from tkinter import *
from tkinter import messagebox
import sqlite3
from displaycontacts import DisplayContacts


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
        self.heading = Label(self.top, text="Search person", font='Helvetica 20 bold', bg='white')
        self.heading.place(x=250, y =50)
        self.selectbtn = Label(self.bottom, text="Select person", font="Helvetica 20 bold", bg='white')
        self.selectbtn.place(x=49, y=40)

      #   #first name
      #   self.first_name_label = Label(self.bottom, text="FirstName", font="Helvetica 20 bold", bg='white')
      #   self.first_name_label.place(x=49, y=40)
      #   self.first_name = Entry(self.bottom, width=30, bd=4)
      #   self.first_name.place(x=200, y=40)

      #   #last name
      #   self.last_name_label = Label(self.bottom, text="LastName", font="Helvetica 20 bold", bg='white')
      #   self.last_name_label.place(x=40, y=80)
      #   self.last_name = Entry(self.bottom, width=30, bd=4)
      #   self.last_name.place(x=200, y=80)

        self.listBox = Listbox(self.bottom, width=100,  height = 27)
        self.listBox.grid(row=0, column=0, padx=(0,0))  
        #search contact
        searchbtn = Button(self.bottom, text="Select and Search", font="Helvetica 20 bold", bg='white', command = self.show_personinfo)
        searchbtn.place(x=200, y=300)

        contacts = cur.execute("select * from 'phonebook'").fetchall() 
        totalcontact = 0
        for contact in contacts:
            self.listBox.insert(totalcontact, str(contact[0])+". " +contact[1]+ " " +contact[2])
            totalcontact+=0

   def show_personinfo(self):
      person_info = self.listBox.curselection()
      person = self.listBox.get(person_info)
      id = person.split(".")[0]
      display_person = DisplayContacts(id)