""" Holds divinity related methods """
import time
import pyautogui as pg
import coordinates as c
from image_index import IMAGE_DICTIONARY
import helpers
from tabs import Tabs


class Divinity(Tabs):
    COORDINATES = c.DivinityCords()
    PLUS = IMAGE_DICTIONARY["plus"]
    MINUS = IMAGE_DICTIONARY["minus"]
    GAIN_IMAGE = IMAGE_DICTIONARY["div_gain"]
    CONVERT_IMAGE = IMAGE_DICTIONARY["div_conv"]
    CAPACITY_IMAGE = IMAGE_DICTIONARY["div_capacity"]
    WORKER_CLONES_IMAGE = IMAGE_DICTIONARY["worker_clones"]
    CLONES_TO_USE_IMAGE = IMAGE_DICTIONARY["clones_use"]
    CLONE_INPUT_IMAGE = IMAGE_DICTIONARY["clone_input"]
    image_cache = {}
    TABS = [COORDINATES.tab]

    def __init__(self, name):
        super().__init__(name)
        self.go_to_tab()
        self.is_constructed = self.check_if_constructed()

    def check_if_constructed(self):
        self.go_to_tab()
        pos = helpers.return_position_of_image_on_screen(IMAGE_DICTIONARY["div_gen_uc"])
        pos_2 = helpers.return_position_of_image_on_screen(IMAGE_DICTIONARY["div_gen_constructed"])
        if pos[0] != -1:
            return False
        elif pos_2[0] != -1:
            return True
        else:
            return True

    def construct(self):
        self.go_to_tab()
        helpers.click_image_on_screen(Divinity.PLUS)
        self.is_constructed = True

    def construct_upgrades(self):
        self.go_to_tab()
        coordinates = self.COORDINATES
        zone_x_width = 500
        zone_y_height = 60
        current_clones = helpers.get_clone_count(coordinates)
        if current_clones == -1:
            current_clones = 100000
        clones_on_capacity = round(current_clones/20)
        current_clones -= clones_on_capacity
        clones_on_upgrades = round(current_clones/2)
        clones_to_use_image = Divinity.CLONES_TO_USE_IMAGE
        clones_use_zone = self.check_if_cached(clones_to_use_image)
        # ugly as
        if clones_use_zone != -1:
            self.change_clone_use_amount(clones_on_upgrades, clones_use_zone)
        elif clones_use_zone == -1:
            clones_use_zone = helpers.get_active_zone(clones_to_use_image, 200, zone_y_height, coordinates)
            if clones_use_zone == -1:
                pg.click(c.CloneAmounts().twoHundredK)
            else:
                self.cache_image(clones_to_use_image, clones_use_zone)
                self.change_clone_use_amount(clones_on_upgrades, clones_use_zone)
        ##
        images = [Divinity.GAIN_IMAGE, Divinity.CONVERT_IMAGE]
        self.add_or_remove_clones(images, zone_x_width, zone_y_height, Divinity.PLUS)
        # set clones to 1/20 of current
        self.change_clone_use_amount(clones_on_capacity, clones_use_zone)
        self.add_or_remove_clones([Divinity.CAPACITY_IMAGE], zone_x_width, zone_y_height, Divinity.PLUS)

    def add_to_div(self):
        self.go_to_tab()
        helpers.click_image_on_screen(IMAGE_DICTIONARY["add2"])
        pg.moveTo(self.COORDINATES.safe_spot)

    def cap_max(self):
        self.go_to_tab()
        helpers.click_image_on_screen(IMAGE_DICTIONARY["cap_max"])
        helpers.click_image_on_screen(IMAGE_DICTIONARY["fill"])
        self.add_to_div()

    def change_clone_use_amount(self, amount, zone):
        helpers.click_image_in_zone(Divinity.CLONE_INPUT_IMAGE, clicks=2, zone=zone)
        pg.write(str(amount))

    def remove_all_clones(self):
        self.go_to_tab()
        helpers.click_image_on_screen(IMAGE_DICTIONARY["max"])
        images = [Divinity.GAIN_IMAGE, Divinity.CAPACITY_IMAGE, Divinity.CONVERT_IMAGE, Divinity.WORKER_CLONES_IMAGE]
        self.add_or_remove_clones(images, 500, 50, Divinity.MINUS)
