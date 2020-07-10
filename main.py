from tkinter import *

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
        # buttons for add, view, update, delete
        self.createBtn = Button(self.bottom, text="add contacts", )
        self.createBtn.place(x=210, y=70)
        self.readBtn = Button(self.bottom, text="read contacts", )
        self.readBtn.place(x=210, y=130)
        

def main():
    root = Tk() # root is GUI window
    app = PhonebookApp(root) 
    root.title("Phonebook App")
    root.geometry("550x520+270+200")
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__' :
    main()