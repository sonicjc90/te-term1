import random
from sense_hat import SenseHat

sense = SenseHat()

class Player:
    def __init__(self,sense):
        self.posx = random.randint(0, 7)
        self.posy = 7
        self.sense = sense
        
    def move_right(self):
        if self.posx < 7:
            self.posx = self.posx + 1
            self.display(1)
    def move_left(self):
        if self.posx > 0:
            self.posx = self.posx - 1
            self.display(-1)
    def display(self,move):
        sense.set_pixel(self.posx-move,self.posy,(0,0,0))
        sense.set_pixel(self.posx,self.posy,(0,255,0))