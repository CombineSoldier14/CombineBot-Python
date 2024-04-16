import discord
from discord.ext import commands
import os
import random
import json
WORDS = ["rock", "paper", "scissors"]

with open("version.json", "r") as f:
            _r = json.load(f)
            VERSION = _r["VERSION"]



class Rps(commands.Cog):
    group = discord.SlashCommandGroup(name="fun", description="Non-serious commands for fun and enjoyment")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @group.command(title="rps", description="Play Rock Paper Scissors with UltraBot!")
    async def rps(self, ctx, choice: discord.Option(str, description="Your choice! Choose either rock, paper, or scissors.")):
        user_choice = choice.lower()
        bot_choice = random.choice(WORDS)
        def win_status():
         
        
         if bot_choice == "rock" and user_choice == "paper":
            return "You WON!"

         if bot_choice == "rock" and user_choice == "scissors":
            return "You LOST!"

         if bot_choice == "paper" and user_choice == "rock":
            return "You LOST!"

         

         if bot_choice == "paper" and user_choice == "scissors":
            return "You WON!"

         if bot_choice == "scissors" and user_choice == "rock":
            return "You WON!"

         if bot_choice == "scissors" and user_choice == "paper":
            return "You LOST!"

         else:
            return "It's a TIE!"

        embed = discord.Embed(
            title=str(win_status()),
            description="You chose " + str(user_choice) + ", UltraBot chose " + str(bot_choice),
            color=discord.Colour.red(),
        )
        embed.set_footer(text="UltraBot " + VERSION, icon_url="https://cdn.discordapp.com/app-icons/1225220764861730867/f66bd4beb4f1ebee0685d8c5cfd646bb.png?size=256")

        await ctx.respond(embed=embed)








def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Rps(bot)) # add the cog to the bot
