import discord
from discord.ext import commands
import os
import json
import cogs.lists
from cogs.lists import mbtilist
from cogs.lists import mbtifuncs
import cogs.combinebot
from cogs.combinebot import name
from cogs.combinebot import game
from cogs.combinebot import icon
from cogs.combinebot import VERSION
from cogs.combinebot import LATESTADDITION

class Cogfunc(commands.Cog):
    group = discord.SlashCommandGroup(name="cogfunc", description="Commands relating to the Myers-Briggs Type Indicator cognitive functions system")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    

    
          
          

    @group.command(title="mbtifinder", description="Tells you an MBTI via specified dominant/secondary functions.")
    async def mbtifinder(self, interaction, dom: discord.Option(str, description="Dominant function", choices=["Ti", "Te", "Fi", "Fe", "Si", "Se", "Ni", "Ne"]), sec: discord.Option(str, description="Secondary function", choices=["Ti", "Te", "Fi", "Fe", "Si", "Se", "Ni", "Ne"])): # type: ignore
            for functions in mbtifuncs:
                if dom == functions["dom"] and sec == functions["sec"]:
                    mbti = functions["mbti"]
                    stack = functions["stack"]
                    await interaction.response.send_message("The dominant function **{0}** and secondary function **{1}** belong to the MBTI **{2}**. Their full stack is **{3}**.".format(dom, sec, mbti, stack))
                    return
                else:
                    await interaction.response.send_message(":x: The functions \"**{0}-{1}**\" do not belong to any MBTI.".format(dom, sec))
                    return
                
                
    @group.command(name="mbtifunctions", description="Shows you the cognitive function stack for an MBTI")
    async def mbtifunctions(self, interaction, mbti: discord.Option(str, description="The MBTI to get the stack of. Will be random if left blank.", choices=mbtilist)): # type: ignore
        stack = ""
        for functionz in mbtifuncs:
             if mbti == functionz["mbti"]:
                  stack = functionz["stack"]
                  await interaction.response.send_message("The MBTI **{0}** has the stack of **{1}**.".format(mbti, stack))
                  return
            


            


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Cogfunc(bot)) # add the cog to the bot

