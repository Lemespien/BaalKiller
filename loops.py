import coordinates as c
import pyautogui as pg
import time
import divinity_generator as div
import helpers


def light_clones_rebirth_loop():
    """ aiming for 2:10 hour:min run """
    """ Rework
    standard_rebirth_loop()
    idle_start_loop(True)  # ~730 sec
    time.sleep(0.5)
    pet_campaign_loop()
    time.sleep(0.5)
    dungeons = d.set_run_dungeons(c.DungeonCords())
    fresh_dungeons(dungeons)
    # add to divgen
    div.add_clones_to_div_construct()
    for _ in range(2):
        div.add_to_div_gen()
        div.add_clones_to_div_construct()
        time.sleep(51)
    for _ in range(6):
        div.add_to_div_gen()
        div.add_clones_to_div_construct()
        time.sleep(51)
    # 1020 sec ish
    for _ in range(2):
        div.add_to_div_gen()
        time.sleep(600)
    time.sleep(360)  # current run time ~44.5min total
    weather_ceation_lock()  # this should happen after universe has been created ~43min (2580sec)
    # lock creation to weather
    time.sleep(0.5)
    div.remove_clones_from_div_construct()
    div.add_workers_to_div_gen()
    time.sleep(0.1)
    p.add_clones_to_power_surge()
    time.sleep(0.1)
    # build black hole with upgrades
    build_monuments()  # builds ToGs
    time.sleep(300)
    p.fight_ub()
    time.sleep(2)
    # create crystals
    p.add_clones_to_power_surge()
    time.sleep(2800)  # with previous steps ~ 5783sec
    p.fight_ub()  # 96min (5760sec)
    time.sleep(0.5)
    # create crystals (ultimate, mystic and battle)
    p.remove_clones_from_power_surge()
    time.sleep(0.5)
    build_monuments()  # builds ToGs
    time.sleep(800)
    div.remove_workers_from_div_gen()
    all_clones_on_monument_upgrade()
    time.sleep(340)
    # ~115min 6923 sec
    time.sleep(1130)  # time remaining for dungeons and campaign in 2hour 10min run
    end_of_run_clean_up_light_clones(should_restart=True)
    """


def food_rebirth_loop():
    """ Rework
    standard_rebirth_loop()
    idle_start_loop(True)  # ~600 sec
    time.sleep(0.5)
    pet_campaign_loop()
    time.sleep(0.5)

    dungeons = d.set_run_dungeons(c.DungeonCords())
    fresh_dungeons(dungeons)
    # add to divgen
    weather_ceation_lock()
    div.add_clones_to_div_construct()
    for _ in range(2):
        div.add_to_div_gen()
        div.add_clones_to_div_construct()
        time.sleep(240)
    div.add_clones_to_div_construct()
    for _ in range(6):
        div.add_to_div_gen()
        time.sleep(240)
    div.add_clones_to_div_construct()
    time.sleep(0.5)
    div.remove_clones_from_div_construct()
    div.add_workers_to_div_gen()
    time.sleep(0.1)
    p.add_clones_to_power_surge()
    time.sleep(0.1)
    build_monuments()
    time.sleep(0.1)
    p.fight_ub()
    time.sleep(5)
    p.add_clones_to_power_surge()
    time.sleep(1415)
    p.fight_ub()
    time.sleep(0.5)
    p.remove_clones_from_power_surge()
    time.sleep(0.5)
    build_monuments()
    time.sleep(800)
    div.remove_workers_from_div_gen()
    time.sleep(340)
    all_clones_on_monument_upgrade()
    time.sleep(120)  # time remaining for dungeons + buffer
    end_of_run_clean_up_food(should_restart=True)
    """


def rebirth_loop():
    cords = c.rebirthCords()
    pg.click(cords.tab)
    pg.click(cords.button)
    pg.click(cords.confirm)
    pg.click(cords.confirm_2)
    pg.click(cords.confirm_3)
    pg.click(cords.godPowerGain)


def pet_loop():
    cords = c.petCords()
    pg.click(cords.tab)
    pg.click(cords.distribute)


def god_flick_loop():
    cords = c.godCords()
    pg.click(cords.tab)
    pg.click(cords.fingerFlick)


def monument_to_div_gen_loop():
    cords = c.monumentCords()
    pg.click(cords.tab)
    pg.click(cords.mightyStatuePlus)


def creating_loop():
    cords = c.creatingCords()
    # creating_next_at_2()
    pg.click(cords.createMaxClones)
    time.sleep(2)
    pg.click(cords.createMaxClones)


def idle_start_loop(divgen=True):
    """ ~625sec"""
    start_time = time.time()
    print("idle_start_loop started: " + helpers.time_format())
    for _ in range(20):
        pet_loop()
        if divgen:
            div.add_to_div_gen()
            div.add_clones_to_div_construct()
        time.sleep(30)
    time_elapsed = time.time() - start_time
    print("idle_start_loop finished: " + helpers.time_format())
    print("Time elapsed: ", time_elapsed)


def pet_campaign_loop():
    """ Rework into using NRDC style """
    # Extremely finicky atm. Only works for this specific
    # order without modification: growth, item, multi, food
    """
    cords = c.CampaignCords()
    pg.click(cords.tab)
    padding = cords.padding
    active_camps = 0
    # Growth is the top camp (active_camps = 0)
    pg.click(cords.growth[0], cords.growth[1] + padding * active_camps)
    active_camps += 1
    pet_campaign_auto(cords.hour_2)
    time.sleep(0.5)
    # Item has growth active above it (active_camps = 1)
    pg.click(cords.item[0], cords.item[1] + padding * active_camps)
    active_camps += 1
    pet_campaign_auto(cords.hour_2)
    time.sleep(0.5)
    # Multiplier has growth & item camp active above it (active_camps = 2)
    pg.click(cords.multiplier[0], cords.multiplier[1] + padding * active_camps)
    active_camps += 1
    pet_campaign_auto(cords.hour_2)
    time.sleep(0.5)
    # Food only has 1 active camp above it
    pg.click(cords.food[0], cords.food[1] + padding)
    active_camps += 1
    pet_campaign_auto(cords.hour_2)
    """


def fresh_birth_loop():
    start_time = time.time()
    print("Fresh birth loop started: ", helpers.time_format())
    # basic Rebirth loop
    time.sleep(2)
    pet_loop()
    time.sleep(1)
    god_flick_loop()
    monument_to_div_gen_loop()
    creating_loop()
    time.sleep(2)
    div.build_div_generator()
    time.sleep(1)
    div.div_gen_loop()
    time_elapsed = time.time() - start_time
    print("Fresh birth loop finished: ", helpers.time_format())
    print("Time elapsed: ", time_elapsed)


def standard_rebirth_loop():
    start_time = time.time()
    print("Standard Rebirth Loop started: ", helpers.time_format())
    # basic Rebirth loop
    rebirth_loop()
    time.sleep(2)
    pet_loop()
    time.sleep(1)
    god_flick_loop()
    monument_to_div_gen_loop()
    creating_loop()
    time.sleep(2)
    div.build_div_generator()
    time.sleep(1)
    div.div_gen_loop()
    time_elapsed = time.time() - start_time
    print("Standard Rebirth Loop finished: ", helpers.time_format())
    print("Time elapsed: ", time_elapsed)


def pet_dungeon_loop_standard(dungeons):
    cords = c.DungeonCords()
    pg.click(cords.tab)
    current_team_one = d.check_current_team("petTeam_1", cords.next_team)
    while not current_team_one:
        current_team_one = d.check_current_team("petTeam_1", cords.next_team)
        time.sleep(1)

    for dungeon in dungeons:
        d.set_dungeon_info(dungeon)
        pg.click(cords.start)
        time.sleep(0.1)
