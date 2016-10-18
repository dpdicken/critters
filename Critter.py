from abc import ABC, abstractmethod
from enum import Enum

class Critter(ABC):

	x = 0
	y = 0
	width = 0
	height = 0
	alive = True
	awake = True
	neighbors = {" ", " ", " ", " "}

	def __init__(self):
		self.x = 0
		
	# Enum for directions
	class Directions(Enum):
		NORTH = 1
		SOUTH = 2
		EAST = 3
		WEST = 4
		CENTER = 5

	# Enum for attacks
	class Attack(Enum):
		ROAR = 1
		POUNCE = 2
		SCRATCH = 3
		FORFEIT = 4

	# These methods are called by the simulater and not the critter
	def getHeight(self):
		return height

	def getWidth(self):
		return width

	def setHeight(self, height):
		self.height = height

	def setWidth(self, width):
		self.width = width

	def getX(self):
		return x

	def getY(self):
		return y

	def setX(self, x):
		self.x = x

	def setY(self, y):
		self.y = y

	def isAlive(self):
		return alive

	def isAwake(self):
		return awake

	def setAlive(self, alive):
		self.alive = alive

	def setAwake(self, awake):
		self.awake = awake

	# # def setNeighbor(self, direction, critter):


	# def getNeighbor(self, direction):
	# 	return neighbors[direction.]

