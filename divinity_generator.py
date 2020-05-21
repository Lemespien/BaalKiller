""" Holds divinity related methods """
import time
import pyautogui as pg
import coordinates as c
from image_index import IMAGE_DICTIONARY
import helpers


class Divinity:
    PLUS = IMAGE_DICTIONARY["plus"]
    DIVINITY_GAIN_IMAGE = IMAGE_DICTIONARY["div_gain"]
    DIVINITY_CONVERT_IMAGE = IMAGE_DICTIONARY["div_conv"]
    DIVINITY_CAPACITY_IMAGE = IMAGE_DICTIONARY["div_capacity"]
    CLONES_TO_USE_IMAGE = IMAGE_DICTIONARY["clones_use"]
    CLONE_INPUT_IMAGE = IMAGE_DICTIONARY["clone_input"]

    def __init__(self, coordinates=-1):
        if coordinates == -1:
            self.COORDINATES = c.DivinityCords()
        else:
            self.COORDINATES = coordinates
        pg.click(self.COORDINATES.tab)
        self.is_constructed = self.check_if_constructed()

    def check_if_constructed(self):
        pg.click(self.COORDINATES.tab)
        pos = helpers.return_position_of_image_on_screen(IMAGE_DICTIONARY["div_gen_uc"])
        pos_2 = helpers.return_position_of_image_on_screen(IMAGE_DICTIONARY["div_gen_constructed"])
        if pos[0] != -1:
            return False
        elif pos_2[0] != -1:
            return True
        else:
            return True

    def construct(self):
        pg.click(self.COORDINATES.tab)
        helpers.click_image_on_screen(Divinity.PLUS)
        self.is_constructed = True

    def construct_upgrades(self):
        coordinates = self.COORDINATES
        zone_x_width = 500
        zone_y_height = 50
        current_clones = get_clone_count(coordinates)
        clones_on_capacity = round(current_clones/20)
        current_clones -= clones_on_capacity
        clones_on_upgrades = round(current_clones/2)
        print(current_clones)
        time.sleep(0.1)
        clones_use_zone = self.get_active_zone(Divinity.CLONES_TO_USE_IMAGE, 200, 50, coordinates)
        self.change_clone_use_amount(clones_on_upgrades, clones_use_zone)
        self.add_clones_to_upgrade(Divinity.DIVINITY_GAIN_IMAGE, zone_x_width, zone_y_height)
        self.add_clones_to_upgrade(Divinity.DIVINITY_CONVERT_IMAGE, zone_x_width, zone_y_height)
        # set clones to 1/20 of current
        self.change_clone_use_amount(clones_on_capacity, clones_use_zone)
        self.add_clones_to_upgrade(Divinity.DIVINITY_CAPACITY_IMAGE, zone_x_width, zone_y_height)

    def get_active_zone(self, image, x_length, y_height, coordinates=-1):
        if coordinates == -1:
            coordinates = self.COORDINATES
        pos = helpers.return_position_of_image_on_screen(image, coordinates)
        x = round(pos[0])
        y = round(pos[1]) - 25
        action_region = (x, y, x + x_length, y + y_height)
        return action_region

    def change_clone_use_amount(self, amount, zone):
        helpers.click_image_in_zone(Divinity.CLONE_INPUT_IMAGE, zone=zone)
        helpers.click_image_in_zone(Divinity.CLONE_INPUT_IMAGE, zone=zone)
        pg.write(str(amount))

    def add_clones_to_upgrade(self, image, zone_x_width=500, zone_y_height=50, click_image=None):
        coordinates = self.COORDINATES
        zone = self.get_active_zone(image, zone_x_width, zone_y_height, coordinates)
        helpers.click_image_in_zone(click_image, zone=zone)


def get_clone_count(coordinates=-1):
    if coordinates == -1:
        coordinates = c.Coordinates()
    clone_count_image = helpers.get_image_from_zone(coordinates.clone_count_region)
    text = helpers.get_text_from_image(clone_count_image)
    split_text = text.split()
    try:
        index_of_slash = split_text.index("/")
        clone_count = int(split_text[index_of_slash-1].replace(",", ""))

    except ValueError:
        print(text)
        print("Clone error?")
        return -1
    return clone_count


def build_div_generator():
    """ Start construction of div generator """
    cords = c.DivinityCords()
    pg.click(cords.tab)
    pg.click(cords.divGenPlus)


def div_gen_loop():
    """ Add clones to construction of div generator upgrades """

    cords = c.DivinityCords()
    pg.click(cords.tab)
    add_to_div_gen()
    pg.click(cords.gain)
    time.sleep(1)
    add_clones_to_div_construct()
    add_to_div_gen()


def add_to_div_gen():
    """ Simply adds charge to the divinity generator """
    cords = c.DivinityCords()
    pg.click(cords.tab)
    pg.click(cords.add)


def add_clones_to_div_construct():
    """ Adds 200k clones to both gain and speed upgrade construction """
    cords = c.DivinityCords()
    pg.click(cords.tab)
    pg.click(c.CloneAmounts().twoHundredK)
    for _ in range(10):
        pg.click(cords.gain)
        pg.click(cords.speed)
    pg.click(cords.capacity)


def remove_clones_from_div_construct():
    cords = c.DivinityCords()
    pg.click(cords.tab)
    pg.click(c.CloneAmounts().maxAmount)
    time.sleep(0.1)
    pg.click(cords.gainMinus)
    time.sleep(0.1)
    pg.click(cords.speedMinus)
    time.sleep(0.1)
    pg.click(cords.capacityMinus)


def add_workers_to_div_gen():
    cords = c.DivinityCords()
    pg.click(cords.tab)
    pg.click(cords.CAPmax)
    time.sleep(0.1)
    pg.click(cords.fill)
    for _ in range(5):
        time.sleep(2)
        pg.click(cords.fill)


def remove_workers_from_div_gen():
    cords = c.DivinityCords()
    pg.click(cords.tab)
    time.sleep(0.1)
    pg.click(c.CloneAmounts().maxAmount)
    time.sleep(0.1)
    pg.click(cords.workerMinus)
