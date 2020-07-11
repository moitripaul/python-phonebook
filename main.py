from tkinter import *
from tkinter import messagebox
from addcontacts import AddContacts
from searchcontacts import SearchContacts
import sqlite3


conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()

class PhonebookApp(object):
    def __init__(self, master):
        #phonebook window
        self.master = master
        self.top = Frame(master, height=80, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(master, height= 500, bg = 'gray')
        self.bottom.pack(fill=X)
        #heading
        self.heading = Label(self.top, text='Phonebook App', font='Helvetica 20 bold', bg='white')
        self.heading.place(x=230, y= 25)
        # buttons for create, read, update, delete
        self.createBtn = Button(self.bottom, text="add contacts", command=self.createEntry )
        self.createBtn.place(x=210, y=70)
        self.readBtn = Button(self.bottom, text="search contacts", command=self.readEntry )
        self.readBtn.place(x=210, y=130)
        self.viewAllBtn = Button(self.bottom, text="View all contacts", command=self.allEntries )
        self.viewAllBtn.place(x=210, y=190)

    def allEntries(self):
        person = PersonInfo()
        
    def createEntry(self):
        add_person = AddContacts()
    
    def readEntry(self):
        search_person = SearchContacts()


class PersonInfo(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+600+200")
        self.title("Contacts")
        self.resizable(False,False)
        self.top = Frame(self, height=80, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height= 500, bg = 'gray')
        self.bottom.pack(fill=X)
        self.heading = Label(self.top, text='All Contacts List', font='Helvetica 20 bold', bg='white')
        self.heading.place(x=230, y= 25)
        # self.scrollbar = Scrollbar(self.bottom, orient= VERTICAL)
        # self.scrollbar.grid(row=0, column=1, sticky=N+S)
        # self.listBox = Listbox(self.bottom, width=40, height = 27)
        # self.listBox.grid(row=0, column=0, padx=(40,0))  
        self.listBox = Listbox(self.bottom, width=100,  height = 27)
        self.listBox.grid(row=0, column=0, padx=(20,0))  
        contacts = cur.execute("select * from 'phonebook'").fetchall() 
        totalcontact = 0
        for contact in contacts:
            self.listBox.insert(totalcontact, str(contact[0])+" " +contact[1]+ " " +contact[2]+ " " +contact[3]+ " " +contact[4])
            totalcontact+=0
        print(contacts)


def main():
    root = Tk() # root is GUI window
    app = PhonebookApp(root) 
    root.title("Phonebook App")
    root.geometry("550x520+270+200")
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__' :
    main()