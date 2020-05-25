import time
import pyautogui as pg
import coordinates as c
import helpers


class Tabs:
    COORDINATES = c.Coordinates()
    CORD_LAST_UPDATE = time.time()
    CORD_UPDATE_THRESHOLD = 60
    TABS = []

    def __init__(self, name):
        self.name = name

    def get_cords(self):
        if time.time() - self.CORD_LAST_UPDATE > Tabs.CORD_UPDATE_THRESHOLD:
            self.update_cords()
        return self.COORDINATES

    def update_cords(self):
        Tabs.COORDINATES.find_game_window()
        print(f"{self.name} last update was {time.time() - self.CORD_LAST_UPDATE} ago")
        print(f"{self.name} called for a cord update at {helpers.time_format()}")
        Tabs.CORD_LAST_UPDATE = time.time()

    def go_to_tab(self):
        if time.time() - self.CORD_LAST_UPDATE > Tabs.CORD_UPDATE_THRESHOLD:
            self.update_cords()
        for tab in self.TABS:
            pg.click(tab)
        pg.moveTo(self.COORDINATES.safe_spot)

    def add_or_remove_clones(self, images, zone_x_width=500, zone_y_height=60, click_image=None):
        coordinates = self.COORDINATES
        for image in images:
            zone = self.check_if_cached(image)
            if zone == -1:
                zone = helpers.get_active_zone(image, zone_x_width, zone_y_height, coordinates)
                if zone == -1:
                    return
                self.cache_image(image, zone)
            helpers.click_image_in_zone(click_image, zone=zone)
            pg.moveTo(coordinates.safe_spot)

    def check_if_cached(self, image):
        if image in self.COORDINATES.IMAGE_CACHE:
            return self.COORDINATES.IMAGE_CACHE[image]
        return -1

    def cache_image(self, image, value):
        self.COORDINATES.IMAGE_CACHE[image] = value
