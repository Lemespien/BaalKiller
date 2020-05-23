"""
 
All coordinates assume a screen resolution of 1280x1024, and Chrome 
maximized with the Bookmarks Toolbar enabled.
Game has been moved to just below the toolbar.
X_PAD = 629
Y_PAD = 102
Play area =  X_PAD+1, Y_PAD+1, 1912, 748
"""

from PIL import ImageGrab
import os
import time

# Globals
# ------------------

X_PAD = 629
Y_PAD = 102


def screenGrab():
    box = (X_PAD + 1, Y_PAD + 1, X_PAD + 1283, 646)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
            '.png', 'PNG')


def main():
    screenGrab()


if __name__ == '__main__':
    main()
