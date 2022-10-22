import random
from Sense_hat import SenseHat
from time import sleep

sense = SenseHat()

class Berry:
    def __init__(self,color,speed,value):
        self.position = random.randint(0,7)
        self.color = color
        self.speed = speed
        self.value = value


    def drop(self):
        if self.position <= 63:
            self.position = self.position += 8
        sleep(self.speed)
        self.display()

    def display(self):
        sense.set_pixel(self.position,self.color)
        x = self.position%8
        y = self.position//8
        sense.set_pixel(x,y-1,(0,0,0))
        sense.set_pixel(x,y,self.color)