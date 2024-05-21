import discord
from discord.ext import commands
import os
from discord import reaction
from discord import Reaction
import random
import json

with open("dev.json", "r") as f:
            _r = json.load(f)
            dev_status = _r["DEV_STATUS"]

with open("version.json", "r") as f:
            _r = json.load(f)
            VERSION = _r["VERSION"]



#The Dev status is meant for if UltraBot is running in DEV mode which changes some names and icons.


if dev_status == "true":
            name = "UltraBot Development Edition"
            game = "with unstable ass commands"
            icon = "https://cdn.discordapp.com/app-icons/1227477531461025854/85f59950e14cca56e4b1bcefd911ca23.png?size=256"

if dev_status == "false":
            name = "UltraBot"
            game = "Ace Attorney: Dual Destinies"
            icon = "https://cdn.discordapp.com/app-icons/1225220764861730867/f66bd4beb4f1ebee0685d8c5cfd646bb.png?size=256"


calc = discord.SlashCommandGroup(name="calc", description="Commands for calculating numbers")

class Calc(commands.Cog):
    group = discord.SlashCommandGroup(name="calc", description="Commands for calculating numbers")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
     
    @group.command(name="dndrng", description="Get a random number between 2 values and roll DND dice!")
    async def dndrng(self, ctx, 
                  d4: discord.Option(int, description="How many times to roll the D4 dice", required=False, default=0), 
                  d6: discord.Option(int, description="How many times to roll the D6 dice", required=False, default=0),
                  d8: discord.Option(int, description="How many times to roll the D8 dice", required=False, default=0),
                  d10: discord.Option(int, description="How many times to roll the D10 dice", required=False, default=0),
                  d12: discord.Option(int, description="How many times to roll the D12 dice", required=False, default=0),
                  d20: discord.Option(int, description="How many times to roll the D20 dice", required=False, default=0),
                  d100: discord.Option(int, description="How many times to roll the D100 dice", required=False, default=0),
                  extraadd: discord.Option(int, description="Any extra numbers to add", required=False, default=0),
                  extraminus: discord.Option(int, description="Any extra numbers to subtract", required=False, default=0),
                  custommax: discord.Option(int, description="A custom maximum.", required=False, default=0),
                  custommin: discord.Option(int, description="A custom minimum. MUST be accompanied by a custom maximum!!!", required=False, default=0),
                  customamount: discord.Option(int, description="How many times to do the custom min/max", required=False, default=0)):
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
            await ctx.respond("Your number is too high!")
        else:
            await ctx.respond(":game_die: " + str(total))


        

        
        
        
    
    @group.command(name="add", description="Adds 2 numbers together")
    async def add(self, ctx, value1: discord.Option(float, description="The first number to add", required=True), value2: discord.Option(float, description="The second number to add", required=True)):
        
        await ctx.respond("**{0}** + **{1}** = **{3}**".format(str(value1), str(value2), str(value1 + value2)))

    @group.command(name="multiply", description="Multiplies 2 numbers together")
    async def multiply(self, ctx, value1: discord.Option(int, description="The first number to multiply", required=True), value2: discord.Option(int, description="The second number to multiply", required=True)):
        await ctx.respond(str(value1 * value2))

    @group.command(name="divide", description="Divides 2 numbers")
    async def divide(self, ctx, value1: discord.Option(int, description="The first number to divide", required=True), value2: discord.Option(int, description="The second number to divide", required=True)):
        if value1 == 0 or value2 == 0:
           await ctx.respond("You can't divide things by zero, smarty.")
        else:
          await ctx.respond(str(value1 / value2))

    








def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Calc(bot)) # add the cog to the b

