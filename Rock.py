from Critter import Critter

class Rock(Critter):

    def __init__(self):
        print("test")

    def eat(self):
        return true

    def fight(self, opponent):
        return ATTACK_POUNCE

    def getColor(self):
        return "black"

    def getMove(self):
        if (y > height/2 + 10):
            return DIRECTION_NORTH
        else:
            return DIRECTION_SOUTH

    def toString(self):
        return "R"
