import discord
import main
import requests

from datetime import datetime
from discord.ext import commands
from utils.config import *

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", description="Main help command.", usage="")
    async def help(self, ctx, *, command = None):
        if command is None:
            await ctx.send(f"""```css
{requests.get(f'https://artii.herokuapp.com/make?text={TITLE}').text}
Arguments in [] are required, arguments in () are optional.

{PREFIX}fun » All available fun commands.
{PREFIX}text » All available text commands.
{PREFIX}misc » All available misc commands.
{PREFIX}info » All available info commands.
{PREFIX}moderation » All available moderation commands.

{PREFIX}search [term] » Search through Shadow.
{PREFIX}help [command] » Get help with command.
```""")

        else:
            for cmd in self.bot.commands:
                if command == cmd.name:
                    await ctx.send(f"""
**{PREFIX}{cmd.name}**
- Usage:{cmd.usage}
- Description: {cmd.description}
""")

    @commands.command(name="search", description="Search for a command.", usage=" [term]")
    async def search(self, ctx, command = None):
        if command is not None:
            text = ""
            for cmd in self.bot.commands:
                if command in cmd.name or command in cmd.description:
                    text += f"`{PREFIX}`**{cmd.name}{cmd.usage}** » {cmd.description}\n"

            searchedItems = len(text.split("\n"))

            await ctx.send(f"**🔎 Search results...**\nFound `{searchedItems}` items for `{command}`.\n\n{text}")

def setup(bot):
    bot.add_cog(General(bot))
