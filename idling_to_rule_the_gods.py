""" docstring """
import time
from colorama import Fore, init
import pyautogui as pg
import coordinates as c
from divinity_generator import Divinity
import dungeons as d
import helpers
from helpers import TimerClass
from planet import Planet
from image_index import IMAGE_DICTIONARY
from gods import Gods
from tabs import Tabs
from pets import Pets
from monuments import Monuments
from creations import Creations

ACTIVE_DUNGEONS = {}
ACTIVE_TIMERS = []
TIMER_TRACKER = {}

CAMPAIGN_INDEX = {
    # ordered top to bottom
    "growth": 0,
    "divinity": 1,
    "food": 2,
    "item": 3,
    "level": 4,
    "multiplier": 5,
    "godpower": 6,
}

G_DUNGEON_INDEX = {
    # ordered top to bottom

    "newbie": 0,
    "scrap": 1,
    "water_temple": 2,
    "fire_temple": 3,
    "mountain": 4,
    "forest_temple": 5
}


class ActionClass(Tabs):
    COORDINATES = c.Coordinates()
    print(f"{Fore.CYAN}ActionClass called c.Coordinates() at {helpers.time_format()}")
    CORD_LAST_UPDATE = time.time()
    START_BUTTON = None
    REWARD_BUTTON = None
    FALL_BACK_POS = []
    ALL_ACTION_CLASSES = {}
    CAMPAIGNS = {}
    DUNGEONS = {}
    TABS = []

    def __init__(self, name):
        super().__init__(name)
        self.timer = TimerClass(self.name, -1)
        self.is_active = False
        self.action_region = -1
        self.action_region_relative = -1
        self.current_duration = None
        self.camp_index = -1
        self.active_name = self.name + "_active"
        ActionClass.ALL_ACTION_CLASSES[self.name] = self

    def check_if_active(self):
        coordinates = self.get_cords()
        self.go_to_tab()
        try:
            pos = helpers.return_position_of_image_on_screen(IMAGE_DICTIONARY[self.active_name])
        except KeyError as exception:
            pos = (self.FALL_BACK_POS[0], self.FALL_BACK_POS[1] + 45 * self.camp_index)
            print(exception)
        if pos[0] == -1:
            pos = (self.FALL_BACK_POS[0], self.FALL_BACK_POS[1] + 45 * self.camp_index)
        x = round(pos[0])
        y = round(pos[1]) - 25
        self.action_region_relative = (x - coordinates.X_PAD, y - coordinates.Y_PAD,
                                       x + 350 - coordinates.X_PAD, y + 50 - coordinates.Y_PAD)
        pg.moveTo(pos[0] + 50, pos[1])
        tooltip_image = helpers.get_image_from_zone(coordinates.tooltip_region)
        time.sleep(0.1)
        time_left = get_hours_left(tooltip_image)
        if time_left == -1:
            print(f"{Fore.RED}{self.name} is not active")
            self.is_active = False
            return False
        elif time_left == 0:
            print(f"{Fore.GREEN}{self.name} is finished... Collecting Reward (self.collect_reward())")
            self.collect_reward()
            self.is_active = False
            return False
        self.timer.set_end_time(time_left + 5)
        self.timer.reset_timer()
        self.is_active = True
        print(f"{Fore.GREEN}{self.name} is active with {self.timer.time_remaining():.0f} remaining")
        return True

    def start_action(self):
        """ This part can be run for both campaign and dungeons. """
        if self.is_active and self.timer.time_remaining() > 0:
            print(f"{self.name} is active with {self.timer.time_remaining():.0f} remaining")
            return
        coordinates = self.get_cords()
        self.go_to_tab()
        pos = helpers.return_position_of_image_on_screen(IMAGE_DICTIONARY[self.name], coordinates)  # coordinates
        x = round(pos[0])
        y = round(pos[1]) - 25
        self.action_region = (x, y, x + 350, y + 50)
        self.action_region_relative = (x - coordinates.X_PAD, y - coordinates.Y_PAD,
                                       x + 350 - coordinates.X_PAD, y + 50 - coordinates.Y_PAD)
        pg.moveTo(coordinates.safe_spot)
        helpers.click_image_in_zone(IMAGE_DICTIONARY[self.START_BUTTON], zone=self.action_region)
        pg.moveTo(coordinates.safe_spot)
        duration = self.current_duration + 20
        if self.timer == -1:
            self.timer = TimerClass(self.name, duration)
        else:
            self.timer.set_end_time(duration)
            self.timer.reset_timer()
        TIMER_TRACKER[self.timer.name] = self.timer
        print(f"{self.name} has {self.timer.time_remaining()} seconds remaining")

    def collect_reward(self):
        coordinates = self.get_cords()
        self.go_to_tab()
        pos = self.action_region_relative
        if pos[0] == -1:
            pos = (self.FALL_BACK_POS[0], self.FALL_BACK_POS[1] + 45 * self.camp_index)
        x = round(pos[0])
        y = round(pos[1]) - 15
        zone = (x + coordinates.X_PAD, y + coordinates.Y_PAD,
                x + 400 + coordinates.X_PAD, y + 65 + coordinates.Y_PAD)
        print(self.REWARD_BUTTON)
        helpers.click_image_in_zone(IMAGE_DICTIONARY[self.REWARD_BUTTON], zone=zone)
        pg.moveTo(coordinates.safe_spot)
        time.sleep(2)
        helpers.click_image_on_screen(IMAGE_DICTIONARY["close_button"])
        time.sleep(0.1)
        self.is_active = False


class Campaign(ActionClass):
    COORDINATES = c.CampaignCords()
    print(f"{Fore.CYAN}Campaign called c.CampaignCords() at {helpers.time_format()}")
    START_BUTTON = "select_button"
    CLOSE_BUTTON = "auto_button"
    REWARD_BUTTON = "result_button"
    pg.click(COORDINATES.tab)
    FALL_BACK_POS = helpers.return_position_of_image_on_screen(IMAGE_DICTIONARY["growth_active"], COORDINATES)
    TABS = [COORDINATES.tab]
    CAMPAIGNS = {}

    def __init__(self, name, rooms):
        super().__init__(name)
        self.duration = int(rooms) * 60 * 60 + 20
        self.current_duration = self.duration
        try:
            self.camp_index = CAMPAIGN_INDEX[self.name]
        except KeyError:
            print(f"{self.name} not found in campaign_index")
        ActionClass.CAMPAIGNS[self.name] = self
        ActionClass.ALL_ACTION_CLASSES[self.name] = self

    def start_action(self):
        """ This can set and collect both campaign and dungeons. """
        coordinates = self.get_cords()
        self.go_to_tab()
        super().start_action()
        pg.click(coordinates.hour_12)
        pg.moveTo(coordinates.safe_spot)
        helpers.click_image_on_screen(IMAGE_DICTIONARY[self.CLOSE_BUTTON])
        self.is_active = True


class Dungeon(ActionClass):
    COORDINATES = c.DungeonCords()
    print(f"{Fore.CYAN}Dungeon called c.DungeonCords() at {helpers.time_format()}")
    START_BUTTON = "info_button"
    CLOSE_BUTTON = "start_button"
    REWARD_BUTTON = "dungeon_finished_button"
    pg.click(COORDINATES.tab)
    FALL_BACK_POS = helpers.return_position_of_image_on_screen(IMAGE_DICTIONARY["newbie_active"], COORDINATES)
    TABS = [COORDINATES.tab, COORDINATES.dungeon_tab]
    DUNGEONS = {}

    def __init__(self, name, team, depth, rooms, difficulty):
        super().__init__(name)
        self.team = team
        self.depth = depth
        self.rooms = rooms
        self.difficulty = difficulty
        self.duration = int(self.rooms) * self.get_cords().room_duration + 5
        self.current_duration = self.duration
        self.timer = TimerClass(self.name, -1)
        self.active_name = self.name + "_active"
        try:
            self.camp_index = G_DUNGEON_INDEX[self.name]
        except KeyError as exception:
            print(exception, "Not in list")
        super().DUNGEONS[self.name] = self
        Dungeon.DUNGEONS[self.name] = self

    def start_action(self):
        """ This is part 2 of start_action. ActionClass holds part 1"""
        self.go_to_tab()
        super().start_action()
        self.check_if_correct_team()
        dungeon_info(self)
        helpers.click_image_on_screen(IMAGE_DICTIONARY[self.CLOSE_BUTTON])
        self.is_active = True

    def check_if_correct_team(self):
        coordinates = self.get_cords()
        next_button_cord = helpers.add_screen_padding(
            helpers.find_image_in_game_window(IMAGE_DICTIONARY["next_button"], coordinates=coordinates),
            coordinates)
        button_center = (next_button_cord[0] + 26, next_button_cord[1] + 18)
        current_team = d.new_check_current_team(self.team, button_center)
        if not current_team:
            return


def create_default_actions(dungeon=False, campaign=False):
    """ Returns an array of "Actions" with the corresponding responsibility (dungeon or campaigns) """
    actions = []
    if dungeon:
        fire_temple = Dungeon("fire_temple", "team_1", "depth_2", "16", "4")
        water_temple = Dungeon("water_temple", "team_2", "depth_2", "18", "3")
        forest_temple = Dungeon("forest_temple", "team_3", "depth_1", "6", "7")
        actions.append(fire_temple)
        actions.append(water_temple)
        actions.append(forest_temple)
        fire_temple.go_to_tab()
    if campaign:
        growth = Campaign("growth", "12")
        item = Campaign("item", "12")
        multiplier = Campaign("multiplier", "12")
        food = Campaign("food", "12")
        actions.append(growth)
        actions.append(item)
        actions.append(multiplier)
        actions.append(food)
        growth.go_to_tab()
    return actions


def nrdc_loop(loop_count):
    """ loop_count = how many total dungeons it should loop through """
    # Get coordinates and set timers to track it
    create_default_actions(dungeon=True)
    dungeons = Dungeon.DUNGEONS
    for dungeon_name in dungeons:
        dungeon = dungeons[dungeon_name]
        dungeon.check_if_active()
        if not dungeon.is_active:
            dungeon.start_action()
    pg.moveTo(Dungeon.COORDINATES.safe_spot)
    next_dungeon = helpers.locate_min_dungeon(dungeons)
    sleep_time = next_dungeon.timer.time_remaining()  # == dungeon.current_duration <- current time left
    if sleep_time < 0:
        sleep_time = 0
    # Sleep for shortest dungeon timer
    helpers.print_action_next_action(sleep_time)
    time.sleep(sleep_time)
    for _ in range(loop_count):
        # get current window location by getting a new DungeonCords object
        for dungeon_name in dungeons:
            dungeon = dungeons[dungeon_name]
            print(f"{Fore.MAGENTA}{dungeon.name} has {dungeon.timer.time_remaining():.0f}s remaining")
        pg.moveTo(Dungeon.COORDINATES.safe_spot)
        next_dungeon.collect_reward()
        time.sleep(4)  # Dungeos sometime have a 3-4 sec delay to open the reward screen
        pg.moveTo(Dungeon.COORDINATES.safe_spot)
        next_dungeon.start_action()
        # Get new sleep time
        next_dungeon = helpers.locate_min_dungeon(dungeons)
        sleep_time = next_dungeon.timer.time_remaining()
        if sleep_time < 0:
            sleep_time = 0
        helpers.print_action_next_action(sleep_time)
        time.sleep(sleep_time)


def dungeon_info(dungeon):
    coordinates = Dungeon.COORDINATES
    depth_text = helpers.return_position_of_image_on_screen(IMAGE_DICTIONARY["depth_text"], coordinates)  # coordinates
    current_depth = d.new_check_current_team(dungeon.depth, depth_text)
    if not current_depth:
        return
    set_input_box_value("duration_text", "input_box", dungeon.rooms)
    pg.moveTo(coordinates.safe_spot)
    set_input_box_value("difficulty_text", "input_box", dungeon.difficulty)
    pg.moveTo(coordinates.safe_spot)


def set_input_box_value(identity_image, input_box, input_value):
    coordinates = Dungeon.COORDINATES
    pos = helpers.return_position_of_image_on_screen(IMAGE_DICTIONARY[identity_image], coordinates)  # coordinates
    x = round(pos[0])
    y = round(pos[1]) - 25
    helpers.click_image_in_zone(IMAGE_DICTIONARY[input_box], x, y, x + 300, y + 50)
    helpers.click_image_in_zone(IMAGE_DICTIONARY[input_box], x, y, x + 300, y + 50)
    pg.write(input_value)


def infinite_loop():
    actions = create_default_actions(c.DungeonCords(), c.CampaignCords())
    for action in actions:
        action.check_if_active()
        if action.is_active:
            action.start_action()
    looping = True
    while looping:
        for action in actions:
            print("{} has {} seconds remaining".format(action.name, action.timer.time_remaining()))
        for action in TIMER_TRACKER:
            print("{} has {} remaining".format(action, TIMER_TRACKER[action].time_remaining()))
        time.sleep(5)


def add_resources_to_dict(resources, total_resources):
    for resource in resources:
        split_resource = resource.split("x")
        count = split_resource[0].strip()
        resource_name = split_resource[1:][0].strip()
        if resource_name in total_resources:
            total_resources[resource_name] += int(count)
        else:
            total_resources[resource_name] = int(count)
        print(total_resources[resource_name])


def get_hours_left(image):
    text = helpers.get_text_from_image(image)
    try:
        index_of_in = text.index("finished in ")
        index_of_in += len("finished in ")
    except ValueError:
        print(text)
        print("No active dungeon?")
        return -1
    try:
        my_words = text[index_of_in:].split()
        my_new_words = my_words[0].split(":")
        length_of_my_words = len(my_new_words)
        time_left = 0
        for i in range(length_of_my_words):
            time_left += 60**(length_of_my_words-1-i) * int(my_new_words[i])
    except ValueError as value_error:
        time_left = -1
        print(value_error)
        print(text)
    return time_left


init(autoreset=True)


def quick_rebirth():
    """
    pets.distribute()
    gods.finger_flick()
    monuments.div_gen_unlock()
    creation.div_gen_unlock()
    div_gen.construct()
    div_gen.construct_upgrades()
    for _ in range(x):
        #
        pets.distribute()
        div_gen.add()
        div_gen.construct_upgrades()
    div_gen.remove_all_clones()
    div_gen.cap_max()
    planet.power_surge()
    monuments.temple_of_god()
    for _ in range(x):
        # Idle loop
        pets.distribute()
        div_gen.add()
    if creation.finished_cycle:
        creation.weather()
    end_of_run()
        monuments.black_hole()
        monuments.black_hole_upgrade()
        god.finger_flick()
        god.fight()
        bp.food()
        bp.light_clones()
        bp.pet_stones()
    quick_rebirth()
    """


def main():
    main_start_time = time.time()
    started_at = helpers.time_format()
    main_timer = TimerClass("Rebirth")
    print(f'{Fore.GREEN}Script starting at:{started_at}\n')
    creation = Creations("creation")
    creation.create_clones_on()
    creation.create_progress(creation.WEATHER)
    # mon = monuments.Monuments("monuments")
    # mon.build(mon.EVERLASTING_LIGHTHOUSE)
    # mon.upgrade(mon.EVERLASTING_LIGHTHOUSE)
    # div_gen = div.Divinity(c.DivinityCords())
    # if not div_gen.is_constructed:
    #    print("divgen is not constructed")
    #    div_gen.construct()
    # div_gen.construct_upgrades()
    # planet = p.Planet()
    # p.Planet.POWER_SURGING = True
    # planet.fight_UB()
    # planet.create_crystals()
    # planet.upgrade_crystals()
    # planet.equip_crystals()
    # if div_gen.is_constructed:
    # div_gen.construct_upgrades()
    # div_gen.add_to_div()
    # div_gen.construct_upgrades()
    # div_gen.remove_all_clones()
    # div_gen.cap_max()
    # dungeon_test = Dungeon("water_temple", "team_2", "depth_2", "18", "3")
    # dungeon_test.check_if_active()
    # dungeon_test.collect_reward()
    # dungeon_test.start_action()
    # create_default_actions(c.DungeonCords(), c.CampaignCords())
    # for action in ActionClass.ALL_ACTION_CLASSES:
    #     action = ActionClass.ALL_ACTION_CLASSES[action]
    #     action.check_if_active()
    #     if not action.is_active:
    #         action.start_action()
    # pet = pets.Pets(c.PetCords())
    # pet = pets.Pets(c.PetCords())
    # pet.distribute()
    # god = gods.Gods(c.GodCords())
    # god.finger_flick()
    # god.fight()

    # nrdc_loop(50)
    # print(dungeon_test.get_cords())
    # print(Dungeon.COORDINATES)
    # infinite_loop()
    main_end_time = time.time()
    print("Script ended at: " + helpers.time_format())
    print("Time elapsed: " + str(main_end_time - main_start_time))


if __name__ == '__main__':
    main()

# Unused stuff #

""" Todo:

Make a dungeon/campaign class that has an "Interact" function
that performs starting / collection of CAMPAIGNS.
This way we can add them all to a common timer tracker and launch "interact"
with the dungeon/campaign that is up for completion/starting

class:
    coordinates for its tab?
    camp/dungen name
    timer
    current_remaining
    buttons to click (see "set_CAMPAIGNS")


def creating_next_at_2():
    ""sets next at to option 2""
    coordinates = c.creatingCords()
    pg.click(coordinates.tab)
    pg.click(coordinates.light)
    pg.click(coordinates.nextAt_2)


def pet_campaign_auto(hours_cord):
    pg.click(hours_cord)
    helpers.click_image_on_screen(IMAGE_DICTIONARY["auto_button"])
    # pg.click(coordinates.auto_select)


def feed_pets():
    coordinates = c.petCords()
    pg.click(coordinates.tab)
    pg.click(coordinates.feed)


def collect_campaign_rewards(coordinates):
    ""clicks the coordinates to finish a campaign ""
    coordinates = c.CampaignCords()
    pg.click(coordinates.tab)
    pg.click(coordinates[0], coordinates[1] + coordinates.padding)  # collect reward
    time.sleep(0.1)
    pg.click(coordinates.close_result)


def spend_bp_on_food():
    coordinates = c.petCords()
    pg.click(coordinates.tab)
    pg.click(coordinates.buyFoodButton)
    pg.click(coordinates.bpFoodOption)
    pg.click(coordinates.buyFoodMax)
    pg.click(coordinates.confirmPurchase)


def end_of_run_clean_up_food(should_restart):
    collect_pet_rewards(c.CampaignCords().tab, "result_button")
    time.sleep(0.1)
    collect_pet_rewards(c.DungeonCords().tab, "dungeon_finish_button")
    feed_pets()
    time.sleep(0.1)
    final_battle()
    time.sleep(0.5)
    spend_bp_on_food()
    # Implement crystal upgrade & equip.
    # in our current rebith time -> 2 crystals
    time.sleep(2)
    if should_restart:
        loops.food_rebirth_loop()


def end_of_run_clean_up_light_clones(should_restart):
    collect_pet_rewards(c.CampaignCords().tab, "result_button")
    time.sleep(0.1)
    collect_pet_rewards(c.DungeonCords().tab, "dungeon_finish_button")
    feed_pets()
    time.sleep(0.1)
    final_battle()
    time.sleep(0.5)
    spend_bp_on_light_clones()
    # Implement crystal upgrade & equip.
    # in our current rebith time -> 2 crystals
    time.sleep(2)
    if should_restart:
        loops.light_clones_rebirth_loop()


def build_monuments():
    # ToG
    coordinates = c.monumentCords()
    clone_cords = c.cloneAmounts()
    pg.click(coordinates.tab)
    pg.mouseDown(coordinates.bottomOfScroll)
    time.sleep(1)
    pg.mouseUp()
    pg.click(clone_cords.twoHundredK)
    pg.click(coordinates.toGUpgradePlus)
    time.sleep(0.1)
    pg.click(clone_cords.maxAmount)
    pg.click(coordinates.toGPlus)


def all_clones_on_monument_upgrade():
    coordinates = c.monumentCords()
    pg.click(coordinates.tab)
    pg.mouseDown(coordinates.bottomOfScroll)
    time.sleep(1)
    pg.mouseUp()
    time.sleep(0.1)
    pg.click(c.cloneAmounts().maxAmount)
    pg.click(coordinates.toGMinus)
    time.sleep(0.1)
    pg.click(coordinates.toGUpgradePlus)


def final_battle():
    coordinates = c.godCords()
    pg.click(coordinates.tab)
    pg.click(coordinates.unleash)
    pg.click(coordinates.fingerFlick)
    for _ in range(5):
        time.sleep(2)
        pg.click(coordinates.fight)


def weather_ceation_lock():
    # didnt work last time
    coordinates = c.creatingCords()
    pg.click(coordinates.tab)
    pg.mouseDown(coordinates.weather_scroll_position)
    time.sleep(0.5)
    pg.mouseUp()
    time.sleep(0.1)
    pg.click(coordinates.weather)
    time.sleep(0.1)
    pg.click(coordinates.nextAtOff)


def fresh_dungeons(dungeons, coordinates=-1):
    if coordinates == -1:
        coordinates = c.DungeonCords()
    pg.click(coordinates.tab)
    coordinates = c.Coordinates()
    next_button_cord = helpers.add_screen_padding(helpers.find_image_in_game_window(IMAGE_DICTIONARY["next_button"], coordinates=coordinates), coordinates)
    new_value = (next_button_cord[0] + 26, next_button_cord[1] + 18)
    current_team_one = d.new_check_current_team("petTeam_1", new_value, coordinates)
    if not current_team_one:
        return
    for dungeon in dungeons:
        print("Starting: ", dungeon.name)
        dungeon_timer = TimerClass(dungeon.name, dungeon.current_duration)
        TIMER_TRACKER[dungeon_timer.name] = dungeon_timer
        set_CAMPAIGNS(coordinates.tab, dungeon.name, "info_button", "start_button", dungeon, coordinates)


def check_light_clone_cost():
    # Check the cost of clones
    clone_cost_4 = helpers.add_screen_padding(helpers.find_image_in_game_window(IMAGE_DICTIONARY["4_light_clones"], 0.9))
    if clone_cost_4[0] != -1:
        print("This will be the case of clones costing 4 BP per. RESET COST")
        helpers.click_image_on_screen(IMAGE_DICTIONARY["reset_button"])
        time.sleep(0.1)
        helpers.click_image_on_screen(IMAGE_DICTIONARY["yes_button"])
    else:
        print("This is the case where clone cost is less than 4")
        return True
    clone_cost_rest = helpers.find_image_in_game_window(IMAGE_DICTIONARY["0_light"])
    if clone_cost_rest[0] != -1:
        print("RESET SUCCESSFULL")
        return True
    else:
        print("reset unsuccessfull")
        return False
        # check resets available


def spend_bp_on_light_clones():
    coordinates = c.SpaceDimCords()
    pg.click(coordinates.tab)
    pg.moveTo(coordinates.tab[0], coordinates.tab[1] + 200)
    # make sure we're on the right page
    buy_screen_pos = helpers.find_image_in_game_window(IMAGE_DICTIONARY["buy_light_clones"], 0.9, 1)
    if buy_screen_pos[0] == -1:
        # if buy_screen_pos == -1, we want to get there
        pg.click(coordinates.buy_more_button)
    buy_button_pos = helpers.find_image_in_game_window(IMAGE_DICTIONARY["buy_button"], 0.9)
    while buy_button_pos[0] != -1:
        print("We have a buy button")
        if check_light_clone_cost():
            # buy light clones
            pg.click(coordinates.buy_max)
            pg.click(coordinates.buy_middle)
            pg.click(coordinates.buy_lowest)
        else:
            break
        buy_button_pos = helpers.find_image_in_game_window(IMAGE_DICTIONARY["buy_button"], 0.9)
    # need "one light clone costs 4 Baal Power" picture to search for reset.


def set_CAMPAIGNS(tab_cord, identity_image, start_button, close_button, dungeon=-1, coordinates=-1):
    "" This can set and collect both campaign and dungeons.
tab -> campaign or dungeon coordinates
identity_image -> the campaign/dungeon to start
start_button -> "Select" for campaign, "info" for dungeon
close_button -> "Auto" for campaign, "start" for dungeon
dungeon -> if supplied, set predefined dungeon info(difficulty, duration and depth)
""
    if coordinates == -1:
        coordinates = c.Coordinates()
    pg.click(tab_cord)
    pos = helpers.return_position_of_image_on_screen(IMAGE_DICTIONARY[identity_image], coordinates)  # coordinates
    x = round(pos[0])
    y = round(pos[1]) - 25
    helpers.click_image_in_zone(IMAGE_DICTIONARY[start_button], x, y, x + 400, y + 50)
    pg.moveTo(x, y + 50)
    if dungeon != -1:
        dungeon_info(dungeon, coordinates)
    helpers.click_image_on_screen(IMAGE_DICTIONARY[close_button])


def collect_pet_rewards(tab_cord, button_name):
    "" This will collect all rewards on the given tab
button_name = > "result" for CAMPAIGNS, "finish" for dungeons
    ""
    pg.click(tab_cord)
    coordinates = c.Coordinates()
    pos = helpers.return_position_of_image_on_screen(IMAGE_DICTIONARY["finished_campaign"], coordinates)
    active_campaign = False
    if pos[0] != -1:
        active_campaign = True
    while active_campaign:
        pg.moveTo(tab_cord[0] + 350, tab_cord[1])
        pos = helpers.return_position_of_image_on_screen(IMAGE_DICTIONARY["finished_campaign"], coordinates)
        if pos[0] != -1:
            active_campaign = True
        else:
            active_campaign = False
            break
        x = round(pos[0])
        y = round(pos[1]) - 25
        helpers.click_image_in_zone(IMAGE_DICTIONARY[button_name], x, y, x + 400, y + 50)
        close_pos = helpers.return_position_of_image_on_screen(IMAGE_DICTIONARY["close_button"], coordinates)
        attempts = 0
        while close_pos[0] == -1:
            close_pos = helpers.return_position_of_image_on_screen(IMAGE_DICTIONARY["close_button"], coordinates)
            time.sleep(0.1)
            attempts += 1
            if attempts >= 10:
                break
        pg.click(close_pos)
"""
