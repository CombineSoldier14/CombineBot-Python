import discord
from discord.ext import commands
import os
import time
import json
import uuid
import string
import random
import time
import cogs.combinebot
from cogs.combinebot import name
from cogs.combinebot import game
from cogs.combinebot import icon
from cogs.combinebot import VERSION
from cogs.combinebot import LATESTADDITION



class Utilitycog(commands.Cog):
    group = discord.SlashCommandGroup(name="utility", description="Useful utility commands")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @group.command(name="avatar", description="Find the avatar of the mentioned user!")
    async def avatar(self, interaction, user: discord.Option(discord.Member, description="Member to get avatar of", required=True)):
      await interaction.response.send_message(user.display_avatar)


    @group.command(name="makeembed", description="Make your own embed!")
    async def makeembed(self, interaction, title: discord.Option(str, description="Title of embed"), 
                        description: discord.Option(str, description="Description of embed"), 
                        footer: discord.Option(str, description="Footer of embed"), 
                        color: discord.Option(int, description="Color of embed in hex format")):
        embed = cogs.combinebot.makeEmbed(title=title, description=description, color=color)
        embed.set_footer(text=footer)
        await interaction.response.send_message(embed=embed)

    
    @group.command(name="gettime", description="Returns the current date and time.")
    async def gettime(self, interaction):
        await interaction.response.send_message(time.ctime())

    @group.command(name="timestop", description="Stop time in a server JJBA style")
    @commands.has_permissions(manage_channels=True)
    async def timestop(self, interaction):
        await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=False)
        embed = cogs.combinebot.makeEmbed(title="ZA WARUDO!", 
                                          description="Time has been stopped! No messages can be sent except for admins.", 
                                          color=discord.Colour.red(), 
                                          footer="{0} v{1}".format(name, VERSION), icon_url=icon)
        embed.set_image(url="https://i.redd.it/05vtn9chak101.gif")
        await interaction.response.send_message(embed=embed)

    @group.command(name="resume", description="Resumes time in a server")
    @commands.has_permissions(manage_channels=True)
    async def resume(self, interaction):
        await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=True)
        await interaction.response.send_message("Time has been resumed!")
    
    @group.command(name="userinfo", description="Gets info on a user in the server!")
    async def userinfo(self, interaction, user: discord.Option(discord.Member, description="User to get info of", required=True)):
        if user.bot == True:
         embed = cogs.combinebot.makeEmbed(title="Info on {0}".format(user), 
                                           description="""
             **ID:** {0}
**Joined Discord:** {1}
**Discriminator:** {2} 
**Is A Bot?:** Yes
             """.format(user.id, user.created_at, user.discriminator),
             color=user.color)
         embed.set_thumbnail(url=user.avatar)
        
        if user.bot == False:
    
         embed = cogs.combinebot.makeEmbed(title="Info on {0}".format(user), 
                                           description="""
             **ID:** {0}
**Joined Discord:** {1} 
**Is A Bot?:** No 
             """.format(user.id, user.created_at, user.discriminator),
             color=user.color)
         embed.set_thumbnail(url=user.avatar)
        await interaction.response.send_message(embed=embed)
          

    @group.command(name="botinfo", description="Info about CombineBot!")
    async def botinfo(self, interaction):
         embed = cogs.combinebot.makeEmbed(title="Bot Info", 
                                           description="""
**Bot Name:** {0}
**Bot Owner:** @combinesoldier14
**Creation Date:** 4/5/2024
**Library**: Py-cord v{1}
              """.format(name, discord.__version__),
              color=discord.Colour.og_blurple())
         embed.set_thumbnail(url=icon)
         await interaction.response.send_message(embed=embed)

    @group.command(name="channelinfo", description="Shows detailed info on a server channel.")
    async def channelinfo(self, interaction, channel: discord.Option(discord.TextChannel, description="Channel to get info of")):
        embed = cogs.combinebot.makeEmbed(
            title="Info on #{0}".format(channel), 
            description="""
**Category:** {0}
**Created at:** {1}
**Guild:** {2}
**ID:** {3}
**NSFW?** {4}
**Slowmode:** {5}
**Type:** {6}
            """.format(channel.category, channel.created_at, channel.guild, channel.id, channel.nsfw, channel.slowmode_delay, channel.type),
            color=discord.Colour.red(),
            )
        await interaction.response.send_message(embed=embed)

    @group.command(name="serverinfo", description="Provides detailed information on the given server.")
    async def serverinfo(self, interaction, server: discord.Option(discord.Guild, description="Name of the server to get info on. Case sensitive!")):
        embed = cogs.combinebot.makeEmbed(
            title="Info on {0}".format(server),
            description="""
**Members:** {0}
**Owner:** {1} 
**ID:** {2} 
**Created at:** {3}
**Description:** {4} 
            """.format(server.member_count, server.owner, server.id, server.created_at, server.description),
            color=discord.Colour.og_blurple()
        )
        embed.set_thumbnail(url=server.icon)

        await interaction.response.send_message(embed=embed)

    @group.command(name="button", description="Make a embed link button!")
    async def button(self, interaction, link: discord.Option(str, description="Link for the button. Must begin with http(s)://"), label: discord.Option(str, description="Label for button")):
         class ButtonView(discord.ui.View):
           def __init__(self):
              super().__init__(timeout=None)

              supportServerButton = discord.ui.Button(label=label, style=discord.ButtonStyle.gray, url=link)
              self.add_item(supportServerButton)

         await interaction.response.send_message(view=ButtonView())

    @group.command(name="uuid", description="Generate a Version 4 UUID")
    async def uuid(self, interaction, amount: discord.Option(int, description="How many UUIDs to create (max 50)", required=False, default=1)):
         if amount > 50:
              await interaction.response.send_message(":x: Too many requests! Must be less than 50.")
              return
         uuids = ""
         for uuidamount in range(amount):
              uuids = uuids + "`{}`\n".format(uuid.uuid4())

         await interaction.response.send_message(str(uuids))


    @group.command(name="randomstring", description="Generate a random string of a custom length")
    async def randomstring(self, interaction, length: discord.Option(int, description="Length of the string. Maximum is 100! Defaults to 12.", required=False, default=12)):
         r = cogs.combinebot.getRandomString(length=length)
         await interaction.response.send_message(r)

    @group.command(name="unixtime", description="Get the current UNIX timestamp!")
    async def unixtime(self, interaction):
         await interaction.response.send_message("`{}`".format(str(time.time())))

    @group.command(name="roleid", description="Get the ID of a role!")
    async def roleid(self, interaction, 
                     role: discord.Option(discord.Role, description="Role to get ID of")):
        await interaction.response.send_message("The role **{0}** has an ID of **{1}**".format(role.name, str(role.id)))

    @group.command(name="welcomescreen", description="Get the welcome screen of the server you're in!")
    async def welcomescreen(self, interaction):
        guild = interaction.guild
        if "COMMUNITY" not in guild.features:
            await interaction.response.send_message(":x: This server does not have a welcome screen.")
            return
        else:
            welcomesc = await guild.welcome_screen()
            await interaction.response.send_message(welcomesc)
    
         
      
def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Utilitycog(bot)) # add the cog to the bot
