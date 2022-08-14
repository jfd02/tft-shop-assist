"""
Handles sending input to the game, coords contain a cartesian ordered pair (x, y)
"""

import pydirectinput

def left_click(coords: tuple) -> None:
    """Left clicks at argument ones coordinates"""
    pydirectinput.moveTo(coords[0], coords[1])
    pydirectinput.mouseDown()
    pydirectinput.mouseUp()

def reroll() -> None:
    """Presses hotkey to purchase reroll"""
    pydirectinput.press("d")
