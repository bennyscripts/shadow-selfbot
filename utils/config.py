import json
import os

from .console import clear

TOKEN = json.load(open("config/config.json"))["token"]
PREFIX = json.load(open("config/config.json"))["prefix"]
VERSION = "1.5"

TITLE = "SHADOW"

def check():
    if not os.path.exists("config/config.json"):
        with open("config/config.json", "w") as f:
            json.dump({"token": "", "prefix": ""}, f, indent=4)

    if json.load(open("config/config.json"))["token"] == "":
        clear()

        print("")
        print("Please input your Discord token below.".center(os.get_terminal_size().columns))
        print("")
        token = input()

        config = json.load(open("config/config.json"))
        config["token"] = (token)
        json.dump(config, open('config/config.json', 'w'), indent=4)

    if json.load(open("config/config.json"))["prefix"] == "":
        clear()

        print("")
        print("Please input the prefix you would like to use to run commands below.".center(os.get_terminal_size().columns))
        print("")
        prefix = input()

        config = json.load(open("config/config.json"))
        config["prefix"] = (prefix)
        json.dump(config, open('config/config.json', 'w'), indent=4)