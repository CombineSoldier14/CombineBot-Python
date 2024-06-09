import discord
from discord.ext import commands
import os
import json
import mcstatus
from mcstatus import JavaServer
from mcstatus import BedrockServer

with open("version.json", "r") as f:
            _r = json.load(f)
            VERSION = _r["VERSION"]

with open("dev.json", "r") as f:
            _r = json.load(f)
            dev_status = _r["DEV_STATUS"]

#The Dev status is meant for if UltraBot is running in DEV mode which changes some names and icons.

if dev_status == "true":
            name = "UltraBot Development Edition"
            game = "with unstable ass commands"
            icon = "https://cdn.discordapp.com/app-icons/1227477531461025854/85f59950e14cca56e4b1bcefd911ca23.png?size=256"

if dev_status == "false":
            name = "UltraBot"
            game = "combinesoldier14.site"
            icon = "https://cdn.discordapp.com/app-icons/1225220764861730867/f66bd4beb4f1ebee0685d8c5cfd646bb.png?size=256"




class Mcstatus(commands.Cog):
    group = discord.SlashCommandGroup(name="minecraft", description="Commands related to Minecraft!")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @group.command(name="mcjava", description="Get the status of a minecraft java server!")
    async def mcjava(self, ctx, host: discord.Option(str, description="Server URL to get info on.", required=True), port: discord.Option(int, description="The port of the Minecraft server", default=25565)):
           await ctx.defer()
           addr = "{0}:{1}".format(host, port)
           serverjava = JavaServer.lookup(addr)
           javastatus = serverjava.status()
           javalatency = javastatus.latency
           javaonline = javastatus.players.online
           javamaximum = javastatus.players.max
           javaprotocol = javastatus.version.protocol
           javaversion = javastatus.version.name
           
           
           embed = discord.Embed(
                  title="Info for {0}:{1}".format(host, port),
                  description="Info on the current minecraft server",
                  color=discord.Colour.green(),
           )
           embed.add_field(name="Player(s) Online", value="{0}/{1}".format(javaonline, javamaximum))
           embed.add_field(name="Latency", value=f"{javalatency} ms")
           embed.add_field(name="Version/Protocol", value="{0} (Protocol {1})".format(javaversion, javaprotocol))
           embed.add_field(name="Secure Chat?", value=str(javastatus.enforces_secure_chat))
           embed.set_thumbnail(url="https://static-00.iconduck.com/assets.00/java-icon-1511x2048-6ikx8301.png")
           embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
           
           
           await ctx.respond(embed=embed)

    @group.command(name="mcbedrock", description="Get the status of a minecraft bedrock server!")
    async def mcbedrock(self, ctx, hosturl: discord.Option(str, description="Server URL to get info on.", required=True), portnumber: discord.Option(int, description="The port of the Minecraft server", default=25565)):
           await ctx.defer()
           bedrockaddr = "{0}:{1}".format(hosturl, portnumber)
           serverbedrock = BedrockServer.lookup(bedrockaddr)
           bedrockstatus = serverbedrock.status()
           bedrocklatency = bedrockstatus.latency
           bedrockonline = bedrockstatus.players.online
           bedrockmaximum = bedrockstatus.players.max
           bedrockprotocol = bedrockstatus.version.protocol
           bedrockversion = bedrockstatus.version.name
           
           
           embed = discord.Embed(
                  title="Info for {0}:{1}".format(hosturl, portnumber),
                  description="Info on the current minecraft server",
                  color=discord.Colour.green(),
           )
           embed.add_field(name="Player(s) Online", value="{0}/{1}".format(bedrockonline, bedrockmaximum))
           embed.add_field(name="Latency", value=f"{bedrocklatency} ms")
           embed.add_field(name="Version/Protocol", value="{0} (Protocol {1})".format(bedrockversion, bedrockprotocol))
           embed.set_thumbnail(url="https://gamepedia.cursecdn.com/minecraft_gamepedia/6/68/Bedrock_JE2_BE2.png?version=fe113612ba2231b70dbf6627c699e644")
           embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
           
           
           await ctx.respond(embed=embed)


    

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Mcstatus(bot)) # add the cog to the bot

           



           
