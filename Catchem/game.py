from sense_hat import SenseHat
import time
import random
from player import Player

sense = SenseHat()

class Game:
  def __init__(self):
    self.score = 0

    self.game_over = False

    self.speed = 0.5 

    self.berries = []

    self.player = Player(56,63,sense)

    

  def start(self):

    #beginning sequence w/countdown. Add more if needed.

    sense.show_message("Catchem!", text_colour=(0,0,255), scroll_speed=0.05)

    # start your game with a countdown or an animation of your choice.

  def play(self):
      self.start()
      self.player.display(0)
      
      while not self.game_over:
        for event in sense.stick.get_events():
          if event.action == "pressed" and event.direction == "left":
            print("left")
            self.player.move_left()
          elif event.action == "pressed" and event.direction == "right":
            self.player.move_right()
#play game 