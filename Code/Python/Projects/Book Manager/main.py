import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
from tinydb import TinyDB, Query

#Sets file for database
db = TinyDB('E:/Code-Learning/Code/Python/Projects/Book Manager/db.json')
search = Query()
#Button Functions
def add():
    name = simpledialog("Name", "Name of book")

def create_book(name, author, year, *tags):
    if db.search(search.name == str(book_name.get())):
        tk.Label(frame, text="Book already owned", padx =6, pady= 8, fg="black").place(x=70,y=200)

#Basic tkinter setup
root = tk.Tk()
frame = tk.Frame(root, height=500, width=500, bg='#354E71').pack()
root.title("Book Manager")

book_name = tk.StringVar()
name_label = tk.Label(frame, text="Name:", bg='#354E71').place(x=50, y=400)
name_entry = tk.Entry(frame, textvariable=book_name).place(x=100, y=400)

button_add = tk.Button(frame, text="Add Book", fg='green', command=add)
button_add.place(x=120, y=450)
button_remove = tk.Button(frame, text="Remove Book", fg='red').place(x=250, y=450)


#Class
class Book():
    def __init__(self, name, author, year, *tags):
        self.name = name 
        self.author = author
        self.year = year
        self.tags = tags


#Keeps the tkinter GUI open
root.mainloop()
#We must close the DB once we are done with it.
db.close()