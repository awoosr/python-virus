# Windows-Rotate Virus
# By sreemanreddy
# github https://github.com/awoosr/python-virus/
#
#
# instalation: pip3 install rotate-screen

import rotatescreen
import time

screen = rotatescreen.get_primary_display()

def start():
    while True:
        screen.set_landscape()
        time.sleep(0.3)
        screen.set_portrait_flipped()
        time.sleep(0.3)
        screen.set_landscape_flipped()
        time.sleep(0.3)
        screen.set_portrait()
        time.sleep(0.3)
        screen.set_landscape()

# please be sure then clear start() function hastag
#start()
