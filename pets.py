import coordinates as c
from image_index import IMAGE_DICTIONARY
import helpers
from tabs import Tabs


class Pets(Tabs):
    COORDINATES = c.PetCords()
    DISTRIBUTE = IMAGE_DICTIONARY["distribute"]
    FEED = IMAGE_DICTIONARY["feed"]
    TABS = [COORDINATES.tab]

    def distribute(self):
        self.go_to_tab()
        helpers.click_image_on_screen(self.DISTRIBUTE)

    def feed(self):
        self.go_to_tab()
        helpers.click_image_on_screen(self.FEED)
