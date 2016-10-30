class Critter():

    # Methods students will be implementing

    def eat(self):
        return false

    def fight(self, opponent):
        return ATTACK_FORFEIT

    def getColor(self):
        return "grey"

    def getMove(self):
        return DIRECTION_CENTER

    def toString(self):
        return "?"

    # End methods students will be implementing

    # Constants for attacks, directions
    ATTACK_POUNCE    = 0
    ATTACK_ROAR      = 1
    ATTACK_SCRATCH   = 2
    ATTACK_FORFEIT   = 3
    DIRECTION_NORTH  = 0
    DIRECTION_SOUTH  = 1
    DIRECTION_EAST   = 2
    DIRECTION_WEST   = 3
    DIRECTION_CENTER = 4

    x = 0
    y = 0
    width = 0
    height = 0
    alive = True
    awake = True
    neighbors = {" ", " ", " ", " "}

    def __init__(self):
        self.x = 0
        
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

    def setNeighbor(self, direction, value):
        neighbors[direction] = value

    def getNeighbor(self, direction):
        return neighbors[direction]

