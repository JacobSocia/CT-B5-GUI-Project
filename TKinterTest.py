from tkinter import *
import random

top = Tk()
playlistList = []

def results():
    print(playlistList)
def addToList():
    newItem = E1.get()
    playlistList.append(newItem)
    E1.delete(0, END)

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

    B1Main = Button(text="    Week 1   ", bg="#b4b570", command = week1)
    B1Main.grid(column = 0, row = 2)

    B2Main = Button(text="    Week 2   ", bg="#a2a365")
    B2Main.grid(column = 0, row = 3)

    B3Main = Button(text="    Week 2   ", bg="#909159")
    B3Main.grid(column = 0, row = 4)


def week1():
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

    Bclear = Button(text= "Main Menu", bg="#34568B", command = clearWindow)
    Bclear.grid(column = 0, row = 5)

def week2():
    clearWindow()
    L1W2 = Label(top, text="Dice Roller Program")
    L1W2.grid(column = 0, row = 1)

    L2W2 = Label(top, text = "How many sides?")
    L2W2.grid(column= 2, row=2)
    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 0, row =3)

    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column =2, row=3)

    B1B2 = Button(text="Roll!", bg="Yellow")
    B1B2.grid(column= 2, row= 3)
    #to add: roll function and exit button


if__name__ == "__main__":
    mainMenu()
    top.mainloop()
