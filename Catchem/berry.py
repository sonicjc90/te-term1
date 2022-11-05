import random
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

class Berry:
    def __init__(self,color,speed,value):
        # self.position = random.randint(0,7)
        self.posx = random.randint(0,7) 
        self.posy = 0
        self.color = color
        self.speed = speed
        self.value = value


    def drop(self):
        if self.posy <7:
            self.posy += 1
            sleep(self.speed)
            self.display()

    def display(self):
        # sense.set_pixel(self.position,self.color)
        x = self.posx
        y = self.posy
        if self.posy>0:
            sense.set_pixel(x,y-1,(0,0,0))
        sense.set_pixel(x,y,self.color)