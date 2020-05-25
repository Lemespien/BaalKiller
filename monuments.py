import coordinates as c
from image_index import IMAGE_DICTIONARY
import helpers
from tabs import Tabs
import pyautogui as pg
import time


class Monuments(Tabs):
    COORDINATES = c.MonumentCords()
    PLUS = IMAGE_DICTIONARY["plus"]
    MINUS = IMAGE_DICTIONARY["minus"]
    # Top
    MIGHTY_STATUE = IMAGE_DICTIONARY["ms"]
    MYSTIC_GARDEN = IMAGE_DICTIONARY["mg"]
    TOMB_OF_GODS = IMAGE_DICTIONARY["tg"]
    EVERLASTING_LIGHTHOUSE = IMAGE_DICTIONARY["el"]
    # Bottom
    GODLY_STATUE = IMAGE_DICTIONARY["gs"]
    PYRAMID_OF_POWER = IMAGE_DICTIONARY["pop"]
    TEMPLE_OF_GOD = IMAGE_DICTIONARY["tog"]
    BLACK_HOLE = IMAGE_DICTIONARY["bh"]
    IMAGES = [MIGHTY_STATUE, MYSTIC_GARDEN, TOMB_OF_GODS, EVERLASTING_LIGHTHOUSE,
              GODLY_STATUE, PYRAMID_OF_POWER, TEMPLE_OF_GOD, BLACK_HOLE]
    TABS = [COORDINATES.tab]

    def build(self, image):
        self.go_to_tab()
        if self.IMAGES.index(image) > 3:
            helpers.scroll_to_bottom()
        else:
            helpers.scroll_to_top()
        self.add_or_remove_clones([image], click_image=self.PLUS)

    def upgrade(self, image):
        self.go_to_tab()
        if self.IMAGES.index(image) > 3:
            helpers.scroll_to_bottom()
        else:
            helpers.scroll_to_top()
        time.sleep(0.1)
        zone = self.check_if_cached(image)
        if zone == -1:
            zone = helpers.get_active_zone(image, 500, 60, self.COORDINATES)
            if zone == -1:
                return
        y_value = zone[1] + 40
        y_2_value = zone[3] + 40
        upgrade_zone = (zone[0], y_value, zone[2], y_2_value)
        helpers.click_image_in_zone(self.PLUS, zone=upgrade_zone)
