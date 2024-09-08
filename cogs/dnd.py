import discord
from discord.ext import commands
import os
import random
import cogs.requestHandler as handler
from random import uniform
import json
import requests
import cogs.combinebot
from cogs.combinebot import name
from cogs.combinebot import game
from cogs.combinebot import icon
from cogs.combinebot import VERSION
from cogs.combinebot import LATESTADDITION




class Dnd(commands.Cog):
    group = discord.SlashCommandGroup(name="dnd", description="Commands relating to the board game Dungeons and Dragons")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @group.command(name="dndmodifier", description="Get info on DND modifiers!")
    async def dndmodifier(self, interaction, mod: discord.Option(str, description="The modifier to get info on", choices=["STR", "DEX", "CON", "INT", "WIS", "CHA"])): # type: ignore
        j = cogs.combinebot.getDNDmod(mod=mod)
       
        skillz = ""
        for skill in j["skills"]:
           skillz = skillz + "{}, ".format(skill["name"])
        
        if mod == "CON":
           skillz = "None"
        
        embed = discord.Embed(
            title = "{0} ({1})".format(j["full_name"], j["name"]),
            description = "{0} {1}".format(j["desc"][0], j["desc"][1]),
            color = discord.Colour.blurple(),
        )
        embed.set_footer(text="Skills: {}".format(skillz))
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/9/9c/Purple_d20.png")
        await interaction.response.send_message(embed=embed)
        
        








def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Dnd(bot)) # add the cog to the bot


