from __future__ import print_function
import discord
import os # default module
from discord.ext import commands
from discord.ext import tasks
import json
import logging
import cowsay
from discord import Option
from discord import User
from discord import Interaction
from discord import InteractionResponse
from discord import MessageInteraction
from discord import interactions
from discord import InteractionMessage
import nltk
import random
import traceback
import cogs.combinebot
import requests
import mysql.connector
from datetime import date, datetime, timedelta
from cogs.lists import levels
from dotenv import load_dotenv
import dotenv
from cogs.combinebot import mysqlcnx

dotenv.load_dotenv()

use_db = os.getenv("USE_DB")
VERSION = os.getenv("VERSION")
ERROR_WEBHOOK = os.getenv("ERROR_WEBHOOK")
FEEDBACK_WEBHOOK = os.getenv("FEEDBACK_WEBHOOK")
LATESTADDITION = os.getenv("LATEST_ADDITION")
use_webhooks = os.getenv("USE_WEBHOOKS")
SQLHOST = os.getenv("SQLHOST")
SQLUSERNAME = os.getenv("SQLUSERNAME")
SQLDB = os.getenv("SQLDB")
SQLPW = os.getenv("SQLPASSWORD")
dev_status = os.getenv("DEVMODE")




if use_db != 0:
    creds = mysql.connector.connect(user=SQLUSERNAME, password=SQLPW, host=SQLHOST, database=SQLDB)
    m = mysqlcnx(cnx=creds, canUseDatabase=use_db)
    cnx = m.cnx
    cursor = m.cursor

#The Dev status is meant for if CombineBot is running in DEV mode which changes some names and icons.

# alphagamedeveloper: you should really just use a real boolean here... this is a mess
# combinesoldier14: You're literally the one that added this -_-
if dev_status in (1, True, "1", "True", "true", "TRUE"):
            name = "CombineBot Development Edition"
            game = "with unstable ass commands"
            prefix = "-"
            icon = ""
            link = "https://discord.com/oauth2/authorize?client_id=1227477531461025854"


else:
            name = "CombineBot"
            game = "https://combinesolder14.site/combinebot"
            prefix = ";"
            icon = "https://i.postimg.cc/65c12W1c/d89047f0124e9aa9e86ed3971af5e7ce.png"
            link = "https://discord.com/oauth2/authorize?client_id=1225220764861730867"



nltk.download('words')


FRENCH = 420052952686919690




# Defing bot and bot user intents
intents = discord.Intents.default()
bot = commands.Bot(command_prefix=prefix, intents=intents)

logging.basicConfig(level=logging.INFO)
#loading cogs
bot.load_extension('cogs.moderation')
bot.load_extension('cogs.fun')
bot.load_extension('cogs.apis')
bot.load_extension('cogs.mbti')
bot.load_extension('cogs.calculator')
bot.load_extension('cogs.rps')
bot.load_extension('cogs.utilitycog')
bot.load_extension('cogs.role')
bot.load_extension('cogs.mcstatus')
bot.load_extension('cogs.suntzu')
bot.load_extension('cogs.cogfunc')
bot.load_extension('cogs.dnd')
bot.load_extension('cogs.cogfunctest')
bot.load_extension('cogs.enneagramtest')
bot.load_extension('cogs.mbtitest')
bot.load_extension('cogs.standbattle')

@tasks.loop(seconds=30)
async def rotateStatus():
    if use_db != 0:
       cnx.ping(reconnect=True)
    print("rotateStatus has been started.")
    await cogs.combinebot.changeStatus(bot)

@bot.listen("on_message")
async def on_message(message: discord.Message):
      if use_db != 0:
           cursor.execute("SELECT leveling_enabled FROM guild_settings WHERE guild_id = %s", [message.guild.id])
           levelingenable = cursor.fetchone()
           if levelingenable == 0:
                return
           cursor.execute("SELECT COUNT(*) FROM levels WHERE id = %s", [message.author.id])
           r = cursor.fetchone()
           print(r)
           if r == None or r == 0 or r == []:
                cursor.execute("INSERT INTO levels (id) values (%s)", [message.author.id])
                cnx.commit()
           
           cursor.execute("UPDATE levels SET messages_sent = messages_sent + 1 WHERE id = %s;", [message.author.id])
           cnx.commit()
           cursor.execute("SELECT messages_sent FROM levels WHERE id = %s", [message.author.id])
           n = cursor.fetchone()
           for x in reversed(levels):
                if n[0] == x["commands_required"]:
                    cursor.execute("UPDATE levels SET level = level + 1 WHERE id = %s;", [message.author.id])
                    cnx.commit()
                    cursor.execute("SELECT level FROM levels WHERE id = %s", [message.author.id])
                    newlevel = cursor.fetchone()
                    cnx.commit()
                    await message.channel.send("<@{0}> you have leveled up to {1}!".format(message.author.id, newlevel[0])) 
      else:
            return

@bot.listen("on_application_command")
async def on_application_command(ctx: discord.context.ApplicationContext):
     if use_db != 0:
           cursor.execute("SELECT leveling_enabled FROM guild_settings WHERE guild_id = %s", [ctx.guild.id])
           levelingenable = cursor.fetchone()
           if levelingenable == 0:
                return
           cursor.execute("SELECT COUNT(*) FROM levels WHERE id = %s", [ctx.author.id])
           r = cursor.fetchone()
           if r == None or 0 or []:
                cursor.execute("INSERT INTO levels (id) values (%s)", [ctx.author.id])
           cursor.execute("UPDATE levels SET commands_ran = commands_ran + 1 WHERE id = %s;", [ctx.author.id])
           cursor.execute("SELECT commands_ran FROM levels WHERE id = %s", [ctx.author.id])
           n = cursor.fetchone()
           for x in reversed(levels):
                if n[0] == x["commands_required"]:
                          cursor.execute("UPDATE levels SET level = level + 1 WHERE id = %s;", [ctx.author.id])
                          cursor.execute("SELECT level FROM levels WHERE id = %s", [ctx.author.id])
                          newlevel = cursor.fetchone()
                          cnx.commit()
                          await ctx.channel.send("<@{0}> you have leveled up to {1}!".format(ctx.author.id, newlevel[0])) 
     else:
            return
  
     
     

@bot.event
async def on_ready():
    bot.auto_sync_commands = True
    BOT_TASKS = [rotateStatus]
    for task in BOT_TASKS:
        if not task.is_running():
            task.start()
    logging.info("Bot is ready!")
    

class ProblemView(discord.ui.View):
   def __init__(self, traceback, bot):
     super().__init__(timeout=None)
     self._error = traceback
     self.bot = bot

     supportServerButton = discord.ui.Button(label="Report GitHub issue", style=discord.ButtonStyle.gray, url="https://github.com/CombineSoldier14/CombineBot/issues/new")
     self.add_item(supportServerButton)

   @discord.ui.button(label="Report Error to CombineSoldier14", style=discord.ButtonStyle.primary)
   async def errorbutton(self, Button: discord.ui.Button, interaction: discord.Interaction):
        if use_webhooks != 0 or True:
           Button.disabled = True
           Button.label = "Error Reported!"
           await interaction.response.edit_message(view=self)
           webhook = ERROR_WEBHOOK
           requests.post(webhook, {
               "content": "<@951639877768863754> {}".format("# Error Occurred!:\n`{0}`\nError: `{1}`".format(''.join(traceback.format_tb(self._error.__traceback__)), repr(self._error)))
           })
        else:
              await interaction.response.send_message(":x: Webhook usage is currently disabled.")
              return



@bot.event
async def on_application_command_error(interaction: discord.Interaction,
                                        error: discord.DiscordException):
    embed = discord.Embed(
        title = "Whoops!",
        description = "An error has occured.  Retrying the command might help, or this can be an internal server error",
        color = discord.Colour.red()
    )
    embed.add_field(name="Error Message", value="`{0}`".format(repr(error)))

    embed.set_thumbnail(url="https://i.imgur.com/KR3aiwB.png")
    try:
        await interaction.response.send_message(embed=embed, view=ProblemView(traceback=error, bot=bot))
    except:
        await interaction.followup.send(embed=embed, view=ProblemView(traceback=error, bot=bot))
    raise error

#CombineBot website button for /about
class AboutLinkBloggerView(discord.ui.View):
    def __init__(self, bot) -> None:
     super().__init__()
     self.bot = bot
     
     button1 = discord.ui.Button(label='Learn More!', style=discord.ButtonStyle.gray, url='https://combinebot.blogspot.com/')
     self.add_item(button1)

     button2 = discord.ui.Button(label='GitHub', style=discord.ButtonStyle.gray, url='https://github.com/CombineSoldier14/CombineBot')
     self.add_item(button2)

     button3 = discord.ui.Button(label='Add {0}!'.format(name), style=discord.ButtonStyle.gray, url=link)
     self.add_item(button3)


     
    @discord.ui.button(label="Send Feedback!", style=discord.ButtonStyle.primary)
    async def feedback(self, button: discord.ui.Button, interaction: discord.Interaction):
         await interaction.response.send_modal(FeedbackModal(title="Feedback on CombineBot", bot=self.bot))
         button.disabled = True
         button.label = "Feedback Sent!"
         await interaction.response.edit_message(view=self)
     
     

class FeedbackModal(discord.ui.Modal):
     def __init__(self, bot, *args, **kwargs) -> None:
          super().__init__(*args, **kwargs)
          self.bot = bot
          
          self.add_item(discord.ui.InputText(label="Feedback", style=discord.InputTextStyle.long))

     async def callback(self, interaction: discord.Interaction):
           if use_webhooks != 0 or True:
              await interaction.response.send_message("Your feedback has been submitted to the bot's owner, **CombineSoldier14**!", ephemeral=True)
              webhook = FEEDBACK_WEBHOOK
              requests.post(webhook, {
               "content": "<@951639877768863754> Feedback submitted from {0} (`{1}`): *{2}*".format(interaction.user, interaction.user.id, self.children[0].value)
              })
           else:
              await interaction.response.send_message(":x: Webhook usage is currently disabled.")


    
class InviteView(discord.ui.View):
   def __init__(self):
      super().__init__(timeout=None)

      supportServerButton = discord.ui.Button(label="Invite CombineBot!", style=discord.ButtonStyle.gray, url="https://discord.com/oauth2/authorize?client_id=1225220764861730867")
      self.add_item(supportServerButton)


#This file main.py can be seen as a cog itself. Only basic and SQL commands are here!


@bot.slash_command(name="ping", description="Sends the bot's ping or latency")
async def ping(interaction):
    await interaction.response.send_message("Pong! Latency or ping is {0}".format(round(bot.latency * 100, 2)))

@bot.slash_command(name="helloworld", description="If your program can't say this, don't talk to me")
async def helloworld(interaction):
    await interaction.response.send_message(":earth_americas: Hello world!")


@bot.slash_command(name="checklevel", description="Get your current level!")
async def checklevel(interaction, user: discord.Option(discord.Member, description="User to get level of")): # type: ignore
     if use_db != 0 or True:
       cursor.execute("SELECT COUNT(*) FROM levels WHERE id = %s", [user.id])
       status = cursor.fetchone()[0]
       if status is None or status == 0:
              level = 0
              embed = cogs.combinebot.makeEmbed(
                 title="{}'s Level".format(user.name),
                 description="Their level is **{}**.\nYou can level up by running CombineBot commands, sending messages, and winning stand battles!".format(str(level)),
                 color=discord.Color.blurple()
              )   
              embed.set_thumbnail(url=user.display_avatar)
              await interaction.response.send_message(embed=embed)
              return
       cursor.execute("SELECT level from levels WHERE id = %s", [user.id])
       level = cursor.fetchone()[0]
       embed = cogs.combinebot.makeEmbed(
            title="{}'s Level".format(user.name),
            description="Your level is **{}**.\nYou can level up by running CombineBot commands!".format(str(level)),
            color=discord.Color.blurple()
       )  
       embed.set_thumbnail(url=user.display_avatar)
       await interaction.response.send_message(embed=embed)
     else:
           await interaction.response.send_message(":x: Database usage is currently disabled.")



@bot.slash_command(name="about", description="About the bot")
async def about(interaction):
    response = cogs.combinebot.getBotInfo()
    usercount = 0
    for user in bot.get_all_members():
            usercount += 1
    embed = discord.Embed(
        title= "About {0} v{1}".format(response[0]["name"], response[0]["version"]),
        description= "{0} is a Python based discord bot created by CombineSoldier14 with commands for moderation and fun!\n {1}'s birthday is **4/5/2024.**\n CombineBot is currently serving **{2}** users in **{3}** servers.".format(response[0]["name"], response[0]["name"], str(usercount), len(bot.guilds)),
        color=discord.Colour.yellow(),
    )
    embed.set_thumbnail(url=icon)
    embed.set_footer(text="NOTE: Amount of users may not be perfectly accurate.")
    embed.add_field(name="**Latest Addition**", value=response[0]["latest_addition"])
    embed.add_field(name="**Bot Ping**", value="{0} ms".format(round(bot.latency * 100, 2)))
    await interaction.response.send_message(embed=embed, view=AboutLinkBloggerView(bot=bot))
    
@bot.slash_command(name="toggleleveling", description="A command for server owners to toggle leveling on/off.")
@commands.has_permissions(administrator=True)
async def disableleveling(interaction, leveling: discord.Option(bool, choices=[True, False])): # type: ignore
     if use_db != 0 or True:
         cursor = cnx.cursor()
         if leveling == True:
            cursor.execute("SELECT COUNT(*) FROM guild_settings WHERE guild_id = %s", [interaction.guild.id])
            status = cursor.fetchone()
            if status == 0 or status is None:
                 cursor.execute("INSERT INTO guild_settings (guild_id) values (%s)", [interaction.guild.id])
                 cnx.commit()
                 await interaction.response.send_message("Leveling is already enabled!")
                 return
            else:
                 cursor.execute("UPDATE guild_settings SET leveling_enabled = 1 WHERE guild_id = %s;", [interaction.guild.id])
                 cnx.commit()
                 await interaction.response.send_message(":white_check_mark: Leveling is enabled on this server!")
         if leveling == False:
            cursor.execute("SELECT COUNT(*) FROM guild_settings WHERE guild_id = %s", [interaction.guild.id])
            status = cursor.fetchone()
            if status == 0 or status is None:
                 cursor.execute("INSERT INTO guild_settings (guild_id) values (%s)", [interaction.guild.id])
            cursor.execute("UPDATE guild_settings SET leveling_enabled = 0 WHERE guild_id = %s;", [interaction.guild.id])
            cnx.commit()
            await interaction.response.send_message(":white_check_mark: Leveling is disabled on this server!")
     else:
           await interaction.response.send_message(":x: Database usage is currently disabled.")
          
          
     

@bot.slash_command(name="say", description="Use the bot to say messages!")
async def _say(interaction, message: discord.Option(str, description="Message for the bot to say")): # type: ignore
      await interaction.response.send_message("Message has been sent!", ephemeral=True)
      await interaction.send(message)

@bot.slash_command(name="ephemeral", description="Sends an ephemeral message to yourself!")
async def ephemeral(interaction, text):
    await interaction.response.send_message(text, ephemeral="true")
    

@bot.slash_command(name="invite", description="Get the invite link for CombineBot!")
async def invite(interaction):
   await interaction.response.send_message(view=InviteView())

# AutoRun prevention with __name__
if __name__ == "__main__": # import run prevention
    if os.path.isfile("token.json") == True: # check if token.json exists
        with open("token.json", "r") as f:
            _d = json.load(f)
            loadedJSONToken = _d["BOT_TOKEN"]
        if loadedJSONToken.lower() == "yourtokenhere":
            loadedJSONToken = None
    else:
        loadedJSONToken = None
    environToken = os.getenv("BOT_TOKEN")

    if (loadedJSONToken == None) and (environToken == None):
        raise EnvironmentError("No token specified!  Please enter a token via token.json or by passing an environment variable called 'BOT_TOKEN'.  Stop.")
    BOT_TOKEN = (environToken if environToken != None else loadedJSONToken)    
    bot.run(BOT_TOKEN)
