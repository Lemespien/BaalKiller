""" coordinates for things ingame """
import time
import imagesearch as imgS
from image_index import IMAGE_DICTIONARY
# GLOBALS

X_PAD_DEFAULT = 629
Y_PAD_DEFAULT = 102
NRDC_FINISHED = 20
NRC_FINISHED = 20

#Creation center = X_PAD + 940, Y_PAD + 480
def find_game_window():
    print("find_game_window was called")
    found = False
    retries = 10
    while not found:
        pos = imgS.imagesearch(IMAGE_DICTIONARY["new_game_window"], 0.3)
        if pos[0] != -1:
            found = True
            print(f"find_game_window_new returned pos: {pos}")
            return pos
        pos_2 = imgS.imagesearch(IMAGE_DICTIONARY["new_game_window_2"], 0.3)
        if pos_2[0] != -1:
            found = True
            print(f"find_game_window_new returned pos_2: {pos_2}")
            return pos_2
        if retries <= 0:
            print(f"find_game_window_new stopped trying")
            break
        retries -= 1
        print(f"find_game_window_new can't find the window. Retries {retries}")
        time.sleep(.5)

class Coordinates:
    X_PAD, Y_PAD = find_game_window()

    def __init__(self):

        self.game_region = (0, 0, 970, 645)
        self.safe_spot = (823, 120)
        self.tooltip_region = (300, 50, 970, 200)
        self.clone_count_region = (15, 75, 200, 130)
        self.center_of_screen = (629, 452)

    def find_game_window(self):
        print(f"{self} called find_game_window_new")
        found = False
        retries = 10
        while not found:
            pos = imgS.imagesearch(IMAGE_DICTIONARY["new_game_window"], 0.3)
            if pos[0] != -1:
                found = True
                Coordinates.X_PAD = pos[0]
                Coordinates.Y_PAD = pos[1]
                print(f"find_game_window_new returned pos: {pos}")
                return pos
            pos_2 = imgS.imagesearch(IMAGE_DICTIONARY["new_game_window_2"], 0.3)
            if pos_2[0] != -1:
                found = True
                Coordinates.X_PAD = pos_2[0]
                Coordinates.Y_PAD = pos_2[1]
                print(f"find_game_window_new returned pos_2: {pos_2}")
                return pos_2
            if retries <= 0:
                print(f"find_game_window_new stopped trying")
                break
            retries -= 1
            print(f"find_game_window_new can't find the window. Retries {retries}")
            time.sleep(.5)

    def __getattribute__(self, attr):
        __dict__ = super(Coordinates, self).__getattribute__('__dict__')
        if attr in __dict__:
            touple = super(Coordinates, self).__getattribute__(attr)
            if isinstance(touple, tuple):
                if len(touple) == 2:
                    return (touple[0] + Coordinates.X_PAD, touple[1] + Coordinates.Y_PAD)
                if len(touple) == 4:
                    return (touple[0] + Coordinates.X_PAD, touple[1] + Coordinates.Y_PAD, touple[2] + Coordinates.X_PAD, touple[3] + Coordinates.Y_PAD)
            return touple
        return super(Coordinates, self).__getattribute__(attr)

class CloneAmounts(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.one = (580, 170)
        self.ten = (630, 170)
        self.twoHundredK = (680, 170)
        self.oneK = (730, 170)
        self.tenK = (780, 170)
        self.hundredK = (830, 170)
        self.oneM = (880, 170)
        self.maxAmount = (930, 170)


class ConfirmCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.yes = (99, 450)
        self.no = (221, 450)


class RebirthCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (152, 198)
        self.button = (89, 566)
        self.confirm = (575, 440)
        self.confirm_2 = (575, 410)
        self.confirm_3 = (575, 380)
        self.godPowerGain = (474, 571)


class PetCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (330, 117)
        self.distribute = (791, 181)
        self.feed = (895, 360)
        self.buyFoodButton = (895, 470)
        self.bpFoodOption = (420, 330)
        self.buyFoodMax = (585, 485)
        self.confirmPurchase = (95, 425)


class GodCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (510, 70)
        self.fingerFlick = (725, 170)
        self.unleash = (880, 170)
        self.fight = (775, 245)


class MonumentCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (556, 70)
        self.mightyStatuePlus = (810, 305)  # scroll at top
        self.mightyStatueMinus = (870, 305)  # scroll at top
        self.toGPlus = (810, 460)  # scroll at bottom
        self.toGMinus = (870, 460)  # scroll at bottom
        self.toGUpgradePlus = (810, 495)  # scroll at bottom
        self.toGUpgradeMinus = (870, 495)  # scroll at bottom
        self.topOfScroll = (930, 290)
        self.bottomOfScroll = (930, 610)


class CreatingCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (332, 70)
        self.light = (805, 391)
        self.weather = (805, 470)
        self.weather_scroll_position = (940, 510)
        self.nextAtOff = (822, 320)
        self.nextAt_1 = (868, 320)
        self.nextAt_2 = (914, 320)
        self.createMaxClones = (918, 174)
        self.autoBuy = (914, 200)


class DivinityCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (600, 70)
        self.divGenPlus = (780, 300)
        self.capacity = (810, 530)
        self.capacityMinus = (870, 530)
        self.gain = (810, 565)
        self.gainMinus = (870, 565)
        self.speed = (810, 600)
        self.speedMinus = (870, 600)
        self.add = (910, 285)
        self.fill = (910, 320)
        self.workerPlus = (710, 445)
        self.workerMinus = (760, 445)
        self.CAPmax = (890, 445)


class CampaignCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (375, 115)
        hour_y = 225
        self.hour_1 = (330, hour_y)
        self.hour_2 = (345, hour_y)
        self.hour_3 = (360, hour_y)
        self.hour_4 = (375, hour_y)
        self.hour_5 = (390, hour_y)
        self.hour_6 = (405, hour_y)
        self.hour_7 = (420, hour_y)
        self.hour_8 = (435, hour_y)
        self.hour_9 = (460, hour_y)
        self.hour_10 = (485, hour_y)
        self.hour_11 = (502, hour_y)
        self.hour_12 = (515, hour_y)

    #@property
    #def hour_1(self): return (self._hour_1[0] + Coordinates.X_PAD, self._hour_1[1] + Coordinates.Y_PAD)
    #@hour_1.setter
    #def hour_1(self, value): self._hour_1 = value


class DungeonCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (420, 115)
        self.dungeon_tab = (520, 180)
        self.room_duration = 15*60 * (100-NRDC_FINISHED)/100


class PlanetCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (645, 70)


class SpaceDimCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (690, 70)
        self.buy_more_button = (750, 200)
        self.buy_lowest = (775, 395)
        self.buy_middle = (775, 430)
        self.buy_max = (775, 470)
        self.region_to_check = (305, 415, 955, 570)


class BaalPartsCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.b_crit_start = (387, 301)
        self.b_crit_stop = (466, 301)
        self.b_wing_start = (368, 371)
        self.b_wing_stop = (368, 408)
        self.b_tail_start = (434, 581)
        self.b_tail_stop = (517, 581)
        self.b_feet_start = (684, 570)
        self.b_feet_stop = (766, 570)
        self.b_mouth_start = (836, 322)
        self.b_mouth_stop = (836, 367)


class BaalRegions(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.b_wing = (402, 326, 435, 477)
        self.b_tail = (397, 535, 550, 561)
        self.b_feet = (646, 522, 803, 554)
        self.b_mouth = (874, 280, 908, 435)


class BaalImages(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.b_wing_image = IMAGE_DICTIONARY["BaalKillerWing"]
        self.b_tail_image = IMAGE_DICTIONARY["BaalKillerTail"]
        self.b_feet_image = IMAGE_DICTIONARY["BaalKillerFeet"]
        self.b_mouth_image = IMAGE_DICTIONARY["BaalKillerMouth"]
