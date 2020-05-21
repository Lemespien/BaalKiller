""" Helper methods """
import time
import PIL
from PIL import Image, ImageFilter
import pyautogui as pg
import pytesseract as pyte
import imagesearch as imgS
import coordinates as c
import chilimangoes as chili
from colorama import Fore, Back, Style
pyte.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def find_image_on_screen(image, x_1, y_1, x_2, y_2):
    found = False
    count = 0
    retries = 3
    while not found:
        pos = imgS.imagesearcharea(image, x_1, y_1, x_2, y_2, 0.8)
        if pos[0] != -1:
            found = True
            return pos
        else:
            if count >= retries:
                print(f'{Fore.RED}find_image_on_screen gave up')
                return (-1, -1)
            print(f'{Fore.RED}find_image_on_screen did not find image. Retries: {retries-count}')
            count += 1
            time.sleep(.5)


def add_screen_padding(pos, cords=-1):
    if cords == -1:
        cords = c.Coordinates()
    if pos[0] == -1 and pos[1] == -1:
        return (-1, -1)
    return (pos[0] + cords.x_pad, pos[1] + cords.y_pad)


def find_image_in_game_window(image, precision=0.8, retries=3, cords=-1):
    """returns position of image in game_window coordinates"""
    if cords == -1:
        cords = c.Coordinates()
    x_1, y_1, x_2, y_2 = cords.game_region
    found = False
    count = 0
    pg.moveTo(cords.safe_spot)
    while not found:
        pos = imgS.imagesearcharea(image, x_1, y_1, x_2, y_2, precision)
        if pos[0] != -1:
            found = True
            return pos
        count += 1
        if count >= retries:
            return (-1, -1)
        pg.moveTo(cords.safe_spot)
        print("Image not found")
        print("Tries left: ", retries - count)
        time.sleep(0.5)


def return_position_of_image_on_screen(image, coordinates=-1):
    """ returns position of image center in monitor space """
    if coordinates == -1:
        coordinates = c.Coordinates()
    pil_image = PIL.Image.open(image)
    width, height = pil_image.size
    image_pos = add_screen_padding(find_image_in_game_window(image, 0.8, cords=coordinates), cords=coordinates)
    if image_pos[0] != -1:
        return image_pos[0] + width/2, image_pos[1] + height/2
    else:
        return -1, -1


def click_image_on_screen(image, coordinates=-1):
    if coordinates == -1:
        coordinates = c.Coordinates()
    pil_image = PIL.Image.open(image)
    width, height = pil_image.size
    image_pos = add_screen_padding(find_image_in_game_window(image, 0.9, cords=coordinates), cords=coordinates)
    if image_pos[0] != -1:
        # move to and click resetbutton
        pg.click(image_pos[0] + width/2, image_pos[1] + height/2)


def click_image_in_zone(image, x_1=None, y_1=None, x_2=None, y_2=None, zone=None):
    if zone is not None:
        x_1, y_1, x_2, y_2 = zone
    pil_image = PIL.Image.open(image)
    width, height = pil_image.size
    image_pos = find_image_on_screen(image, x_1, y_1, x_2, y_2)
    if image_pos[0] != -1:
        pg.click(x_1 + image_pos[0] + width/2, y_1 + image_pos[1] + height/2)


def print_action_next_action(next_action_time):
    action_started = time_format()
    print(f'\n{Fore.GREEN}Action started at: {action_started}')
    next_action = time_format(next_action_time)
    print(f'{Fore.GREEN}Next action at: {next_action}\n')


def time_format(future_time=0):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + future_time))


def locate_min(a):
    smallest = min(a)
    return [element for index, element in enumerate(a) if smallest[0] == element[0]]


def locate_min_dungeon(dungeons):
    # shortest = a[0]
    shortest = None
    for dungeon_name in dungeons:
        dungeon = dungeons[dungeon_name]
        if shortest is None:
            shortest = dungeon
        if dungeon.timer.time_remaining() < shortest.timer.time_remaining():
            shortest = dungeon
    # for action in a:
    #     if action.timer.time_remaining() < shortest.timer.time_remaining():
    #         shortest = action
    return shortest


def enhance_image(image):
    if not isinstance(image, PIL.Image.Image):
        image = Image.open(image)
    image = image.resize((image.width*4, image.height*4))
    new_image = image.filter(ImageFilter.SMOOTH)
    new_image = new_image.filter(ImageFilter.SMOOTH)
    return new_image


def get_text_from_image(image):
    txt = pyte.image_to_string(enhance_image(image))
    return txt


def get_resources_from_image(image):
    txt = get_text_from_image(image)
    index_of_resources = txt.index("found:")
    resources = txt[index_of_resources + len("found:") + 2:]
    resource_array = []
    for resource in resources.split('\n'):
        if len(resource) > 0:
            resource_array.append(resource)
    return resource_array


def get_image_from_zone(zone):
    return chili.grab_screen(zone)
# def timer_function(index=-1, name="default"):
#     """
#     Set a new timer, returns index of timer in ACTIVE_TIMERS
#     Pass in index of timer to get finished time
#     """
#     if index == -1:
#         ACTIVE_TIMERS.append([name, time.time()])
#         index = len(ACTIVE_TIMERS) - 1
#         return index
#     end_time = time.time()
#     print(ACTIVE_TIMERS[index][0] + " time elapsed: " + str(end_time - ACTIVE_TIMERS[index][1]))
