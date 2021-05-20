from tkinter import *
import random
import turtle

top = Tk()
pen = turtle.Turtle()
smiles = turtle.Turtle()
playlistList = []
myRolls = []
rollTimes = 0
dieType = 0

def results():
    print(playlistList)


def happyEmotion():
    # function for creation of eye
    def eye(col, rad):
        pen.down()
        pen.fillcolor(col)
        pen.begin_fill()
        pen.circle(rad)
        pen.end_fill()
        pen.up()

 
    # draw face
    pen.fillcolor('yellow')
    pen.begin_fill()
    pen.circle(100)
    pen.end_fill()
    pen.up()

    # draw eyes
    pen.goto(-40, 120)
    eye('white', 15)
    pen.goto(-37, 125)
    eye('black', 5)
    pen.goto(40, 120)
    eye('white', 15)
    pen.goto(40, 125)
    eye('black', 5)
     

     
    # draw mouth
    pen.goto(-40, 85)
    pen.down()
    pen.right(90)
    pen.circle(40, 180)
    pen.up()
def angryEmotion():
    smiles.penup()
    smiles.goto(-105,155)
    smiles.pendown()
    smiles.goto(-45,115)

    smiles.penup()
    smiles.goto(-75,75)
    smiles.pendown()
    smiles.circle(10)

    smiles.penup()
    smiles.goto(105,155)
    smiles.pendown()
    smiles.goto(45,115)

    smiles.penup()
    smiles.goto(75,75)
    smiles.pendown()
    smiles.circle(10)

    smiles.penup()
    smiles.goto(0,25)
    smiles.pendown()
    smiles.circle(-100,80)

    smiles.penup()
    smiles.setheading(180)
    smiles.goto(0,25)
    smiles.pendown()
    smiles.circle(100,80)

    turtle.done()

def surpriseEmotion():
    smiles.penup()
    smiles.goto(-75,150)
    smiles.pendown()
    smiles.circle(10)     #eye one

    smiles.penup()
    smiles.goto(75, 150)
    smiles.pendown()
    smiles.circle(10)     #eye two


    smiles.penup()
    smiles.goto(0,50)
    smiles.pendown()
    smiles.circle(-100)

    turtle.done()
def sadEmotion():
    smiles.penup()
    smiles.goto(0,50)
    smiles.pendown()
    smiles.circle(-100,90)

    smiles.penup()
    smiles.setheading(180)
    smiles.goto(0,50)
    smiles.pendown()
    smiles.circle(100,90)
    turtle.done()



def exportList():
    with open("test.txt", "w") as f:
        for item in playlistList:
            f.write("%s\n" % item)

def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()
def mainMenu():
    clearWindow()
    LMain = Label(top, text="Block 5 GUI Projects")
    LMain.grid(column = 0, row = 1)

    B1Main = Button(text="    Week 1   ", bg="#CBC3E3", command = week1)
    B1Main.grid(column = 0, row = 2)

    B2Main = Button(text="    Week 2   ", bg="#CBC3E3", command = week2)
    B2Main.grid(column = 0, row = 3)

    B3Main = Button(text="    Week 3   ", bg="#CBC3E3", command = week3)
    B3Main.grid(column = 0, row = 4)


def week1():
    def addToList():
        newItem = E1.get()
        playlistList.append(newItem)
        E1.delete(0, END)
    clearWindow()
    #This is a Lable widget
    L1 = Label(top, text="playlistList")
    L1.grid(column = 0, row = 1)

    #This is a Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    #This is a Button widget
    B1 = Button(text= "    Print List    ", bg="#34568B", command = results )
    B1.grid(column = 0, row = 3)

    B2 = Button(text= "    +    ", bg="#DD4124", command = addToList)
    B2.grid(column = 1, row = 2)

    B3 = Button(text= "    Export List    ", bg="#34568B", command = exportList)
    B3.grid(column = 0, row = 4)

    Bclear = Button(text= "Main Menu", bg="#90ee90", command = mainMenu)
    Bclear.grid(column = 0, row = 5)

def week2():
    def rollDice():
        dieType = E1W2.get()
        rollTimes = E2W2.get()
        #Clear window after pulling entry data
        clearWindow()
        #calculate dice rolls
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))
        #display dice rolls and present and exit button
        L4W2 = Label(top, tex="Here are your rolls!")
        L4W2.grid(column= 0, row=1)
        #this one will use a .format() statement
        L5W2 = Label(top, text = "{}".format(myRolls))
        L5W2.grid(column= 0, row = 2)
        B2W2 = Button(text = "Main Menu", bg= "yellow", command = mainMenu)
        B2W2.grid(column=0,row=3)
    clearWindow()
    L1W2 = Label(top, text="Dice Roller Program")
    L1W2.grid(column = 0, row = 1)

    L2W2 = Label(top, text = "How many sides?")
    L2W2.grid(column= 2, row=2)

    L3W2 = Label(top, text = "How many roles?")
    L3W2.grid(column = 0, row =2)
    
    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 0, row =3)

    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column =2, row=3)

    B1B2 = Button(text="Roll!", bg="#34568B")
    B1B2.grid(column= 2, row= 4)
    #to add: roll function and exit button
    Bclear = Button(text= "Main Menu", bg="#90ee90", command = mainMenu)
    Bclear.grid(column = 0, row = 5)

def week3():
    clearWindow()
    L1W3 = Label(top, text = "Emotion Drawer")
    L1W3.grid(column = 0, row=1)

    B1W3 = Button(text="happy", bg = "#34568B", command = happyEmotion)
    B1W3.grid(column=0, row= 2)

    B2W3 = Button(text="Angry", bg = "#34568B", command = angryEmotion)
    B2W3.grid(column=0, row= 3)

    B3W3 = Button(text="Surprise", bg = "#34568B", command = surpriseEmotion)
    B3W3.grid(column=0, row= 4)

    B4W3 = Button(text="Sad", bg = "#34568B", command = sadEmotion)
    B4W3.grid(column=0, row= 5)

    Bclear = Button(text= "Main Menu", bg="#90ee90", command = mainMenu)
    Bclear.grid(column = 0, row = 5)

    
    


if __name__ == "__main__":
    mainMenu()
    top.mainloop()
