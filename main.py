from tkinter import *
import sqlite3


conn = sqlite3.connect('phonebook.db')
c = conn.cursor()

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
        self.createBtn = Button(self.bottom, text="add contacts", )
        self.createBtn.place(x=210, y=70)
        self.readBtn = Button(self.bottom, text="read contacts", command=self.readEntry )
        self.readBtn.place(x=210, y=130)

    def readEntry(self):
        person = PersonInfo()


class PersonInfo(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+600+200")
        self.title("Contacts")
        self.resizable(False,False)     


def main():
    root = Tk() # root is GUI window
    app = PhonebookApp(root) 
    root.title("Phonebook App")
    root.geometry("550x520+270+200")
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__' :
    main()