import pygame
import pygame.mixer
from pygame.mixer import Sound
from gpiozero import PWMLED
from gpiozero import Button
from signal import pause
from time import sleep
import random
import os

pygame.mixer.init()

randomfile = ""
file = ""

eyes = PWMLED(17)
green = PWMLED(6)
pushme = Button(16)

def scary_noise():
    randomfile = random.sample(os.listdir("/home/pi/spookysfx/"), 1)[0]
    file = "/home/pi/spookysfx/" + randomfile
    fright = Sound(file)
    pygame.mixer.music.set_volume(0.75)
    fright.play()

eyes.pulse(fade_in_time=2, fade_out_time=2)
green.pulse(fade_in_time=2, fade_out_time=2)

pushme.when_pressed = scary_noise

pause()
