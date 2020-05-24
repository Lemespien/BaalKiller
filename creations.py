import coordinates as c
from image_index import IMAGE_DICTIONARY
import helpers
from tabs import Tabs
import pyautogui as pg
import time


class Creations(Tabs):
    COORDINATES = c.CreatingCords()
    CREATE = IMAGE_DICTIONARY["create"]
    BUY = IMAGE_DICTIONARY["buy_button"]
    NA_OFF = IMAGE_DICTIONARY["creation_off"]
    NA_ONE = IMAGE_DICTIONARY["creation_1"]
    NA_TWO = IMAGE_DICTIONARY["creation_2"]
    CREATE_CLONES_MAX = IMAGE_DICTIONARY["create_clones_max"]
    CREATE_CLONES_ON = IMAGE_DICTIONARY["afky_on"]
    CREATE_CLONES_OFF = IMAGE_DICTIONARY["afky_off"]

    SHADOW_CLONES = IMAGE_DICTIONARY["shadow_clones"]
    LIGHT = IMAGE_DICTIONARY["light"]
    NATION = IMAGE_DICTIONARY["nation"]
    WEATHER = IMAGE_DICTIONARY["weather"]
    GALAXY = IMAGE_DICTIONARY["galaxy"]
    UNIVERSE = IMAGE_DICTIONARY["universe"]
    IMAGES = [LIGHT, NATION, WEATHER, GALAXY, UNIVERSE]
    TABS = [COORDINATES.tab]

    def create(self, image):
        """ Will start creating given element, regardless of next at setting """
        self.go_to_tab()
        coordinates = self.COORDINATES
        helpers.scroll_to_top()
        if self.IMAGES.index(image) >= self.IMAGES.index(self.NATION):
            pg.moveTo(coordinates.center_of_screen)
            pg.scroll(-2300)  # magic number for weather scroll positions
        elif self.IMAGES.index(image) > self.IMAGES.index(self.WEATHER):
            helpers.scroll_to_bottom()
        zone = helpers.get_active_zone(image, 500, 60, coordinates)
        helpers.click_image_in_zone(self.CREATE, zone=zone)

    def create_specific(self, image):
        """ Will set next at to off """
        self.go_to_tab()
        helpers.click_image_on_screen(self.NA_OFF, self.COORDINATES)
        self.create(image)

    def create_progress(self, image):
        """ Will set next at to 2 """
        self.go_to_tab()
        helpers.click_image_on_screen(self.NA_TWO, self.COORDINATES)
        self.create(image)

    def create_clones_on(self):
        self.go_to_tab()
        zone = helpers.get_active_zone(self.CREATE_CLONES_MAX, 500, 60, self.COORDINATES)
        helpers.click_image_in_zone(self.CREATE_CLONES_OFF, zone=zone)

    def create_clones_off(self):
        self.go_to_tab()
        zone = helpers.get_active_zone(self.CREATE_CLONES_MAX, 500, 60, self.COORDINATES)
        helpers.click_image_in_zone(self.CREATE_CLONES_ON, zone=zone)

    def check_if_idle(self):
        """ Defaults to create weather if idle """
        self.go_to_tab()
        pos = helpers.return_position_of_image_on_screen(IMAGE_DICTIONARY["creating_shadow_clones"], self.COORDINATES)
        if pos[0] != -1:
            # We're creating shadow clones
            return True
        else:
            # We're still in the cycle
            return False

    # def upgrade(self, image):
    #     self.go_to_tab()
    #     if self.IMAGES.index(image) > 1:
    #         helpers.scroll_to_bottom()
    #     else:
    #         helpers.scroll_to_top()
    #     time.sleep(0.1)
    #     zone = helpers.get_active_zone(image, 500, 60, self.COORDINATES)
    #     y_value = zone[1] + 40
    #     y_2_value = zone[3] + 40
    #     upgrade_zone = (zone[0], y_value, zone[2], y_2_value)
    #     helpers.click_image_in_zone(self.PLUS, zone=upgrade_zone)

    # def add_or_remove_clones(self, images, zone_x_width=500, zone_y_height=60, click_image=None):
    #     coordinates = self.COORDINATES
    #     for image in images:
    #         zone = helpers.get_active_zone(image, zone_x_width, zone_y_height, coordinates)
    #         helpers.click_image_in_zone(click_image, zone=zone)
