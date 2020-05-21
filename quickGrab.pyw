"""
 
All coordinates assume a screen resolution of 1280x1024, and Chrome 
maximized with the Bookmarks Toolbar enabled.
Game has been moved to just below the toolbar.
x_pad = 629
y_pad = 102
Play area =  x_pad+1, y_pad+1, 1912, 748
"""

from PIL import ImageGrab
import os
import time

# Globals
# ------------------

x_pad = 629
y_pad = 102


def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 1283, 646)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
            '.png', 'PNG')


def main():
    screenGrab()


if __name__ == '__main__':
    main()
