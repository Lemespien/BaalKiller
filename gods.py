import coordinates as c
from image_index import IMAGE_DICTIONARY
import helpers
from tabs import Tabs


class Gods(Tabs):
    COORDINATES = c.GodCords()
    FINGER_FLICK = IMAGE_DICTIONARY["finger_flick"]
    FIGHT = IMAGE_DICTIONARY["fight"]
    TABS = [COORDINATES.tab]

    def finger_flick(self):
        self.go_to_tab()
        helpers.click_image_on_screen(self.FINGER_FLICK)

    def fight(self):
        self.go_to_tab()
        helpers.click_image_on_screen(self.FIGHT)
