import os
import sys

from datetime import datetime
from sty import fg, bg, ef, rs, Style, RgbFg

__consolecolour__ = "#A7A7A7"
fg.consoleColour = Style(RgbFg(int(__consolecolour__[1:3], 16), int(__consolecolour__[3:5], 16), int(__consolecolour__[5:7], 16)))

fg.cRed = Style(RgbFg(255, 81, 69))
fg.cOrange = Style(RgbFg(255, 165, 69))
fg.cYellow = Style(RgbFg(255, 255, 69))
fg.cGreen = Style(RgbFg(35, 222, 57))
fg.cBlue = Style(RgbFg(69, 119, 255))
fg.cPurple = Style(RgbFg(177, 69, 255))
fg.cPink = Style(RgbFg(255, 69, 212))

fg.cGrey = Style(RgbFg(207, 207, 207))
fg.cBrown = Style(RgbFg(199, 100, 58))
fg.cBlack = Style(RgbFg(0, 0, 0))
fg.cWhite = Style(RgbFg(255, 255, 255))

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def title(text):
    if sys.platform == "win32":
        os.system("title " + text)
    elif sys.platform == "linux":
        print(f"\033]0;{text}\007")
    elif sys.platform == "darwin":
        print(f"\033]0;{text}\007")

def print_cmd(command):
    print(f"{fg.consoleColour}[{fg.cWhite}" + datetime.now().strftime("%H:%M:%S") + f"{fg.consoleColour}]{fg.cWhite} | {fg.consoleColour}[{fg.cWhite}Command{fg.consoleColour}] {fg.cWhite}{command}")

def print_sharecmd(user, command):
    print(f"{fg.consoleColour}[{fg.cWhite}" + datetime.now().strftime("%H:%M:%S") + f"{fg.consoleColour}]{fg.cWhite} | {fg.consoleColour}[{fg.cWhite}Share Command{fg.consoleColour}] {fg.cWhite}({user}) {command}")

def print_error(error):
    print(f"{fg.consoleColour}[{fg.cWhite}" + datetime.now().strftime("%H:%M:%S") + f"{fg.consoleColour}]{fg.cWhite} | {fg.consoleColour}[{fg.cWhite}Error{fg.consoleColour}] {fg.cWhite}{error}")

def print_sniper(sniper, message):
    print(f"{fg.consoleColour}[{fg.cWhite}" + datetime.now().strftime("%H:%M:%S") + f"{fg.consoleColour}]{fg.cWhite} | {fg.consoleColour}[{fg.cWhite}{sniper}{fg.consoleColour}] {fg.cWhite}{message}")