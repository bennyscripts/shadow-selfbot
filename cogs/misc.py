import discord
import main
import requests

from discord.ext import commands
from utils.config import *


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="misc", description="Main misc command.", usage="")
    async def misc(self, ctx):
        commands_list = self.bot.get_cog("Misc").get_commands()
        commands_str = ""

        for cmd in commands_list:
            if cmd.description[-1] == ".":
                cmd.description = cmd.description[:-1]

            commands_str += f"{PREFIX}{cmd.name}{cmd.usage} » {cmd.description}\n"

        await ctx.send(f"""```css
{requests.get(f'https://artii.herokuapp.com/make?text=MISC').text}
{commands_str}
```""")

    @commands.command(name="settings", description="Shows selfbot settings.", usage="")
    async def settings(self, ctx):
        totalcommands = len(self.bot.commands)

        await ctx.send(f"**⚙ Settings**\n- Commands: {totalcommands}\n- Prefix: {self.bot.command_prefix}")

    @commands.command(name="restart", description="Restart Shadow selfbot.", usage="", aliases=["reboot", "reload"])
    async def restart(self, ctx):
        await ctx.send(f"**🔁 Restarting...**")
        main.restart_bot()

    @commands.command(name="playing", description="Set a playing status.", usage=" [status]")
    async def playing(self, ctx, *, status):
        await self.bot.change_presence(activity=discord.Activity(type=0, name=f"{status}"))
        await ctx.send(f"**🎮 Playing Status**\nPlaying status changed to `{status}`")

    @commands.command(name="streaming", description="Set a streaming status.", usage=" [status]")
    async def streaming(self, ctx, *, status):
        await self.bot.change_presence(activity=discord.Activity(type=1, name=f"{status}"))
        await ctx.send(f"**📸 Streaming Status**\nStreaming status changed to `{status}`")

    @commands.command(name="listening", description="Set a listening status.", usage=" [status]")
    async def listening(self, ctx, *, status):
        await self.bot.change_presence(activity=discord.Activity(type=2, name=f"{status}"))
        await ctx.send(f"**🎧 Listening Status**\nListening status changed to `{status}`")

    @commands.command(name="watching", description="Set a watching status.", usage=" [status]")
    async def watching(self, ctx, *, status):
        await self.bot.change_presence(activity=discord.Activity(type=3, name=f"{status}"))
        await ctx.send(f"**💻 Watching Status**\nWatching status changed to `{status}`")

    @commands.command(name="clearstatus", description="Clear your custom status.", usage="")
    async def clearstatus(self, ctx):
        await self.bot.change_presence(activity=discord.Activity(type=-1))
        await ctx.send(f"**🗑 Status Cleared**")

    @commands.command(name="nick", description="Change your nickname.", usage=" [nickname]")
    async def nick(self, ctx, nickname="Shadow Selfbot Is The Best"):
        await ctx.author.edit(nick=nickname)
        await ctx.send(f"**🏷 Nickname**\nNickname change to `{nickname}`")

def setup(bot):
    bot.add_cog(Misc(bot))
