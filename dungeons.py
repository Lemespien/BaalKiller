""" Dungeon related module """
import time
import pyautogui as pg
import coordinates as c
import imagesearch as imgS
from image_index import IMAGE_DICTIONARY
import helpers


class Dungeon:
    """ Dungeon class to hold dungeon stuff """
    name = ''
    depth = '1'
    rooms = '6'
    difficulty = '1'
    current_duration = ''
    duration = '6'
    team = ''

    def __init__(self, name, team, depth=1, rooms=6, difficulty=1):
        self.name = name
        self.depth = depth
        self.rooms = rooms
        self.difficulty = difficulty
        self.team = team

    def check_if_correct_team(self, main_coordinates=-1):
        if main_coordinates == -1:
            main_coordinates = c.Coordinates()
        next_button_cord = helpers.add_screen_padding(
            helpers.find_image_in_game_window(IMAGE_DICTIONARY["next_button"], cords=main_coordinates),
            main_coordinates)
        new_value = (next_button_cord[0] + 26, next_button_cord[1] + 18)
        current_team = new_check_current_team(self.team, new_value)
        if not current_team:
            return


def set_run_dungeons(cords=-1):
    if cords == -1:
        cords = c.DungeonCords()
    volcano = Dungeon("volcano", "team_1", "depth_2", "16", "6")
    water = Dungeon("water", "team_2", "depth_2", "18", "3")
    forest = Dungeon("forest", "team_3", "depth_1", "6", "7")
    new_new_dungeons = [volcano, water, forest]
    for dungeon in new_new_dungeons:
        dungeon.duration = int(dungeon.rooms) * cords.room_duration + 5
        dungeon.current_duration = dungeon.duration
    return new_new_dungeons


def dungeon_tab():
    cords = c.DungeonCords()
    pg.click(cords.tab)
    pg.click(cords.dungeon_tab)
    pg.click(cords.items_back_button)


def check_current_team(identity_image, cord_to_click, cords=-1):
    """ 
    Cycle through options given a button that cycles through them 
    identity_image is the wanted option
    cord_to_click is coordinate of the cycle button
    if cords is not supplied, it will get its own cords
    """
    if cords == -1:
        cords = c.DungeonCords()
    pg.click(cords.tab)
    region = cords.region
    pg.moveTo(region[2], region[3])
    # time.sleep(.1)
    pos = imgS.imagesearcharea(
        IMAGE_DICTIONARY[identity_image], region[0], region[1], region[2], region[3], 0.95)
    if pos[0] != -1:
        return True
    else:
        # next button (usecase is when a button cycles through options)
        print("I clicked: ", cord_to_click)
        pg.click(cord_to_click)
        return False


def new_check_current_team(identity_image, cord_to_click, cords=-1):
    """ 
    Cycle through options given a button that cycles through them 
    identity_image is the wanted option
    cord_to_click is coordinate of the cycle button
    if cords is not supplied, it will get its own cords
    """
    if cords == -1:
        cords = c.DungeonCords()
    pg.click(cords.tab)
    region = cords.region
    pg.moveTo(cords.safe_spot)
    # time.sleep(.1)
    pos = imgS.imagesearcharea(
        IMAGE_DICTIONARY[identity_image], region[0], region[1], region[2], region[3], 0.95)
    if pos[0] != -1:
        return True
    count = 1
    while count < 20:
        pg.moveTo(cords.safe_spot)
        pos = imgS.imagesearcharea(
            IMAGE_DICTIONARY[identity_image], region[0], region[1], region[2], region[3], 0.95)
        if pos[0] != -1:
            return True
        count += 1
        # next button
        print("I clicked: ", cord_to_click)
        pg.click(cord_to_click)
        time.sleep(0.05)
    # after 20 attempts, it failed, return False
    return False


def set_dungeon_info(dungeon):
    pg.click(dungeon[2])
    pg.click(dungeon[3])
    pg.click(dungeon[4])


def collect_dungeon_rewards(coordinates):
    """clicks the coordinates to finish a dungeon """
    cords = c.DungeonCords()
    dungeon_tab()
    pg.click(coordinates[0] + cords.finish_offset, coordinates[1])
    time.sleep(0.1)
    pg.click(cords.close_result)


def collect_all_dungeon_rewards():
    """ set in stone dungeon rewards (water, volcano and mountain) """
    cords = c.DungeonCords()
    dungeon_tab()
    collect_dungeon_rewards(cords.water)
    time.sleep(0.1)
    collect_dungeon_rewards(cords.volcano)
    time.sleep(0.1)
    collect_dungeon_rewards(cords.mountain)
    time.sleep(0.1)
