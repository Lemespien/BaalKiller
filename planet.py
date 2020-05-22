import time
import pyautogui as pg
import coordinates as c
import imagesearch as imgS
from image_index import IMAGE_DICTIONARY
import helpers
IMAGE_FOLDER = "images/"


class Planet:
    COORDINATES = c.PlanetCords()
    TIMER = helpers.TimerClass("Planet", 60 * 60 * (100-c.NRC_FINISHED)/100 + 5)
    PLUS = IMAGE_DICTIONARY["plus"]
    MINUS = IMAGE_DICTIONARY["minus"]
    CAP = IMAGE_DICTIONARY["cap"]
    FIGHT = IMAGE_DICTIONARY["fight"]
    UBS = IMAGE_DICTIONARY["ubs"]
    UBSV2 = IMAGE_DICTIONARY["ubs_v2"]
    CRYSTAL = IMAGE_DICTIONARY["crystal"]
    UP_ALL = IMAGE_DICTIONARY["up_all"]
    LEVEL = IMAGE_DICTIONARY["level"]
    MAX_ALL = IMAGE_DICTIONARY["max_all"]
    EQUIP_ALL = IMAGE_DICTIONARY["equip_all"]
    PE = IMAGE_DICTIONARY["pe"]
    GT = IMAGE_DICTIONARY["gt"]
    LS = IMAGE_DICTIONARY["ls"]
    GAA = IMAGE_DICTIONARY["gaa"]
    ITRTG = IMAGE_DICTIONARY["itrtg"]
    POWER_SURGING = False

    def power_surge(self):
        coordinates = Planet.COORDINATES
        pg.click(coordinates.tab)
        helpers.click_image_on_screen(Planet.UBS, coordinates)
        helpers.click_image_on_screen(Planet.CAP, coordinates)
        Planet.POWER_SURGING = True

    def remove_clones(self):
        """ self explanatory """
        coordinates = Planet.COORDINATES
        pg.click(coordinates.tab)
        images = [IMAGE_DICTIONARY["max"], Planet.UBS, Planet.MINUS]
        for image in images:
            helpers.click_image_on_screen(image, coordinates)
        Planet.POWER_SURGING = False

    def fight_UB(self):
        """ Checks if the UBs are active and then fights them"""
        if Planet.POWER_SURGING:
            coordinates = Planet.COORDINATES
            pg.click(coordinates.tab)
            images = [Planet.PE, Planet.GT, Planet.LS, Planet.GAA, Planet.ITRTG]
            for image in images:
                zone = helpers.get_active_zone(image, 600, 70, coordinates)
                if zone == -1:
                    print("Ub not active")
                    continue
                helpers.click_image_in_zone(Planet.FIGHT, zone=zone)
            pg.click(Planet.CAP)

    def create_crystals(self):
        """ Uses the auto level feature """
        coordinates = Planet.COORDINATES
        pg.click(coordinates.tab)
        images = [Planet.CRYSTAL, Planet.UP_ALL, Planet.LEVEL]
        for image in images:
            helpers.click_image_on_screen(image, coordinates)

    def upgrade_crystals(self):
        """ Uses the auto upgrade feature """
        coordinates = Planet.COORDINATES
        pg.click(coordinates.tab)
        helpers.click_image_on_screen(Planet.CRYSTAL, coordinates)
        helpers.scroll_to_bottom(coordinates)
        pg.scroll(500)
        print("sleeping")
        time.sleep(5)
        helpers.click_image_on_screen(Planet.MAX_ALL, coordinates)


    def equip_crystals(self):
        """ Uses the auto equip feature """
        coordinates = Planet.COORDINATES
        pg.click(coordinates.tab)
        helpers.click_image_on_screen(Planet.CRYSTAL, coordinates)
        helpers.scroll_to_bottom(coordinates)
        pg.scroll(500)
        helpers.click_image_on_screen(Planet.EQUIP_ALL, coordinates)

