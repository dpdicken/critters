#
# Author: Daniel Dicken
# Converting CSc 110 "Critters" program from java to python.
#

# Global variable, once a critter class is implemented, put its name in here
CLASS_NAMES = ["Rock"]

SELECTED_CLASSES = []

# Imports
import atexit
import sys
import time
import subprocess
import os
import imp
import inspect
from random import *
from Critter import *
from tkinter import *

# ---------- start main ----------

def main():
    control = Control()
    gui = GUI(control)
    #model = Model(3, 3)

# ---------- end main ----------

# ---------- start Model ----------

# Model represents the board and critter tournament
class Model:

    def __init__(self, xSize, ySize, control):

        self.control = control
        self.classes = []

        #self.world = [[None*xSize]*ySize]
        self.world = [[0 for x in range(ySize)] for y in range(xSize)]

        # Represent our map with a 2d array of the given size
        for x in range(xSize):
            for y in range(ySize):
                self.world[x][y] = Critter()

        self.i = 0
        for value in CLASS_NAMES:
           print("Value: " + str(SELECTED_CLASSES[self.i].get()))
           if (SELECTED_CLASSES[self.i].get() == True):
                print("Importing " + CLASS_NAMES[self.i])
                self.classes.append(__import__(CLASS_NAMES[self.i]))
           self.i += 1

#        for classVar in self.classes:
#           self.inst = classVar() 

    def getWorld(self):
        return self.world

# ---------- end Model ----------

# ---------- start Control ----------
class Control:

    def __init__(self):
        self.width = 0
        self.height = 0

    def setGUI(self, gui):
        self.gui = gui
        self.width = int(gui.width)
        self.height = int(gui.height)
        self.model = Model(self.width, self.height, self)

    def getMap(self):
        return self.model.getWorld()

# ---------- end Control ----------

# ---------- start GUI ----------
# Tkinter GUI for program
class GUI(Tk):

    # Define variables
    width = 0
    height = 0
    critters = 0

    def __init__(self, control):
        Tk.__init__(self)
        
        self.frame = Frame(self)
        self.frame.pack()

        self.control = control

        self.title("Critters Settings")

        self.widthLabel = Label(self.frame, text="width")
        self.widthEntry = Text(self.frame, height=1, width=10)
        self.widthEntry.insert(END, "60")
        self.widthLabel.pack()
        self.widthEntry.pack()

        self.heightLabel = Label(self.frame, text="height")
        self.heightEntry = Text(self.frame, height=1, width=10)
        self.heightEntry.insert(END, "50")
        self.heightLabel.pack()     
        self.heightEntry.pack()

        self.critterLabel = Label(self.frame, text="Number of Critters")
        self.critterEntry = Text(self.frame, height=1, width=10)
        self.critterEntry.insert(END, "5")
        self.critterLabel.pack()        
        self.critterEntry.pack()

        # Put tick boxes for each critter class in the directory to select if we want them in the tournament
        i = 0
        for fileName in CLASS_NAMES:
            SELECTED_CLASSES.append(BooleanVar())
            c = Checkbutton(self.frame, text=fileName, variable=SELECTED_CLASSES[i], onvalue=1, offvalue=0)
            i += 1
            c.pack()

        self.enterButton = Button(self.frame, text="Enter", fg="black", command=self.switchView)
        self.enterButton.pack()

        self.mainloop()

    # Switch view from starting prompt to critters tournament
    def switchView(self):

        self.width = self.retrieve_input(self.widthEntry)
        self.height = self.retrieve_input(self.heightEntry)
        self.critters = self.retrieve_input(self.critterEntry)

        if isValid(self.width) and isValid(self.height) and isValid(self.critters):
            self.width = int(self.width)
            self.height = int(self.height)
            self.control.setGUI(self)
            self.setMapGUI()
        else:
            self.errorWindow("Given inputs were not numbers")

    # Draw the map and other aspects of GUI
    def setMapGUI(self):

        self.frame.destroy()
        self.mapTemp = self.control.getMap()

        self.guiMap = Canvas(self, width=(self.width*12)+1,height=(self.height*12)+1, bg="lightgreen")
        self.guiMap.grid(row = 0, column = 0)

        self.multiple = 0
        for j in range(self.height + 2):
            self.guiMap.create_line(0, self.multiple + 1, self.width*12, self.multiple + 1)
            self.multiple = self.multiple + 12

        self.multiple = 0
        for i in range(self.width + 2):
            self.guiMap.create_line(self.multiple + 1, 0, self.multiple + 1, self.height*12)
            self.multiple = self.multiple + 12

        self.points = []

        self.scale = Scale(self, from_=0, to=61, orient=HORIZONTAL)
        self.scale.grid(row = 1, column = 0)

        while i < int(self.critters):
            self.randX = randInt(self.width - 1)
            self.randY = randInt(self.height - 1)

            if (self.randX,self.randY) not in self.points:
                # self.mapTemp[randX][randY] = 
                i = i + 1
            else:
                continue

    # Give error message popup windows
    def errorWindow(self, msg):

        self.top = Toplevel()
        self.top.title("Error")

        self.msgWindow = Message(self.top, text=msg)
        self.msgWindow.pack()

        self.button = Button(self.top, text="Dismiss", command=self.top.destroy)
        self.button.pack()

    def retrieve_input(self, textBox):
        return textBox.get("1.0",'end-1c')

# ---------- end GUI ----------

# ---------- start Helper Functions ----------

# check if input is valid
def isValid(s):

    try: 

        num = int(s)

        if (num > 0):
            return  True
        else:
            return False

    except ValueError:
        return False

# ---------- end Helper Functions ----------

main()

