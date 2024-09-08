import discord
from discord.ext import commands
import os
import random
import cogs.combinebot
import json
import cogs.combinebot
from cogs.combinebot import name
from cogs.combinebot import game
from cogs.combinebot import icon
from cogs.combinebot import VERSION
from cogs.combinebot import LATESTADDITION
WORDS = ["rock", "paper", "scissors"]



class Rps(commands.Cog):
   
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @commands.slash_command(title="rps", description="Play Rock Paper Scissors with UltraBot!")
    async def rps(self, interaction, choice: discord.Option(str, description="Your choice! Choose either rock, paper, or scissors.", choices=["rock", "paper", "scissors"])): # type: ignore
        user_choice = choice.lower()
        bot_choice = random.choice(WORDS)
        if user_choice == bot_choice:
            final = "It's a TIE!"
        else:
            final = cogs.combinebot.rpswin(userchoice=user_choice, botchoice=bot_choice)
        embed = cogs.combinebot.makeEmbed(title=final, 
                                          description="You chose " + str(user_choice) + "\n CombineBot chose " + str(bot_choice),
                                          color=discord.Colour.red(),)

        await interaction.response.send_message(embed=embed)








def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Rps(bot)) # add the cog to the bot
