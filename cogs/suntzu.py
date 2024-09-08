import discord
import os
from discord.ext import commands
from random import uniform
from cogs.combinebot import name
from cogs.combinebot import game
from cogs.combinebot import icon
from cogs.combinebot import VERSION
from cogs.combinebot import LATESTADDITION
from cogs.combinebot import getSunTzu

class SunTzu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.slash_command(name="suntzuquotes", description="Get a random Sun Tzu quote!")
    async def suntzuquotes(self, interaction):
            await interaction.response.send_message("""> \"_{0}_\" 
                            - Sun Tzu, _The Art of War_
                              
                              """.format(getSunTzu()))


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(SunTzu(bot)) # add the cog to the bot
