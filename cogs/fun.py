import discord
from discord.ext import commands
import os
from discord import default_permissions
from discord import permissions
from discord import Permissions
from discord import PermissionOverwrite
import cowsay
import nltk
import random
import json
import cogs.combinebot
from cogs.combinebot import name
from cogs.combinebot import game
from cogs.combinebot import icon
from cogs.combinebot import VERSION
from cogs.combinebot import LATESTADDITION


nltk.download('words')

word_list = ["Heads", "Tails"]
eightball_list = ["It is certain.", "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again", "Ask again later", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]



class Fun(commands.Cog):
    group = discord.SlashCommandGroup(name="fun", description="Commands made for having fun!")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

 
    @group.command(name="cowsay", description="The cowsay command from Linux!")
    async def cowsay(self, interaction, text=discord.Option(str, description="Text for cow to say", required=True), 
                     character=discord.Option(str, description="Character for cowsay to use."), 
                     choices=cowsay.char_names, default="cow"):
        await interaction.response.send_message("```\n{0}\n```".format(cowsay.get_output_string(character, text))),
    
    @group.command(name="randomword", description="Gives you a random English word!")
    async def randomword(self, interaction):
        await interaction.response.send_message("Your Random Word: `" + random.choice(nltk.corpus.words.words()) + "`")
    
    @group.command(name="coinflip", description="Flip a coin!")
    async def coinflip(self, interaction):
        await interaction.response.send_message(":coin: **" + random.choice(word_list) + "**")

    @group.command(name="8ball", description="The Magic 8 Ball answers your question!")
    async def _8ball(self, interaction, text=discord.Option(str, description="Question to ask the 8 ball")):
        embed = discord.Embed(
            title="Magic 8 Ball: " + text,
            description=random.choice(eightball_list),
            color=discord.Colour.darker_gray(),
            
        )
        embed.set_thumbnail(url="https://icons.iconarchive.com/icons/barkerbaggies/pool-ball/256/Ball-8-icon.png")
        embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
        await interaction.response.send_message(embed=embed)

    @group.command(name="randomyt", description="Get a random youtube video")
    async def randomyt(self, interaction):
         await interaction.response.send_message(cogs.combinebot.getYTvideo())
         await interaction.send("NOTE: Not all generated videos may exist.")

    @group.command(name="aaquote", description="Get a random Ace Attorney quote!")
    async def aaquote(self, interaction):
          await interaction.response.send_message(
                cogs.combinebot.getAceAttorneyQuote()
          )

    @group.command(name="edgeworthcube", description="Roll the Edgeworth cube!")
    #credit to u/TheFinkrat for making the edgey cubes
    async def edgeworthcube(self, interaction):
        imgs = [
            "https://i.postimg.cc/HJhx1kxq/CRINGE.png",
            "https://i.postimg.cc/DWZZNX2Q/FALSE.png",
            "https://i.postimg.cc/JsK0KqW4/MAYBE.png",
            "https://i.postimg.cc/gxGrv7QT/MISINFORMED.png"
        ]
        embed = cogs.combinebot.makeEmbed(
            title="Edgeworth Cube",
            color=discord.Colour.blurple()
        )
        embed.set_image(url=random.choice(imgs))
        await interaction.response.send_message(embed=embed)
        

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Fun(bot)) # add the cog to the bot
