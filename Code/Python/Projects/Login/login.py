#We need to import some Libraries
import tkinter as tk
from tkinter import filedialog, Text
import os
from tinydb import TinyDB, Query, where

#Root, Canvas and Frame for the base of our GUI window
root = tk.Tk()
root.title("Login Screen")

canvas = tk.Canvas(root, height=450, width=450, bg="#031B4E")
canvas.pack()

frame = tk.Frame(root, bg="#021846")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


#Username and password label and entry field
usernamelb = tk.Label(frame, text="Username")
usernamelb.place(x=90, y= 100)

usernamevar = tk.StringVar()
usernamefield = tk.Entry(frame, textvariable=usernamevar)
usernamefield.place(x=160, y= 100)

passwordlb = tk.Label(frame, text="Password")
passwordlb.place(x=90, y= 130)

passwordvar = tk.StringVar()
passwordfield = tk.Entry(frame, textvariable=passwordvar)
passwordfield.place(x=160, y= 130)

#Database File
db = TinyDB("Python/Projects/Login/loginDB.json")


#Register and Login commands

search = Query()

def register():
    if db.search(search.username == str(usernamevar.get())):
        tk.Label(frame, text="Username already in use", padx =6, pady= 8, fg="black").place(x=110,y=40)
    else:
        db.insert({'username': str(usernamevar.get()), 'password': str(passwordvar.get())})
        tk.Label(frame, text="Registration success, you can now login.", padx = 8, pady= 4).place(x=80,y=190)


def login():
    if db.search(search.username == str(usernamevar.get())) and db.search(search.password == str(passwordvar.get())):
        tk.Label(frame, text="Login Successful", padx =7, pady= 8, fg="black").place(x=120,y=30)
    else:
        tk.Label(frame, text="Invalid Credentials.", padx =6, pady= 8, fg="black").place(x=110,y=40).place(x=110,y=40)

#Register and Login Buttons
login = tk.Button(frame, text="Login", padx=10, pady=8,
                    fg="black", bg="lightblue", width=6, command=login)
login.place(x=160, y=240)


register = tk.Button(frame, text="Register", padx=10, pady=8,
                    fg="black", bg="lightblue", command=register)
register.place(x=160, y=280)


#Mainloop that keeps the GUI window open
root.mainloop()

#We must close the database file once we are done.
db.close()

