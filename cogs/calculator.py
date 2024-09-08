import discord
from discord.ext import commands
import os
from discord import reaction
from discord import Reaction
import random
import json
import cogs.combinebot
from cogs.combinebot import name
from cogs.combinebot import game
from cogs.combinebot import icon
from cogs.combinebot import VERSION
from cogs.combinebot import LATESTADDITION

class Calc(commands.Cog):
    group = discord.SlashCommandGroup(name="calc", description="Commands for calculating numbers")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
     
    @group.command(name="dndrng", description="Get a random number between 2 values and roll DND dice!")
    async def dndrng(self, interaction, 
                  d4: discord.Option(int, description="How many times to roll the D4 dice", required=False, default=0), # type: ignore
                  d6: discord.Option(int, description="How many times to roll the D6 dice", required=False, default=0), # type: ignore
                  d8: discord.Option(int, description="How many times to roll the D8 dice", required=False, default=0),# type: ignore
                  d10: discord.Option(int, description="How many times to roll the D10 dice", required=False, default=0),# type: ignore
                  d12: discord.Option(int, description="How many times to roll the D12 dice", required=False, default=0),# type: ignore
                  d20: discord.Option(int, description="How many times to roll the D20 dice", required=False, default=0),# type: ignore
                  d100: discord.Option(int, description="How many times to roll the D100 dice", required=False, default=0),# type: ignore
                  extraadd: discord.Option(int, description="Any extra numbers to add", required=False, default=0),# type: ignore
                  extraminus: discord.Option(int, description="Any extra numbers to subtract", required=False, default=0),# type: ignore
                  custommax: discord.Option(int, description="A custom maximum.", required=False, default=0),# type: ignore
                  custommin: discord.Option(int, description="A custom minimum. MUST be accompanied by a custom maximum!!!", required=False, default=0),# type: ignore
                  customamount: discord.Option(int, description="How many times to do the custom min/max", required=False, default=0)):# type: ignore
        total = 0
        for _d4 in range(d4):
            total += random.randint(1, 4)
        
        for _d6 in range(d6):
            total += random.randint(1, 6)

        for _d8 in range(d8):
            total += random.randint(1, 8)

        for _d10 in range(d10):
            total += random.randint(1, 10)

        for _d12 in range(d12):
            total += random.randint(1, 12)

        for _d20 in range(d20):
            total += random.randint(1, 20)

        for _d20 in range(d100):
            total += random.randint(1, 100)

       

        for _custom in range(customamount):
            total += random.randint(custommin, custommax)

        total += extraadd
        total -= extraminus

        if total > 1000:
            await interaction.response.send_message("Your number is too high!")
        else:
            await interaction.response.send_message(":game_die: " + str(total))


        

        
        
        
    
    @group.command(name="add", description="Adds 2 numbers together")
    async def add(self, interaction, value1: discord.Option(float, description="The first number to add", required=True), value2: discord.Option(float, description="The second number to add", required=True)): # type: ignore
        
        await interaction.response.send_message("**{0}** + **{1}** = **{2}**".format(str(value1), str(value2), str(value1 + value2)))

    @group.command(name="multiply", description="Multiplies 2 numbers together")
    async def multiply(self, interaction, value1: discord.Option(float, description="The first number to multiply", required=True), value2: discord.Option(float, description="The second number to multiply", required=True)): # type: ignore
        await interaction.response.send_message("**{0}** x **{1}** = **{2}**".format(str(value1), str(value2), str(value1 * value2)))

    @group.command(name="divide", description="Divides 2 numbers")
    async def divide(self, interaction, value1: discord.Option(float, description="The first number to divide", required=True), value2: discord.Option(float, description="The second number to divide", required=True)): # type: ignore
        if value1 == 0 or value2 == 0:
           await interaction.response.send_message("You can't divide things by zero, smarty.")
        else:
          await interaction.response.send_message("**{0}** / **{1}** = **{2}**".format(str(value1), str(value2), str(value1 / value2)))

    @group.command(name="minus", description="Subtract a mumber")
    async def minus(self, interaction, value1: discord.Option(float, description="The first number to subtract", required=True), value2: discord.Option(float, description="The second number to subtract", required=True)): # type: ignore
         await interaction.response.send_message("**{0}** - **{1}** = **{2}**".format(str(value1), str(value2), str(value1 - value2)))

    @group.command(name="exponent", description="Get the exponent of a number!")
    async def exponent(self, interaction, value: discord.Option(float, description="Number to power"), power: discord.Option(float, description="Power to set number to")): # type: ignore
         await interaction.response.send_message("**{0}** to the power of **{1}** is **{2}**".format(str(value), str(power), str(value**power)))
         
    
    








def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Calc(bot)) # add the cog to the b



