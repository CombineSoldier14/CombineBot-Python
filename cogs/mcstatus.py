import discord
from discord.ext import commands
import os
import json
import mcstatus
from mcstatus import JavaServer
from mcstatus import BedrockServer
import cogs.combinebot
from cogs.combinebot import name
from cogs.combinebot import game
from cogs.combinebot import icon
from cogs.combinebot import VERSION
from cogs.combinebot import LATESTADDITION



class Mcstatus(commands.Cog):
    group = discord.SlashCommandGroup(name="minecraft", description="Commands related to Minecraft!")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @group.command(name="mcjava", description="Get the status of a minecraft java server!")
    async def mcjava(self, interaction, host: discord.Option(str, description="Server URL to get info on.", required=True), port: discord.Option(int, description="The port of the Minecraft server", default=25565)): # type: ignore
           await interaction.defer()
           addr = "{0}:{1}".format(host, port)
           serverjava = JavaServer.lookup(addr)
           javastatus = serverjava.status()
           javalatency = javastatus.latency
           javaonline = javastatus.players.online
           javamaximum = javastatus.players.max
           javaprotocol = javastatus.version.protocol
           javaversion = javastatus.version.name
           
           
           embed = cogs.combinebot.makeEmbed(
                  title="Info for {0}:{1}".format(host, port),
                  description="Info on the current minecraft server",
                  color=discord.Colour.green(),
           )
           embed.add_field(name="Player(s) Online", value="{0}/{1}".format(javaonline, javamaximum))
           embed.add_field(name="Latency", value=f"{javalatency} ms")
           embed.add_field(name="Version/Protocol", value="{0} (Protocol {1})".format(javaversion, javaprotocol))
           embed.add_field(name="Secure Chat?", value=str(javastatus.enforces_secure_chat))
           embed.set_thumbnail(url="https://static-00.iconduck.com/assets.00/java-icon-1511x2048-6ikx8301.png")
           
           await interaction.followup.send(embed=embed)

    @group.command(name="mcbedrock", description="Get the status of a minecraft bedrock server!")
    async def mcbedrock(self, interaction, hosturl: discord.Option(str, description="Server URL to get info on.", required=True), portnumber: discord.Option(int, description="The port of the Minecraft server", default=25565)): # type: ignore
           await interaction.defer()
           bedrockaddr = "{0}:{1}".format(hosturl, portnumber)
           serverbedrock = BedrockServer.lookup(bedrockaddr)
           bedrockstatus = serverbedrock.status()
           bedrocklatency = bedrockstatus.latency
           bedrockonline = bedrockstatus.players.online
           bedrockmaximum = bedrockstatus.players.max
           bedrockprotocol = bedrockstatus.version.protocol
           bedrockversion = bedrockstatus.version.name
           
           
           embed = cogs.combinebot.makeEmbed(
                  title="Info for {0}:{1}".format(hosturl, portnumber),
                  description="Info on the current minecraft server",
                  color=discord.Colour.green(),
           )
           embed.add_field(name="Player(s) Online", value="{0}/{1}".format(bedrockonline, bedrockmaximum))
           embed.add_field(name="Latency", value=f"{bedrocklatency} ms")
           embed.add_field(name="Version/Protocol", value="{0} (Protocol {1})".format(bedrockversion, bedrockprotocol))
           embed.set_thumbnail(url="https://gamepedia.cursecdn.com/minecraft_gamepedia/6/68/Bedrock_JE2_BE2.png?version=fe113612ba2231b70dbf6627c699e644")
           
           
           await interaction.followup.send(embed=embed)


    

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Mcstatus(bot)) # add the cog to the bot

           



           

           



           
