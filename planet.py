import time
import pyautogui as pg
import coordinates as c
import imagesearch as imgS
IMAGE_FOLDER = "images/"


def add_clones_to_power_surge():
    cords = c.PlanetCords()
    pg.click(cords.tab)
    time.sleep(0.1)
    pg.click(cords.UBsTab)
    time.sleep(0.1)
    pg.click(cords.power_surge_cap)


def remove_clones_from_power_surge():
    cords = c.PlanetCords()
    pg.click(cords.tab)
    time.sleep(0.1)
    pg.click(cords.UBsTab)
    time.sleep(0.1)
    pg.click(c.cloneAmounts().maxAmount)
    time.sleep(0.1)
    pg.click(cords.power_surge_minus)


def fight_ub():
    cords = c.PlanetCords()
    pg.click(cords.tab)
    time.sleep(0.1)
    pg.click(cords.UBsTab)
    time.sleep(0.1)
    pg.click(cords.PEFight)
    time.sleep(0.1)
    pg.click(cords.GTFight)
