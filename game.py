"""
Handles tasks that happen each game round
"""

from time import sleep
from difflib import SequenceMatcher
import threading
from PIL import ImageGrab
import win32gui
import keyboard
import ocr
import screen_coords
import champions
import settings
import mk_functions
from vec4 import Vec4
from vec2 import Vec2


class Game:
    """Game class that handles game loop and purchasing champions"""

    def __init__(self):
        self.found_window = False
        self.validate_shop()
        print("\n[!] Searching for game window")
        while not self.found_window:
            print("\tDid not find window, trying again...")
            win32gui.EnumWindows(self.callback, None)
            sleep(1)
        self.game_loop()

    def validate_shop(self):
        """Iterates through the champions to buy array and makes sure it's a valid champion"""
        print(f"\nValidating champions to buy {settings.CHAMPIONS_TO_BUY}")
        for champion in settings.CHAMPIONS_TO_BUY:
            if champion not in champions.CHAMPIONS:
                raise Exception(f"Invalid champion {champion} in settings, ensure all champions are spelled properly")
            print(f"\tValid: {champion}")

    def callback(self, hwnd, extra) -> None: # pylint: disable=unused-argument
        """Function used to find the game window and get its size"""
        if "League of Legends (TM) Client" not in win32gui.GetWindowText(hwnd):
            return

        rect = win32gui.GetWindowRect(hwnd)

        x_pos = rect[0]
        y_pos = rect[1]
        width = rect[2] - x_pos
        height = rect[3] - y_pos

        if width < 200 or height < 200:
            return

        print(f"\tWindow {win32gui.GetWindowText(hwnd)} found")
        print(f"\t\tLocation: ({x_pos}, {y_pos})")
        print(f"\t\tSize:     ({width}, {height})")
        Vec4.setup_screen(x_pos, y_pos, width, height)
        Vec2.setup_screen(x_pos, y_pos, width, height)
        self.found_window = True

    def game_loop(self) -> None:
        """Loop that keeps the bot running"""
        while True:
            if (keyboard.is_pressed(settings.HOT_KEY) and settings.USE_HOT_KEY) or not settings.USE_HOT_KEY:
                self.buy_champions()
            sleep(0.01)

    def valid_champ(self, champ: str) -> str:
        """Matches champion string to a valid champion name string and returns it"""
        if champ in champions.CHAMPIONS:
            return champ

        for champion in champions.CHAMPIONS:
            if SequenceMatcher(a=champion, b=champ).ratio() >= 0.7:
                return champion
        return ""

    def get_champ(self, screen_capture: ImageGrab.Image, name_pos: Vec4, shop_pos: int, shop_array: list) -> str:
        """Returns a tuple containing the shop position and champion name"""
        champ = screen_capture.crop(name_pos.get_coords())
        champ = ocr.get_text_from_image(image=champ, whitelist="")
        if champ in champions.CHAMPIONS:
            shop_array.append((shop_pos, champ))
            return
        shop_array.append((shop_pos, self.valid_champ(champ)))

    def get_shop(self) -> list:
        """Returns the list of champions in the shop"""
        screen_capture = ImageGrab.grab(bbox=screen_coords.SHOP_POS.get_coords())
        shop = []
        thread_list = []
        for shop_index, name_pos in enumerate(screen_coords.CHAMP_NAME_POS):
            thread = threading.Thread(target=self.get_champ, args=(screen_capture, name_pos, shop_index, shop))
            thread_list.append(thread)
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()
        return shop

    def buy_champions(self) -> None:
        """Iterates through the shop and purchases champions that are in champions to buy array"""
        shop = self.get_shop()
        print(f"\nShop: {shop}")
        for champion in shop:
            if champion[1] in settings.CHAMPIONS_TO_BUY:
                mk_functions.left_click(screen_coords.BUY_LOC[champion[0]].get_coords())
                print(f"\tPurchased {champion[1]}")
        if settings.REROLL:
            mk_functions.reroll()
            print("\nRerolled shop")
