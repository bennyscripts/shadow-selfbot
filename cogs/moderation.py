import discord
import requests

from discord.ext import commands
from utils.config import *


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="moderation", description="All available moderation commands.", usage="")
    async def moderation(self, ctx):
        commands_list = self.bot.get_cog("Moderation").get_commands()
        commands_str = ""

        for cmd in commands_list:
            if cmd.description[-1] == ".":
                cmd.description = cmd.description[:-1]

            commands_str += f"{PREFIX}{cmd.name}{cmd.usage} » {cmd.description}\n"

        await ctx.send(f"""```css
{requests.get(f'https://artii.herokuapp.com/make?text=MODERATION').text}
{commands_str}
```""")

    @commands.command(name="ban", description="Ban a user from the command server.", usage=" [@member] (reason)")
    async def ban(self, ctx, member: discord.Member, *, reason="Undefined"):
        if ctx.author.guild_permissions.ban_members:
            await member.ban()
            await ctx.send(f"**🔨 {member.name} was banned!**\n-Reason: {reason}")

    @commands.command(name="kick", description="Kick a user from the command server.", usage=" [@member] (reason)")
    async def kick(self, ctx, member: discord.Member, *, reason="Undefined"):
        if ctx.author.guild_permissions.kick_members:
            await member.kick(reason=reason)
            await ctx.send(f"**👢 {member.name} was kicked!**\n- Reason: {reason}")

    @commands.command(name="mute", description="Mute a user from the command server.", usage=" [@member] (reason)")
    async def mute(self, ctx, member: discord.Member, *, reason="Undefined"):
        if ctx.author.guild_permissions.mute_members:
            mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

            if not mutedRole:
                mutedRole = await ctx.guild.create_role(name="Muted")
                for channel in ctx.guild.channels:
                    await channel.set_permissions(mutedRole, send_messages=False)

            await member.add_roles(mutedRole)
            await ctx.send(f"**🤐 {member.name} was muted!**\n- Reason: {reason}")

    @commands.command(name="unmute", description="Unmute a user from the command server.", usage=" [@member] (reason)")
    async def unmute(self, ctx, member: discord.Member, *, reason="Undefined"):
        if ctx.author.guild_permissions.mute_members:
            mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
            
            if mutedRole not in member.roles:
                await member.remove_roles(mutedRole)
                await ctx.send(f"**😀 {member.name} was unmuted!**\nReason: {reason}")

            else:
                await ctx.send(f"**😐 {member.name} is not muted!**")

    @commands.command(name="lock", description="Lock the command channel.", usage=" (reason)")
    async def lock(self, ctx, *, reason="Undefined"):
        await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=False)
        await ctx.send("**🔒 Locked Channel!**")

    @commands.command(name="unlock", description="Unlock the command channel.", usage=" (reason)")
    async def unlock(self, ctx, *, reason="Undefined"):
        await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=True)
        await ctx.send("**🔓 Unlocked Channel!**")


def setup(bot):
    bot.add_cog(Moderation(bot))
