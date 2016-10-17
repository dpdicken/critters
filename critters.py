#
# Author: Daniel Dicken
# Converting CSc 110 "Critters" program from java to python.
#

# Imports
import atexit
import sys
import time
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

	world = []

	def __init__(self, xSize, ySize, control):

		self.control = control

		# Represent our map with a 2d array of the given size
		self.world = [[0 for x in range(ySize)] for y in range(xSize)]

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

		self.enterButton = Button(self.frame, text="Enter", fg="black", command=self.switchView)
		self.enterButton.pack()

		self.mainloop()

	def switchView(self):

		self.width = self.retrieve_input(self.widthEntry)
		self.height = self.retrieve_input(self.heightEntry)
		self.critters = self.retrieve_input(self.critterEntry)

		if isValid(self.width) and isValid(self.height) and isValid(self.critters):
			self.control.setGUI(self)
			self.setMapGUI()
		else:
			self.errorWindow("Given inputs were not numbers")

	def setMapGUI(self):
		self.frame.destroy()
		self.frame = Frame(self)

	# Give error message popup windows
	def errorWindow(self, msg):

		top = Toplevel()
		top.title("Error")

		msgWindow = Message(top, text=msg)
		msgWindow.pack()

		button = Button(top, text="Dismiss", command=top.destroy)
		button.pack()

	def retrieve_input(self, textBox):
		return textBox.get("1.0",'end-1c')

# ---------- end GUI ----------


# ---------- start Helper Functions ----------
def isValid(s):

    try: 

        num = int(s)

        if (num > 0):
        	return 	True
        else:
        	return False

    except ValueError:
        return False

# ---------- end Helper Functions ----------


main()
