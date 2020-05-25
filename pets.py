import coordinates as c
from image_index import IMAGE_DICTIONARY
import helpers
from tabs import Tabs
import time
import pyautogui as pg


class Pets(Tabs):
    COORDINATES = c.PetCords()
    DISTRIBUTE = IMAGE_DICTIONARY["distribute"]
    FEED = IMAGE_DICTIONARY["feed"]
    TABS = [COORDINATES.tab]

    def distribute(self):
        self.go_to_tab()
        coordinates = self.COORDINATES
        image = self.DISTRIBUTE
        if image in coordinates.IMAGE_CACHE:
            pos = coordinates.IMAGE_CACHE[image]
            print("got image from cache")
        else:
            pos = helpers.click_image_on_screen(image)
            coordinates.IMAGE_CACHE[image] = pos
            print("cached image")
        pg.click(pos)
        pg.moveTo(coordinates.safe_spot)

    def feed(self):
        self.go_to_tab()
        helpers.click_image_on_screen(self.FEED)

    def buy_pet_food(self):
        self.go_to_tab()
        helpers.click_image_on_screen(IMAGE_DICTIONARY["buy_button"])
        time.sleep(0.1)
        helpers.click_image_on_screen(IMAGE_DICTIONARY["pet_baal_power"])
        helpers.click_image_on_screen(IMAGE_DICTIONARY["buy_max"])
        helpers.click_image_on_screen(IMAGE_DICTIONARY["yes_button"])
