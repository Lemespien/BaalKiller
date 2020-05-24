import coordinates as c
from image_index import IMAGE_DICTIONARY
import helpers
from tabs import Tabs
import time


class Rebirth(Tabs):
    COORDINATES = c.RebirthCords()
    DISTRIBUTE = IMAGE_DICTIONARY["distribute"]
    FEED = IMAGE_DICTIONARY["feed"]
    TABS = [COORDINATES.tab]

    def rebirth(self):
        self.go_to_tab()
        helpers.click_image_on_screen(IMAGE_DICTIONARY["rebirth"])
        helpers.click_image_on_screen(IMAGE_DICTIONARY["yes_button"])
