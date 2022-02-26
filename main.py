VERSION = "1.5" # DONT EDIT THIS!

import os
import sys
import json

from discord.ext import commands
from utils import console
from utils.config import *

console.clear()
console.title(f"Loading Shadow v{VERSION}...")

bot = commands.Bot(
    command_prefix=PREFIX, 
    help_command=None,
    self_bot=True
)

for cog_file in os.listdir("cogs"):
    if cog_file.endswith(".py"):
        bot.load_extension(f"cogs.{cog_file[:-3]}")

def restart_bot():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def split(word):
    return list(word)

@bot.event
async def on_connect():
    console.clear()
    console.title(f"Shadow v{VERSION} ─ Logged into {bot.user.name}")

    print(console.fg.consoleColour + "")
    print(".▄▄ ·  ▄ .▄ ▄▄▄· ·▄▄▄▄        ▄▄▌ ▐ ▄▌".center(os.get_terminal_size().columns))
    print("▐█ ▀. ██▪▐█▐█ ▀█ ██▪ ██ ▪     ██· █▌▐█".center(os.get_terminal_size().columns))
    print("▄▀▀▀█▄██▀▐█▄█▀▀█ ▐█· ▐█▌ ▄█▀▄ ██▪▐█▐▐▌".center(os.get_terminal_size().columns))
    print("▐█▄▪▐███▌▐▀▐█ ▪▐▌██. ██ ▐█▌.▐▌▐█▌██▐█▌".center(os.get_terminal_size().columns))
    print(" ▀▀▀▀ ▀▀▀ · ▀  ▀ ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ ▀▪".center(os.get_terminal_size().columns))
    print("")
    print(f"Shadow v{VERSION} logged into {bot.user.name}".center(os.get_terminal_size().columns))
    print("")
    print(console.fg.consoleColour + '─'*os.get_terminal_size().columns)
    print("")

@bot.event
async def on_command(ctx):
    await ctx.message.delete()
    console.print_cmd(f"{ctx.command.name}")

@bot.event
async def on_command_error(ctx, error):
    console.print_error(error)
    try:
        await ctx.message.delete()
    except:
        pass

bot.run(TOKEN)
