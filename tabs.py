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
        Tabs.CORD_LAST_UPDATE = time.time()
        print(f"{self.name} last update was {time.time() - self.CORD_LAST_UPDATE} ago")
        print(f"{self.name} called for a cord update at {helpers.time_format(self.CORD_LAST_UPDATE)}")

    def go_to_tab(self):
        if time.time() - self.CORD_LAST_UPDATE > Tabs.CORD_UPDATE_THRESHOLD:
            self.update_cords()
        for tab in self.TABS:
            pg.click(tab)
        pg.moveTo(self.COORDINATES.safe_spot)
