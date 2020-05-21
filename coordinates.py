""" coordinates for things ingame """
import time
import imagesearch as imgS
from image_index import IMAGE_DICTIONARY
# GLOBALS

X_PAD_DEFAULT = 629
Y_PAD_DEFAULT = 102
NRDC_FINISHED = 19


class Coordinates:
    def __init__(self):
        self.x_pad = X_PAD_DEFAULT
        self.y_pad = Y_PAD_DEFAULT
        self.find_game_window_new()
        self.game_region = (self.x_pad, self.y_pad, self.x_pad + 1280, self.y_pad + 645)
        self.safe_spot = (self.x_pad + 823, self.y_pad + 120)
        self.tooltip_region = (self.x_pad + 300, self.y_pad + 50, self.x_pad + 970, self.y_pad + 200)
        self.clone_count_region = (self.x_pad + 15, self.y_pad + 75, self.x_pad + 200, self.y_pad + 130)

    def find_game_window_new(self):
        print(f"{self} called find_game_window_new")
        found = False
        retries = 10
        while not found:
            pos = imgS.imagesearch(IMAGE_DICTIONARY["new_game_window"], 0.3)
            if pos[0] != -1:
                found = True
                self.x_pad = pos[0]
                self.y_pad = pos[1]
                print(f"find_game_window_new returned pos: {pos}")
                return pos
            pos_2 = imgS.imagesearch(IMAGE_DICTIONARY["new_game_window_2"], 0.3)
            if pos_2[0] != -1:
                found = True
                self.x_pad = pos_2[0]
                self.y_pad = pos_2[1]
                print(f"find_game_window_new returned pos_2: {pos_2}")
                return pos_2
            if retries <= 0:
                print(f"find_game_window_new stopped trying")
                break
            retries -= 1
            print(f"find_game_window_new can't find the window. Retries {retries}")
            time.sleep(.5)


class CloneAmounts(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.one = (self.x_pad + 580, self.y_pad + 170)
        self.ten = (self.x_pad + 630, self.y_pad + 170)
        self.twoHundredK = (self.x_pad + 680, self.y_pad + 170)
        self.oneK = (self.x_pad + 730, self.y_pad + 170)
        self.tenK = (self.x_pad + 780, self.y_pad + 170)
        self.hundredK = (self.x_pad + 830, self.y_pad + 170)
        self.oneM = (self.x_pad + 880, self.y_pad + 170)
        self.maxAmount = (self.x_pad + 930, self.y_pad + 170)


class ConfirmCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.yes = (self.x_pad + 99, self.y_pad + 450)
        self.no = (self.x_pad + 221, self.y_pad + 450)


class RebirthCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (self.x_pad + 152, self.y_pad + 198)
        self.button = (self.x_pad + 89, self.y_pad + 566)
        self.confirm = (self.x_pad + 575, self.y_pad + 440)
        self.confirm_2 = (self.x_pad + 575, self.y_pad + 410)
        self.confirm_3 = (self.x_pad + 575, self.y_pad + 380)
        self.godPowerGain = (self.x_pad + 474, self.y_pad + 571)


class PetCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (self.x_pad + 330, self.y_pad + 117)
        self.distribute = (self.x_pad + 791, self.y_pad + 181)
        self.feed = (self.x_pad + 895, self.y_pad + 360)
        self.buyFoodButton = (self.x_pad + 895, self.y_pad + 470)
        self.bpFoodOption = (self.x_pad + 420, self.y_pad + 330)
        self.buyFoodMax = (self.x_pad + 585, self.y_pad + 485)
        self.confirmPurchase = (self.x_pad + 95, self.y_pad + 425)


class GodCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (self.x_pad + 510, self.y_pad + 70)
        self.fingerFlick = (self.x_pad + 725, self.y_pad + 170)
        self.unleash = (self.x_pad + 880, self.y_pad + 170)
        self.fight = (self.x_pad + 775, self.y_pad + 245)


class MonumentCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (self.x_pad + 556, self.y_pad + 70)
        self.mightyStatuePlus = (self.x_pad + 810, self.y_pad + 305)  # scroll at top
        self.mightyStatueMinus = (self.x_pad + 870, self.y_pad + 305)  # scroll at top
        self.toGPlus = (self.x_pad + 810, self.y_pad + 460)  # scroll at bottom
        self.toGMinus = (self.x_pad + 870, self.y_pad + 460)  # scroll at bottom
        self.toGUpgradePlus = (self.x_pad + 810, self.y_pad + 495)  # scroll at bottom
        self.toGUpgradeMinus = (self.x_pad + 870, self.y_pad + 495)  # scroll at bottom
        self.topOfScroll = (self.x_pad + 930, self.y_pad + 290)
        self.bottomOfScroll = (self.x_pad + 930, self.y_pad + 610)


class CreatingCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (self.x_pad + 332, self.y_pad + 70)
        self.light = (self.x_pad + 805, self.y_pad + 391)
        self.weather = (self.x_pad + 805, self.y_pad + 470)
        self.weather_scroll_position = (self.x_pad + 940, self.y_pad + 510)
        self.nextAtOff = (self.x_pad + 822, self.y_pad + 320)
        self.nextAt_1 = (self.x_pad + 868, self.y_pad + 320)
        self.nextAt_2 = (self.x_pad + 914, self.y_pad + 320)
        self.createMaxClones = (self.x_pad + 918, self.y_pad + 174)
        self.autoBuy = (self.x_pad + 914, self.y_pad + 200)


class DivinityCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (self.x_pad + 600, self.y_pad + 70)
        self.divGenPlus = (self.x_pad + 780, self.y_pad + 300)
        self.capacity = (self.x_pad + 810, self.y_pad + 530)
        self.capacityMinus = (self.x_pad + 870, self.y_pad + 530)
        self.gain = (self.x_pad + 810, self.y_pad + 565)
        self.gainMinus = (self.x_pad + 870, self.y_pad + 565)
        self.speed = (self.x_pad + 810, self.y_pad + 600)
        self.speedMinus = (self.x_pad + 870, self.y_pad + 600)
        self.add = (self.x_pad + 910, self.y_pad + 285)
        self.fill = (self.x_pad + 910, self.y_pad + 320)
        self.workerPlus = (self.x_pad + 710, self.y_pad + 445)
        self.workerMinus = (self.x_pad + 760, self.y_pad + 445)
        self.CAPmax = (self.x_pad + 890, self.y_pad + 445)


class CampaignCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (self.x_pad + 375, self.y_pad + 115)
        self.growth = (self.x_pad + 640, self.y_pad + 185)
        self.divinity = (self.x_pad + 640, self.y_pad + 230)
        self.food = (self.x_pad + 640, self.y_pad + 275)
        self.item = (self.x_pad + 640, self.y_pad + 320)
        self.level = (self.x_pad + 640, self.y_pad + 365)
        self.multiplier = (self.x_pad + 640, self.y_pad + 410)
        self.god_power = (self.x_pad + 640, self.y_pad + 455)
        hour_y = 225
        self.hour_1 = (self.x_pad + 330, self.y_pad + hour_y)
        self.hour_2 = (self.x_pad + 345, self.y_pad + hour_y)
        self.hour_3 = (self.x_pad + 360, self.y_pad + hour_y)
        self.hour_4 = (self.x_pad + 375, self.y_pad + hour_y)
        self.hour_5 = (self.x_pad + 390, self.y_pad + hour_y)
        self.hour_6 = (self.x_pad + 405, self.y_pad + hour_y)
        self.hour_7 = (self.x_pad + 420, self.y_pad + hour_y)
        self.hour_8 = (self.x_pad + 435, self.y_pad + hour_y)
        self.hour_9 = (self.x_pad + 460, self.y_pad + hour_y)
        self.hour_10 = (self.x_pad + 485, self.y_pad + hour_y)
        self.hour_11 = (self.x_pad + 502, self.y_pad + hour_y)
        self.hour_12 = (self.x_pad + 515, self.y_pad + 225)
        self.auto_select = (self.x_pad + 640, self.y_pad + 260)
        self.growt_padding = 35
        self.padding = 25
        self.restart_offset = 90  # campaign cord (x - 90)
        # growth campaign cords + growth padding
        self.growth_result = (self.x_pad + 640, self.y_pad + 220)
        self.close_result = (self.x_pad + 475, self.y_pad + 575)
        self.mighty_food = (self.x_pad + 755, self.y_pad + 350)
        self.mayonaise = (self.x_pad + 870, self.y_pad + 440)
        self.campaign_feed = (self.x_pad + 490, self.y_pad + 500)
        self.no_feed = (self.x_pad + 640, self.y_pad + 500)
        self.check_region_complete = (self.x_pad + 586, self.y_pad + 150, self.x_pad + 684, self.y_pad + 572)
        self.campaign_text_region = (self.x_pad + 305, self.y_pad + 155, self.x_pad + 550, self.y_pad + 545)


class DungeonCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (self.x_pad + 420, self.y_pad + 115)
        self.dungeon_tab = (self.x_pad + 520, self.y_pad + 180)
        self.newbie = (self.x_pad + 570, self.y_pad + 300)
        self.water = (self.x_pad + 570, self.y_pad + 345)
        self.volcano = (self.x_pad + 570, self.y_pad + 390)
        self.mountain = (self.x_pad + 570, self.y_pad + 435)
        self.forest = (self.x_pad + 570, self.y_pad + 475)
        self.start = (self.x_pad + 875, self.y_pad + 605)
        self.room_1 = (self.x_pad + 505, self.y_pad + 575)  # only need this one + room_count_offset_less_than_10
        self.room_6 = (self.x_pad + 530, self.y_pad + 575)  # not needed
        self.room_16 = (self.x_pad + 578, self.y_pad + 575)  # not needed
        self.room_18 = (self.x_pad + 588, self.y_pad + 575)  # not needed
        self.difficulty_0 = (self.x_pad + 330, self.y_pad + 575)  # only need this one + difficulty_count_offset
        self.difficulty_1 = (self.x_pad + 340, self.y_pad + 575)  # not needed
        self.difficulty_2 = (self.x_pad + 353, self.y_pad + 575)  # not needed
        self.difficulty_3 = (self.x_pad + 360, self.y_pad + 575)  # not needed
        self.difficulty_4 = (self.x_pad + 370, self.y_pad + 575)  # not needed
        self.difficulty_5 = (self.x_pad + 380, self.y_pad + 575)  # not needed
        self.difficulty_6 = (self.x_pad + 390, self.y_pad + 575)  # not needed
        self.difficulty_7 = (self.x_pad + 400, self.y_pad + 575)  # not needed
        self.difficulty_8 = (self.x_pad + 410, self.y_pad + 575)  # not needed
        self.difficulty_9 = (self.x_pad + 420, self.y_pad + 575)  # not needed
        self.difficulty_10 = (self.x_pad + 435, self.y_pad + 575)  # not needed
        self.finish_offset = 90  # In x direction
        self.room_count_offset_less_than_10 = 4.2  # for rooms less than 10
        self.room_greater_than_10_offset = 4.4  # for rooms greater/equal to 10
        self.difficulty_count_offset = 10.5  # rounding to 11 ?
        self.close_result = (self.x_pad + 870, self.y_pad + 185)
        self.next_team = (self.x_pad + 890, self.y_pad + 240)
        self.region = (self.x_pad + 315, self.y_pad + 120, self.x_pad + 860, self.y_pad + 260)
        self.items_back_button = (self.x_pad + 675, self.y_pad + 240)
        self.room_duration = 15*60 * (100-NRDC_FINISHED)/100
        self.padding = 25
        self.check_region_complete = (self.x_pad + 610, self.y_pad + 220, self.x_pad + 725, self.y_pad + 515)


class PlanetCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (self.x_pad + 645, self.y_pad + 70)
        self.UBsTab = (self.x_pad + 650, self.y_pad + 205)
        self.UBsV2Tab = (self.x_pad + 735, self.y_pad + 205)
        self.UBsV4Tab = (self.x_pad + 820, self.y_pad + 205)
        self.crystalTab = (self.x_pad + 900, self.y_pad + 205)
        self.power_surge_cap = (self.x_pad + 860, self.y_pad + 310)
        self.power_surge_minus = (self.x_pad + 810, self.y_pad + 310)
        self.PEFight = (self.x_pad + 880, self.y_pad + 390)
        self.GTFight = (self.x_pad + 880, self.y_pad + 425)
        self.LSFight = (self.x_pad + 880, self.y_pad + 460)
        self.ITRTGFight = (self.x_pad + 880, self.y_pad + 495)


class SpaceDimCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.tab = (self.x_pad + 690, self.y_pad + 70)
        self.buy_more_button = (self.x_pad + 750, self.y_pad + 200)
        self.buy_lowest = (self.x_pad + 775, self.y_pad + 395)
        self.buy_middle = (self.x_pad + 775, self.y_pad + 430)
        self.buy_max = (self.x_pad + 775, self.y_pad + 470)
        self.region_to_check = (self.x_pad + 305, self.y_pad + 415, self.x_pad + 955, self.y_pad + 570)


class BaalPartsCords(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.b_crit_start = (self.x_pad + 387, self.y_pad + 301)
        self.b_crit_stop = (self.x_pad + 466, self.y_pad + 301)
        self.b_wing_start = (self.x_pad + 368, self.y_pad + 371)
        self.b_wing_stop = (self.x_pad + 368, self.y_pad + 408)
        self.b_tail_start = (self.x_pad + 434, self.y_pad + 581)
        self.b_tail_stop = (self.x_pad + 517, self.y_pad + 581)
        self.b_feet_start = (self.x_pad + 684, self.y_pad + 570)
        self.b_feet_stop = (self.x_pad + 766, self.y_pad + 570)
        self.b_mouth_start = (self.x_pad + 836, self.y_pad + 322)
        self.b_mouth_stop = (self.x_pad + 836, self.y_pad + 367)


class BaalRegions(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.b_wing = (self.x_pad + 402, self.y_pad + 326, self.x_pad + 435, self.y_pad + 477)
        self.b_tail = (self.x_pad + 397, self.y_pad + 535, self.x_pad + 550, self.y_pad + 561)
        self.b_feet = (self.x_pad + 646, self.y_pad + 522, self.x_pad + 803, self.y_pad + 554)
        self.b_mouth = (self.x_pad + 874, self.y_pad + 280, self.x_pad + 908, self.y_pad + 435)


class BaalImages(Coordinates):
    def __init__(self):
        Coordinates.__init__(self)
        self.b_wing_image = IMAGE_DICTIONARY["BaalKillerWing"]
        self.b_tail_image = IMAGE_DICTIONARY["BaalKillerTail"]
        self.b_feet_image = IMAGE_DICTIONARY["BaalKillerFeet"]
        self.b_mouth_image = IMAGE_DICTIONARY["BaalKillerMouth"]
