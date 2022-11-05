from sense_hat import SenseHat
import time
import random
from player import Player
from berry import Berry

sense = SenseHat()

class Game:
  def __init__(self):
    self.score = 0

    self.game_over = False

    self.speed = 0.5 

    self.berries = []

    self.player = Player(sense)

    self.berry = Berry((255,255,255),1,0)

  def start(self):

    #beginning sequence w/countdown. Add more if needed.

    sense.show_message("Catchem!", text_colour=(0,0,255), scroll_speed=0.05)

    # start your game with a countdown or an animation of your choice.

  def play(self):
      self.start()
      self.player.display(0)
      self.berry.display()
      while not self.game_over:
        self.berry.display()
        self.berry.drop()
        for event in sense.stick.get_events():
          if event.action == "pressed" and event.direction == "left":
            print("left")
            self.player.move_left()
          elif event.action == "pressed" and event.direction == "right":
            self.player.move_right()
        
        if self.berry.posy == 7:
          if self.player.posx == self.berry.posx:
            self.score += 1
          else:
            self.game_over = True
            sense.show_message(f"Game Over! Score: {self.score}", text_colour=(0,0,255), scroll_speed=0.05)
        
          sense.set_pixel(self.berry.posx, self.berry.posy,(0,0,0))
          self.berry.posy = 0
          self.berry.posx = random.randint(0,7)


            #play game 

  # def make_berries(self):
    
