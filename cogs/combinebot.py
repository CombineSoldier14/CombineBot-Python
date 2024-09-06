import discord
from discord.ext import commands
import os
from discord import reaction
from discord import Reaction
import json
import datetime
import uuid
import random
import string
import cogs.combinebot
import cogs.lists
from cogs.lists import aaquotes
from cogs.lists import suntzuquotes
from cogs.lists import ytvalues
from cogs.lists import difficulty
from cogs.lists import rpswins
import requests
import time
import json
import uuid
import string
from requests.utils import requote_uri
import random
import time
import cogs.requestHandler as handler
import re
from cogs.lists import statuses
import asyncio
from dotenv import load_dotenv
import dotenv
import mysql.connector

dotenv.load_dotenv()

use_db = os.getenv("USE_DB")
VERSION = os.getenv("VERSION")
ERROR_WEBHOOK = os.getenv("ERROR_WEBHOOK")
FEEDBACK_WEBHOOK = os.getenv("FEEDBACK_WEBHOOK")
LATESTADDITION = os.getenv("LATEST_ADDITION")
dev_status = os.getenv("DEVMODE")
#The Dev status is meant for if CombineBot is running in DEV mode which changes some names and icons.


if dev_status == 1:
            name = "CombineBot Development Edition"
            game = "with unstable ass commands"
            icon = "https://cdn.discordapp.com/app-icons/1227477531461025854/85f59950e14cca56e4b1bcefd911ca23.png?size=256"
            prefix = "-"


else:
            name = "CombineBot"
            game = "https://combinebot.blogspot.com/"
            icon = "https://i.postimg.cc/wjgpb7bb/image-1.png"
            prefix = ";"

def getBotInfo():
        info = [
                {
                        "name":name,
                        "icon":icon,
                        "prefix":prefix,
                        "version":VERSION,
                        "dev_status":dev_status,
                        "latest_addition":LATESTADDITION,
                        "ROTATING_STATUS_INTERVAL":15
                }
        ]
        return info

def makeEmbed(**kwargs):
        embed = discord.Embed(**kwargs)
        embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon) 
        return embed

class mysqlcnx():
    def __init__(self, cnx: mysql.connector.connection.MySQLConnection, canUseDatabase: bool = False):
        super().__init__()
        self.cnx = cnx
        self.canUseDatabase = canUseDatabase
        if canUseDatabase:
            self.cursor = cnx.cursor()
        else:
            self.cursor = None

def getRandomString(length):
        if length > 100:
              return ":x: Specified length is too high!"
              
         
        chars = []

        for c in string.ascii_lowercase:
              chars.append(c)

        for c in string.ascii_uppercase:
              chars.append(c)

        for c in range(10): # 1-9
              chars.append(str(c))
              
        randstring = ""

        for s in range(length):
              randstring = randstring + random.choice(chars)

        return "`{}`".format(str(randstring))


def getSunTzu():
        quotes = suntzuquotes
        return random.choice(quotes)


def getAceAttorneyQuote():
        quotes = aaquotes
        return random.choice(quotes)

def getYTvideo():
        videoid = ""
        for _ in range(11): # video id is 11 chars long
            videoid = videoid + random.choice(ytvalues)
         
        return "https://www.youtube.com/watch?v={}".format(videoid)

def getDNDmod(mod):
        d = handler.get("https://www.dnd5eapi.co/api/ability-scores/{}".format(mod.lower()))
        j = json.loads(d.text)
        return j

def getJoke():
        r = handler.get("https://official-joke-api.appspot.com/random_joke")
        j = json.loads(r.text)
        return "{0} {1}".format(j["setup"], j["punchline"])

def getXKCDRecent():
        xkcdlink = handler.get("https://xkcd.com/info.0.json")
        xkcdjson = json.loads(xkcdlink.text)
        return xkcdjson

def getXKCD(number=random.randint(1, 2949)):
        r = handler.get("https://xkcd.com/{}/info.0.json".format(str(number)))
        if requests.status_codes == 404:
                return ":x: Comic number not found"
        else:
          j = json.loads(r.text)
          return j


        
def getDogPic():
        doglink = handler.get("https://dog.ceo/api/breeds/image/random")
        dogjson = json.loads(doglink.text)
        return dogjson

def getShakespeare(text):
        rshake = handler.get("https://api.funtranslations.com/translate/shakespeare.json?text={0}".format(text))
        jshake = json.loads(rshake.text)
        return jshake

def getStand():
        id = random.randint(1, 155)
        rstand = handler.get("https://stand-by-me.herokuapp.com/api/v1/stands/{0}".format(str(id)))
        jstand = json.loads(rstand.text)
        return jstand
def getJoe():
        id = random.randint(1, 155)
        rchar = handler.get("https://stand-by-me.herokuapp.com/api/v1/characters/{}".format(str(id)))
        jchar = json.loads(rchar.text)
        return jchar

def getRandomReddit(subreddit: str):
        rmeme = handler.get("https://meme-api.com/gimme/{}".format(subreddit))
        jmeme = json.loads(rmeme.text)
        return jmeme

def getRandBreed():
        rbreed = handler.get("https://dog.ceo/api/breeds/list/all")
        breeds = list(json.loads(rbreed.text)["message"].keys())
        randbreed = random.choice(breeds)
        return randbreed

def shortenURL(url):
        rurl = requests.post("https://csclub.uwaterloo.ca/~phthakka/1pt-express/addURL", params={"long": url})
        jurl = json.loads(rurl.text)
        return jurl["short"]

def getWeather(city):
        request = handler.get("https://goweather.herokuapp.com/weather/{0}".format(city))
        response = json.loads(request.text)
        if request.status_code == 404:
          return ":x: City not found! Maybe you misspelt it?"
        else:
          return response

def getPoke(pokemon, interaction=discord.Interaction):
        request = handler.get("https://pokeapi.co/api/v2/pokemon/{0}".format(pokemon.lower()))
           
        if request.status_code == 404:
                  return ":x: Pokemon not found! Maybe you misspelled it?"
                  
                  
           
        response = json.loads(request.text)
        return response 

def getPerson():
         request = handler.get("https://randomuser.me/api/")
         response = json.loads(request.text)
         return response    

def getBible(book, chapter, verse):
        request = handler.get("https://bible-api.com/{0}%20{1}:{2}".format(book, chapter, verse))
        if request.status_code == 404:
                  return ":x: Book/Chapter/Verse not found!"
        response = json.loads(request.text)
        return response

async def getUserInfo(bot, user, interaction=discord.Interaction):
        if bot == True:
                info = {
                        "id":user.id,
                        "joineddiscord":user.created_at,
                        "discriminator":user.discriminator,
                        "avatar":user.avatar,
                        "bot":"No"
                }
                 
        if bot == False:
                info = {
                        "id":user.id,
                        "joineddiscord":user.created_at,
                        "avatar":user.avatar,
                        "bot":"No"
                }
        return info

async def getChannelInfo(channel, interaction=discord.Interaction):
        info = {
                "category":channel.category,
                "createdat":channel.created_at,
                "guild":channel.guild,
                "id":channel.id,
                "nsfw":channel.nsfw,
                "slowmode":channel.slowmode_delay,
                "type":channel.type
        }
        return info

async def getServerInfo(server, interaction=discord.Interaction):
        info = {
                "members":server.member_count,
                "owner":server.owner,
                "id": server.id,
                "createdat":server.created_at,
                "description":server.description,
                "icon":server.icon

        }
        return info

def getTrivia(category=str, difficulty=str):
        if category == "Any Category":
                categoryint = "0"
        if category == "General Knowledge":
                categoryint = "9"
        if category == "Entertainment: Books":
                categoryint = "10"
        if category == "Entertainment: Film":
                categoryint = "11"
        if category == "Entertainment: Music":
                categoryint = "12"  
        if category == "Entertainment: Musicals & Theatres":
                categoryint = "13"
        if category == "Entertainment: Television":
                categoryint = "14"
        if category == "Entertainment: Video Games":
                categoryint = "15"
        if category == "Entertainment: Board Games":
                categoryint = "16"
        if category == "Science & Nature":
                categoryint = "17"
        if category == "Science: Computers":
                categoryint = "18"
        if category == "Science: Mathematics":
                categoryint = "19"
        if category == "Mythology":
                categoryint = "20"
        if category == "Sports":
                categoryint = "21"
        if category == "Geography":
                categoryint = "22"
        if category == "History":
                categoryint = "23"
        if category == "Politics":
                categoryint = "24"
        if category == "Art":
                categoryint = "25"
        if category == "celebrities":
                categoryint = "26"
        if category == "Animals":
                categoryint = "27"
        if category == "Vehicles":
                categoryint = "28"
        if category == "Entertainment: Comics":
                categoryint = "29"
        if category == "Science: Gadgets":
                categoryint = "30"
        if category == "Entertainment: Japanese Anime & Manga":
                categoryint = "31"
        if category == "Entertainment: Cartoon & Animations":
                categoryint = "32"
        url = "https://opentdb.com/api.php?amount=4&category={0}&difficulty={1}&type=multiple".format(categoryint, difficulty)
       
        r = handler.get(url)
        j = json.loads(r.text)
        return j

def remove_html_entities(text):
    # Define regex pattern for HTML entities (decimal and hexadecimal)
    entity_pattern = re.compile(r'&#[0-9]+;|&#[xX][0-9a-fA-F]+;')
    # Replace HTML entities with an empty string
    cleaned_text = re.sub(entity_pattern, '', text)
    return cleaned_text

async def changeStatus(bot):
        botinfo = getBotInfo()
        for status in statuses:
         print("lol")
        
         activity = discord.ActivityType.unknown
         if status["type"] == "PLAYING":
            activity = discord.ActivityType.playing
         elif status["type"] == "LISTENING":
            activity = discord.ActivityType.listening
         elif status["type"] == "WATCHING":
            activity = discord.ActivityType.watching

         real_activity = discord.Activity(type=activity, name=status['status'])
         await bot.change_presence(activity=real_activity)
         await asyncio.sleep(30)

def getCatText(text: str, font_size: int, font_color: str):
        r = "https://cataas.com/cat/says/{0}?fontSize={1}&fontColor={2}".format(text, str(font_size), font_color)
        return requote_uri(r)

def getUrban(term):
        r = handler.get(requote_uri("https://unofficialurbandictionaryapi.com/api/search?term={}&strict=false&matchCase=false&limit=1&page=1&multiPage=false&".format(term)))
        j = json.loads(r.text)
        return j

def getQRCode(url):
        return "https://www.qrtag.net/api/qr_1024.png?url={}".format(url)

def rpswin(userchoice, botchoice):
        for x in rpswins:
                if userchoice == x["userchoice"] and botchoice == x["botchoice"]:
                        return x["final"]
