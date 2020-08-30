import random
from tkinter import *
from PIL import ImageTk, Image


#X and Y Var

x = 580
y = 570


#GUI root window

root = Tk()
root.title("Random Walk")

#Canvas
canvas = Canvas(root, height=1200, width=1200).pack()

#Frame
#frame = Frame(root, bg="Grey").place(relwidth=1, relheight=1)


#Walker


scale = ImageTk.PhotoImage(Image.open("Python/Random Walk/scale.jpg"))
scalelbl = Label(canvas, image=scale).place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("Python/Random Walk/dot.png"))
imagelbl = Label(canvas, image=img)
imagelbl.place(x=x,y=y)


# Increases or decreases X and Y radomly by 1 each run.

repeat = 50000
for i in range(repeat):
    
    n,p = random.randrange(-1,2), random.randrange(-1,2)
    if n == 1:
        x += 1
    elif n == -1:
        x -= 1
    if p == 1:
        y += 1
    elif p == -1:
        y -= 1   
    #print("[" + str(x) + ",", str(y) +"]")


root.mainloop()


