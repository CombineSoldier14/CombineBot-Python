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


with open("version.json", "r") as f:
            _r = json.load(f)
            VERSION = _r["VERSION"]


with open("dev.json", "r") as f:
            _r = json.load(f)
            dev_status = _r["DEV_STATUS"]

with open("latestaddition.json", "r") as f:
            _r = json.load(f)
            LATESTADDITION = _r["LATEST_ADDITION"]


#The Dev status is meant for if CombineBot is running in DEV mode which changes some names and icons.


if dev_status == "true":
            name = "CombineBot Development Edition"
            game = "with unstable ass commands"
            icon = "https://cdn.discordapp.com/app-icons/1227477531461025854/85f59950e14cca56e4b1bcefd911ca23.png?size=256"
            prefix = "-"
            link = "https://discord.com/oauth2/authorize?client_id=1227477531461025854"


if dev_status == "false":
            name = "CombineBot"
            game = "https://combinebot.blogspot.com/"
            icon = "https://i.postimg.cc/wjgpb7bb/image-1.png"
            prefix = ";"
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


@tasks.loop(seconds=30)
async def rotateStatus():
    print("rotateStatus has been started.")
    await cogs.combinebot.changeStatus(bot)


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
        button.disabled = True
        button.label = "Error Reported!"
        await interaction.response.send_message("Your error has been submitted!")
        webhook = "https://discord.com/api/webhooks/1259298998301495379/R6zd6M4D2SQ_l2DfL-3vaEEBNBtU4XuZODbrWHnq0IR0Xj4IZcgvpvS2XrHMpr1YqHXD"
        requests.post(webhook, {
            "content": "{}".format("# Error Occurred!:\n`{0}`\nError: `{1}`".format(''.join(traceback.format_tb(self._error.__traceback__)), repr(self._error)))
        })



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
         print("kjndwdiw")
         await interaction.response.send_modal(FeedbackModal(title="Feedback on CombineBot", bot=self.bot))
     
     

class FeedbackModal(discord.ui.Modal):
     def __init__(self, bot, *args, **kwargs) -> None:
          super().__init__(*args, **kwargs)
          self.bot = bot
          
          self.add_item(discord.ui.InputText(label="Feedback", style=discord.InputTextStyle.long))

     async def callback(self, interaction: discord.Interaction):
           await interaction.response.send_message("Your feedback has been submitted to the bot's owner, **CombineSoldier14**!", ephemeral=True)
           owner = self.bot.get_user(951639877768863754)
           dm = await owner.create_dm()
           await dm.send("Feedback submitted from {0} (`{1}`): *{2}*".format(interaction.user, interaction.user.id, self.children[0].value))


    
class InviteView(discord.ui.View):
   def __init__(self):
      super().__init__(timeout=None)

      supportServerButton = discord.ui.Button(label="Invite CombineBot!", style=discord.ButtonStyle.gray, url="https://discord.com/oauth2/authorize?client_id=1225220764861730867")
      self.add_item(supportServerButton)


#This file main.py can be seen as a cog itself. Only basic commands are here!





@bot.slash_command(name="ping", description="Sends the bot's ping or latency")
async def ping(interaction):
    await interaction.response.send_message("Pong! Latency or ping is {0}".format(round(bot.latency * 100, 2)))

@bot.slash_command(name="helloworld", description="If your program can't say this, don't talk to me")
async def helloworld(interaction):
    await interaction.response.send_message("Hello world!")





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
    
    


@bot.slash_command(name="say", description="Use the bot to say messages!")
async def _say(interaction, message: discord.Option(str, description="Message for the bot to say")):
      await interaction.response.send_message("Message has been sent!", ephemeral=True)
      await interaction.send(message)

@bot.slash_command(name="ephemeral", description="Sends an ephemeral message to yourself!")
async def ephemeral(interaction, text):
    await interaction.response.send_message(text, ephemeral="true")
    
@bot.slash_command(name="spoiler", description="Marks your text as a spoiler!")
async def _spoiler(interaction, text):
    
    await interaction.response.send_message("||" + text + "||")
    

@bot.slash_command(name="invite", description="Get the invite link for CombineBot!")
async def invite(interaction):
   await ctx.send(fuck)
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



































