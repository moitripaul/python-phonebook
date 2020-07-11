from tkinter import *


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
