import discord
import requests

from discord.ext import commands
from utils.config import *


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="info", description="All available info commands.", usage="")
    async def info(self, ctx):
        commands_list = self.bot.get_cog("Info").get_commands()
        commands_str = ""

        for cmd in commands_list:
            if cmd.description[-1] == ".":
                cmd.description = cmd.description[:-1]

            commands_str += f"{PREFIX}{cmd.name}{cmd.usage} » {cmd.description}\n"

        await ctx.send(f"""```css
{requests.get(f'https://artii.herokuapp.com/make?text=INFO').text}
{commands_str}
```""")

    @commands.command(name="userinfo", description="Show information of a discord user.", usage=" [@user]")
    async def userinfo(self, ctx, user: discord.User):
        createdAt = user.created_at.strftime("%d %B, %Y")
        
        await ctx.send(f"**🧑‍🦱 {user.name}'s information**\n- ID: {user.id}\n- Username: {user.name}\n- Discriminator: {user.discriminator}\n- Created At: {createdAt}")

    @commands.command(name="serverinfo", description="Show information of the command server.", usage="")
    async def serverinfo(self, ctx):
        guild = ctx.message.guild
        createdAt = guild.created_at.strftime("%d %B, %Y")

        await ctx.send(f"**🖥 {guild.name}'s information**\n- ID: {guild.id}\n- Name: {guild.name}\n- Owner: {guild.owner}\n- Created At: {createdAt}")

def setup(bot):
    bot.add_cog(Info(bot))
