from tkinter import *
import math
from License_text import *

canvas_width = 500
canvas_height = 500
python_green = "#89CFF0"

main = Tk()
main.geometry("600x600")
main.title("Polygon Area")


Canv = Canvas(main, width=canvas_width, height=canvas_height, bg="white")
Canv.grid(row=0, column=0,columnspan=4)

Procedure=[]

print(math.sin(math.radians(90)))
print(math.sin(math.radians(90)))


def Calculate():
    global b
    global d
    b.configure(bg = "#234", state= DISABLED)
    d.configure(text = "Inserisci la lunghezza del lato. Premi Enter per confermare")


def Delete():
    Canv.delete("Polygon")
    Canv.delete("point")

def Show_License():
    openNewWindow(main)



b = Button(text="Crea Poligono", command=Calculate)
b.grid(row=1, column=0,columnspan=1)

c = Button(text="Delete Canvas", command=Delete)
c.grid(row=1, column=1,columnspan=1)



d = Label(text="Create Polygon...")
d.grid(row=3, column=0,columnspan=1)



# Button to insert 
e = Entry(main, width=50)
e.grid(row=2, column=0,columnspan=1)
e.insert(0, "")

f = Button(text="License", command=Show_License)
f.grid(row=2, column=1,columnspan=1)


def Insert(event):
    global e
    global a
    global b
    global d

    elem = e.get()
    Procedure.append(elem)
    print(Procedure)
    e.delete(0,END)

    if len(Procedure)==1:
        d.configure(text = "Inserisci il numero di lati. Premi Enter per confermare")
    
    if len(Procedure)==2:
        d.configure(text = "Inserisci la coordinata x. Premi Enter per confermare")

    if len(Procedure)==3:
        d.configure(text = "Inserisci la coordinata y. Premi Enter per confermare")    

    if len(Procedure)==4:
        l = int(Procedure[0])
        n = int(Procedure[1])
        center_x= int(Procedure[2])
        center_y= int(Procedure[3])
        Procedure.clear()
        angle = 0
        angle_inc = 360/n
        coordinate = [None] * n 
        print(coordinate)
        print(coordinate[0])
        print(angle)

        for el in range(n):
            coordinate[el] = [None] * (2)
            print(coordinate)

        for el in range(n):
            print(type(el))
            coordinate[el][0]= int((l * math.cos(math.radians(angle)) + center_x))
            coordinate[el][1] =int(( l * math.sin(math.radians(angle))+ center_y))
            Canv.create_oval(coordinate[el][0]-3, coordinate[el][1] -3, coordinate[el][0]+3, coordinate[el][1]+3, fill="black", tags="point")
            print(coordinate),
            angle += angle_inc
            print("el is " + str(el))
            print(angle)
        Canv.create_polygon(coordinate, fill='#088F8F', outline='gray', width=1, tags="Polygon")
        b.configure(bg="white", state= NORMAL)
        Canv.tag_raise("point")



main.bind("<Return>", Insert)


mainloop()