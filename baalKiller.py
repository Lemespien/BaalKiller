"""

All coordinates assume a screen resolution of 1280x1024, and Chrome
maximized with the Bookmarks Toolbar enabled.
Game has been moved to just below the toolbar.
X_PAD_DEFAULT = 629
Y_PAD_DEFAULT = 102
Play area =  X_PAD_DEFAULT+1, Y_PAD_DEFAULT+1, 1912, 748
"""

import time
from PIL import ImageGrab
import pyautogui
import win32api
import win32con
from imagesearch import imagesearcharea
import coordinates as c
# Globals
# ------------------

X_PAD_DEFAULT = 629
Y_PAD_DEFAULT = 102


class Baal_Part():
    def __init__(self):
        self.baal_part_cords = c.BaalPartsCords()
        self.baal_region = c.BaalRegions()
        self.baal_images = c.BaalImages()
        self.wings = (self.baal_part_cords.b_wing_start,
                      self.baal_part_cords.b_wing_stop,
                      self.baal_region.b_wing,
                      self.baal_images.b_wing_image)
        self.tail = (self.baal_part_cords.b_tail_start,
                     self.baal_part_cords.b_tail_stop,
                     self.baal_region.b_tail,
                     self.baal_images.b_tail_image)
        self.feet = (self.baal_part_cords.b_feet_start,
                     self.baal_part_cords.b_feet_stop,
                     self.baal_region.b_feet,
                     self.baal_images.b_feet_image)
        self.mouth = (self.baal_part_cords.b_mouth_start,
                      self.baal_part_cords.b_mouth_stop,
                      self.baal_region.b_mouth,
                      self.baal_images.b_mouth_image)


BAAL_PART = Baal_Part()
X_PAD_DEFAULT = BAAL_PART.baal_part_cords.x_pad
Y_PAD_DEFAULT = BAAL_PART.baal_part_cords.y_pad


def screenGrab():
    box = (X_PAD_DEFAULT + 1, Y_PAD_DEFAULT + 1, X_PAD_DEFAULT + 1283, 646)
    im = ImageGrab.grab()
    # im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
    #         '.png', 'PNG')
    return im


def imageSearchBaalKiller(baalPart):
    startCord = baalPart[0]
    stopCord = baalPart[1]
    region = baalPart[2]
    image = baalPart[3]
    clicked = 0
    timeSinceLastClick = 0
    # pyautogui.moveTo(region[0], region[1])
    # time.sleep(1)
    # pyautogui.moveTo(region[2], region[3])
    # time.sleep(1)
    pyautogui.click(startCord)
    while True:
        if (clicked == 50):
            break
        if (timeSinceLastClick > 50):
            pyautogui.click(stopCord)
            pyautogui.click(startCord)
            timeSinceLastClick = 0
        pos = imagesearcharea(image,
                              region[0], region[1], region[2], region[3], 0.98)
        if pos[0] != -1:
            print("position : ", pos[0], pos[1])
            # pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click(startCord)
            clicked += 1
            time.sleep(0.1)
        else:
            timeSinceLastClick += 1
            print("image not found")
    pyautogui.click(stopCord)


def main():
    baalMenu()
    # partDict = filter(lambda a: not a.startswith('__'), dir(baalPart))
    for key, value in vars(BAAL_PART).items():
        print(key, value)
        imageSearchBaalKiller(value)
    pass


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print("Click.")


def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    print('left Down')


def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print('left release')


def mousePos(cord):
    win32api.SetCursorPos((X_PAD_DEFAULT + cord[0], Y_PAD_DEFAULT + cord[1]))


def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - X_PAD_DEFAULT
    y = y - Y_PAD_DEFAULT
    print(x, y)
    return (x, y)


def baalMenu():
    # Location of baalKiller
    mousePos((824, 69))
    leftClick()
    time.sleep(.1)


def clickBaalPart(cord):
    mousePos(cord)
    leftClick()


if __name__ == '__main__':
    main()
