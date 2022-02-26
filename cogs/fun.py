import discord
import random
import string
import requests

from datetime import datetime
from discord.ext import commands
from utils.config import *

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="fun", description="All available fun commands.", usage="")
    async def fun(self, ctx):
        commands_list = self.bot.get_cog("Fun").get_commands()
        commands_str = ""

        for cmd in commands_list:
            if cmd.description[-1] == ".":
                cmd.description = cmd.description[:-1]

            commands_str += f"{PREFIX}{cmd.name}{cmd.usage} » {cmd.description}\n"

        await ctx.send(f"""```css
{requests.get(f'https://artii.herokuapp.com/make?text=FUN').text}
{commands_str}
```""")

    @commands.command(name="coinflip", description="Flip a coin!", usage="")
    async def coinflip(self, ctx):
        choices = ["Heads", "Tails"]
        choice = random.choice(choices)

        await ctx.send(f"**🪙 Coinflip**\n- The coin landed on `{choice}`")

    @commands.command(name="dice", description="Roll a six sided dice.", usage="")
    async def dice(self, ctx):
        choice = random.randint(1, 6)

        await ctx.send(f"**🎲 Dice roll**\n- The dice rolled `{choice}`")

    @commands.command(name="8ball", description="Ask the magic eight ball a question.", usage=" [question]")
    async def eightball(self, ctx, *, question):
        choices = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes – definitely.", "You may rely on it."]
        choice = random.choice(choices)

        await ctx.send(f"**🎱 {choice}**\n- *Your question: {question}*")

    @commands.command(name="pp", description="Show someone's penis size.", usage=" [@user]")
    async def pp(self, ctx, user: discord.User):
        choice = "8" + "=" * random.randint(1, 12) + "D"
        size = len(choice)

        await ctx.send(f"**🍆 dick size**\n- {user.name} has a {size}\" dick\n- {choice}")

    @commands.command(name="rps", description="Rock paper scissors.", usage=" [move]")
    async def rps(self, ctx, move):
        choices = ["rock", "paper", "scissors"]
        beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

        computer = random.choice(choices)
        player = move.lower()

        if player not in beats: await ctx.send("**❌ Invalid move**\n- Valid moves are `rock`, `paper` and `scissors`.")

        elif player == computer: await ctx.send("**👔 It's a tie**")

        elif beats[player] == computer: await ctx.send(f"**🎉 You win**\n- `{player}` beats `{computer}`")

        else: await ctx.send(f"**😢 You lost**\n- `{computer}` beats `{player}`.")

    @commands.command(name="nitrogen", description="Generate a nitro gift code.", usage=" (amount)")
    async def nitrogen(self, ctx, amount: int = 1):
        nitro_links = []

        for _ in range(amount):
            nitro = "https://discord.gift/" + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(19))
            nitro_links.append(nitro)
        
        nitro_links_str = '\n'.join('- ' + nitro for nitro in nitro_links)
        await ctx.send(f"**🎁 Nitro Generator**\n{nitro_links_str}")

    @commands.command(name="selfbotcheck", description="Check for selfbot users.", usage="")
    async def selfbotcheck(self, ctx):
        await ctx.send("🎉 **GIVEAWAY** 🎉")

def setup(bot):
    bot.add_cog(Fun(bot))
