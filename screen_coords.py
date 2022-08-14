"""
Contains static screen coordinates the bot uses
Screen coords for 1920x1080 screens
(x, y, x+w, y+h) for Vec4 locations, (x, y) for Vec2 locations
"""

from vec4 import Vec4, GameWindow
from vec2 import Vec2

SHOP_POS = Vec4(GameWindow(481, 1039, 1476, 1070))

CHAMP_NAME_POS = [Vec4(GameWindow(3, 5, 120, 24), use_screen_offset=False),
                  Vec4(GameWindow(204, 5, 320, 24), use_screen_offset=False),
                  Vec4(GameWindow(407, 5, 522, 24), use_screen_offset=False),
                  Vec4(GameWindow(608, 5, 712, 24), use_screen_offset=False),
                  Vec4(GameWindow(808, 5, 912, 24), use_screen_offset=False)]

GOLD_POS = Vec4(GameWindow(870, 883, 920, 909))

BUY_LOC = [Vec2(575, 992), Vec2(775, 992), Vec2(
    975, 992), Vec2(1175, 992), Vec2(1375, 992)]
    