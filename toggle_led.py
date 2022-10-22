from gpiozero import LED
from time import sleep

led = LED(17)

while True:
   sans = input("Do you want the lightbulb on or off? --->".lower)
   if sans == "on":
    led.on()
   elif sans == "off":
    led.off()