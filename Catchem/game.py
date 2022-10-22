import SenseHat
import time
import random
from player import Player

class Game:

  

  def __init__(self):
    self.score = 0

    self.game_over = False

    self.speed = 0.5 

    self.berries = []

    self.player = Player(random.randint(56,63))

    

  def start(self):

    #beginning sequence w/countdown. Add more if needed.

    sense.show_message("Catchem!", text_colour=colors.o, scroll_speed=0.05)

    # start your game with a countdown or an animation of your choice.

  def play(self):
      self.start()
      
      while not self.game_over
#play game 