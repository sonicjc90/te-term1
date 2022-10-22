import random


class Player:
    def __init__(self,left,right):
        self.left = left
        self.right = right
        self.position = random.randint(left,right)
        
    def move_right(self):
        if self.position < self.right:
            self.position = self.position + 1
    def move_left(self):
        if self.position > self.left:
            self.position = self.position - 1
    def get_position():
        return position