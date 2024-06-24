import discord
from discord.ext import commands
import os
from discord import default_permissions
from discord import permissions
from discord import Permissions
from discord import PermissionOverwrite
import requests
import json
import random
import cogs.requestHandler as handler
from random import uniform
import feedparser
import pointercratepy
from pointercratepy import Client
import cogs.combinebot
from cogs.combinebot import name
from cogs.combinebot import game
from cogs.combinebot import icon
from cogs.combinebot import VERSION
from cogs.combinebot import LATESTADDITION
from cogs.lists import category
from cogs.lists import difficulty

client = Client()




class Apis(commands.Cog):
    group = discord.SlashCommandGroup(name="api", description="Commands that use online APIs made by other people")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @group.command(name="dadjoke", description="Get a random dad joke!")
    async def dadjoke(self, ctx):
        await ctx.respond(cogs.combinebot.getJoke())
    
    @group.command(name="xkcd", description="Get a random XKCD comic!")
    async def xkcd(self, ctx, number: discord.Option(int, description="Number of XKCD comic to get. By default this is just random.", default=random.randint(1, 2940), required=False)):
        xkcdjson = cogs.combinebot.getXKCD(number=number)
            
        embed = cogs.combinebot.makeEmbed(
            
            
            title="#" + str(xkcdjson["num"]) + " - " + xkcdjson["title"],
            description=xkcdjson["alt"],
            color=discord.Colour.blurple(),
            
            
        )
        embed.set_image(url=xkcdjson["img"])
        embed.set_footer(text="{0}/{1}/{2}".format(xkcdjson["month"], xkcdjson["day"], xkcdjson["year"]))
        await ctx.respond(embed=embed)

    @group.command(name="xkcdrecent", description="Get the most recent XKCD comic!")
    async def xkcdrecent(self, ctx):
        xkcdjson = cogs.combinebot.getXKCDRecent()
            
        embed = cogs.combinebot.makeEmbed(
            
            
            title="#" + str(xkcdjson["num"]) + " - " + xkcdjson["title"],
            description=xkcdjson["alt"],
            color=discord.Colour.blurple(),
            
            
        )
        embed.set_image(url=xkcdjson["img"])
        embed.set_footer(text="{0}/{1}/{2}".format(xkcdjson["month"], xkcdjson["day"], xkcdjson["year"]))
        await ctx.respond(embed=embed)
    
    @group.command(name="dogpics", description="Random picture of a dog!")
    async def dogpics(self, ctx):
        dogjson = cogs.combinebot.getDogPic()

        embed = cogs.combinebot.makeEmbed(
            title="Dog",
            color=discord.Colour.blurple(),
        )
        embed.set_image(url=dogjson["message"])
        await ctx.respond(embed=embed)
    
    @group.command(name="shakespeare", description="Translate english text to Shakespeare english!")
    async def shakespeare(self, ctx, text: discord.Option(str, description="Text to translate", required=True)):
         jshake = cogs.combinebot.getShakespeare(text=text)

         embed = cogs.combinebot.makeEmbed(
              title = jshake["contents"]["translated"],
              description = jshake["contents"]["text"],
              color = discord.Colour.orange(),
         )
         embed.set_thumbnail(url="https://hips.hearstapps.com/hmg-prod/images/william-shakespeare-194895-1-402.jpg")
         await ctx.respond(embed=embed)


    @group.command(name="jojostand", description="Get a random jojo stand and its info!")
    async def jojostand(self, ctx):
         ctx.defer()
         jstand = cogs.combinebot.getStand()

         embed = cogs.combinebot.makeEmbed(
              title=jstand["name"],
              description="""
              **Alternate name:** {0}
              **Japanese name:** {1}
              **Chapter:** {2}
              **Abilities:** {3}
              **Battle Cry:** {4}

               """.format(jstand["alternateName"], jstand["japaneseName"], jstand["chapter"], jstand["abilities"], jstand["battlecry"]),
               color=discord.Colour.blurple()
         )
         embed.set_image(url="https://jojos-bizarre-api.netlify.app/assets/{0}".format(jstand["image"]))

         await ctx.respond(embed=embed)


    @group.command(name="jojocharacter", description="Get a random jojo character and their info!")
    async def jojocharacter(self, ctx):
         ctx.defer()
         jchar = cogs.combinebot.getJoe()

         embed = cogs.combinebot.makeEmbed(
              title=jchar["name"],
              description="""
              **Japanese name:** {0}
              **Abilities:** {1}
              **Nationality:** {2}
              **Catchphrase:** {3}
              **Family:** {4}
              **Chapter:** {5}
              **Still alive?** ||{6}||
              **Is human?** {7}

               """.format(jchar["japaneseName"], 
                          jchar["abilities"], 
                          jchar["nationality"], 
                          jchar["catchphrase"], 
                          jchar["family"], 
                          jchar["chapter"], 
                          ("yes" if jchar["living"] else "no"),
                          jchar["isHuman"]),
               color=discord.Colour.blurple(),
         )
         embed.set_image(url="https://jojos-bizarre-api.netlify.app/assets/{0}".format(jchar["image"]))
         await ctx.respond(embed=embed)
         
    @group.command(name="meme", description="Get a random meme from Reddit!")
    async def meme(self, ctx):
         jmeme = cogs.combinebot.getMeme()
         
         embed = cogs.combinebot.makeEmbed(
              title = jmeme["title"],
              description = "Upvote score: {0}".format(jmeme["ups"]),
              color = discord.Colour.blurple(),
         )
         embed.set_image(url=jmeme["url"])
         embed.set_footer(text="Posted in r/{0} by u/{1}".format(jmeme["subreddit"], jmeme["author"]))

         await ctx.respond(embed=embed)

    @group.command(name="randombreed", description="Get a random dog breed!")
    async def randombreeed(self, ctx):
               randbreed = cogs.combinebot.getRandBreed()
               
               await ctx.respond(f":dog: `{randbreed}`")

    @group.command(name="urlshort", description="Shortens a given URL")
    async def urlshort(self, ctx, url: discord.Option(str, description="URL to shorten. Must begin with http(s)://www.")):
           await ctx.defer()
           
           await ctx.respond("Your Shortened URL: https://1pt.co/{0}".format(cogs.combinebot.shortenURL(url=url)))

    @group.command(name="weather", description="Get the weather for a city!")
    async def weather(self, ctx, city: discord.Option(str, description="The city to get weather of")):
        response = cogs.combinebot.getWeather(city=city)
        if response == ":x: City not found! Maybe you misspelt it?":
              ctx.respond(response)
              return
        embed = cogs.combinebot.makeEmbed(
               title = "Weather in {0}".format(city.upper()),
        )
        embed.add_field(name="Today", value="Temperature is {0}, wind is up to {1} and it's {2}.".format(response["temperature"], response["wind"], response["description"]))

        for day in response["forecast"]:
               embed.add_field(name="Day {}".format(day["day"]), value="Temperture is {0} and wind is up to {1}.".format(day["temperature"], day["wind"]))

        await ctx.respond(embed=embed)
           

    @group.command(name="httpanimal", description="Get an animal image for an HTTP status code!")
    async def httpdog(self, ctx, animal: discord.Option(str, description="The animal to get the HTTP image of.", choices=["Dog", "Cat"]), 
                                 status: discord.Option(str, description="The HTTP status code to get image of.")):
           rurl = requests.get("https://http.{0}/{1}.jpg".format(animal.lower(), status))
           if rurl.status_code == 404:
                  await ctx.respond(":x: {} not found! That status code does not exist.".format(animal))
                  return
           
    
           embed = cogs.combinebot.makeEmbed(
                  title="{0} {1}".format(animal, status),
                  color=discord.Colour.blurple(),
           )
           embed.set_image(url="https://http.{0}/{1}.jpg".format(animal.lower(), status))
           await ctx.respond(embed=embed)

    @group.command(name="pokedex", description="Get info on a pokemon!")
    async def pokedex(self, ctx, pokemon: discord.Option(str, description="Pokemon to get data of")):
           response = cogs.combinebot.getPoke(pokemon=pokemon)
           if response == ":x: Pokemon not found! Maybe you misspelled it?":
                 ctx.respond(response)
                 return

           abilities = ""

           for ability in response["abilities"]:
                  abilities = abilities + "{}, ".format(ability["ability"]["name"])

           embed = cogs.combinebot.makeEmbed(
                  title="Info on {0}".format(pokemon),
                  description="""
                  **Abilities:** {0}
**Base XP:** {1}
**Order:** {2}
**Weight:** {3}
**Height:** {4}




                 """.format(abilities, response["base_experience"], response["order"], response["weight"], response["height"]),
           )
           embed.set_thumbnail(url=response["sprites"]["front_default"])
           await ctx.respond(embed=embed)

    @group.command(name="dictionary", description="Get the definition of an english word!")
    async def dictionary(self, ctx, word: discord.Option(str, description="Word to get definition of")):
           await ctx.defer()
           request = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word))
           if request.status_code == 404:
                 ctx.respond(":x: Word \"**{}**\" not found! Perhaps you misspelled it?".format(word))
                 return
                  
           response = json.loads(request.text)
           response = response[0]
                  
           
           description = ""
           for definitions in response["meanings"]:
                  description = description + "_{0} usage:_ {1}\n".format(
                         definitions["partOfSpeech"],
                         definitions["definitions"][0]["definition"]
                  )

           embed = discord.Embed(
                  title = "Definition of {0}".format(word),
                  description=description,
                  color=discord.Colour.blurple(),
           )
           embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
           await ctx.respond(embed=embed)

    @group.command(name="fakeperson", description="Generates a fake person and their info")
    async def fakeperson(self, ctx):
           response = cogs.combinebot.getPerson()
           response = response["results"][0]
           embed = cogs.combinebot.makeEmbed(
                  title="{0}. {1} {2}, {3}".format(response["name"]["title"], response["name"]["first"], response["name"]["last"], response["gender"])
           )
           embed.set_image(url=response["picture"]["large"])
           embed.add_field(name="Street", value="{0} {1}".format(response["location"]["street"]["number"], response["location"]["street"]["name"]))
           embed.add_field(name="Location", value="{0}, {1}, {2}".format(response["location"]["city"], response["location"]["state"], response["location"]["country"]))
           embed.add_field(name="Email", value=response["email"])
           embed.add_field(name="Age", value="Born on {0}, age {1}".format(response["dob"]["date"], response["dob"]["age"]))
           embed.add_field(name="Phone Number", value=response["phone"])
           await ctx.respond(embed=embed)
    
    @group.command(name="bible", description="Get a verse from the Bible!")
    async def bible(self, ctx, book: discord.Option(str, description="Name of book to get verse from."), chapter: discord.Option(str, description="Chapter to get verse from"), verse: discord.Option(str, description="Verse to get text from")):
           response = cogs.combinebot.getBible(book=book, chapter=chapter, verse=verse)
           if response == ":x: Book/Chapter/Verse not found!":
                 await ctx.respond(response)
                 return
           response = response["verses"][0]
           embed = cogs.combinebot.makeEmbed(
                  title="{0} {1}:{2}".format(response["book_name"], response["chapter"], response["verse"]),
                  description="_{}_".format(response["text"]),
                  color=discord.Colour.blurple(),
           )
           await ctx.respond(embed=embed)

    @group.command(name="rss", description="Get the RSS feed from a website!")
    async def rss(self, ctx, link: discord.Option(str, description="Link to the RSS feed")):
           await ctx.defer()
           d = feedparser.parse(link)
           
           embed = cogs.combinebot.makeEmbed(
                  title=d.feed.title,
                  description=d.feed.description,
                  color=discord.Colour.blurple(),

           )
           for names in d.entries:
                  embed.add_field(name=names.title, value="[Link to post]({})".format(names.link))
           await ctx.respond(embed=embed)


    @group.command(name="demonlist", description="Get info on a demon from the Pointercrate Geometry Dash demon list!")
    async def demonlist(self, ctx, demonname: discord.Option(str, description="Name of the demon to get info on. CASE SENSITIVE!")):
           await ctx.defer()
           demons = client.get_demons(name=demonname)
           
           demons = demons[0]

           verifier = client.get_demons(name=demonname)
           verifier = verifier[0].get("verifier")

           publisher = client.get_demons(name=demonname)
           publisher = publisher[0].get("verifier")
           
           view = discord.ui.View()

           videobutton = discord.ui.Button(label="Verification Video", style=discord.ButtonStyle.gray, url=demons.get("video"))

           view.add_item(videobutton)


           embed = cogs.combinebot.makeEmbed(
                  title="#{0} - {1}".format(str(demons.get("position")), str(demons.get("name"))),
                  description="Verified by {0}, published by {1}".format(verifier["name"], publisher["name"]),
                  color=discord.Colour.red(),
           )
           embed.set_thumbnail(url="https://i.postimg.cc/wM77Spkt/Extreme-Demon.webp")
           await ctx.respond(embed=embed, view=view)

    @group.command(name="trivia", description="Get a random trivia")
    async def trivia(self, ctx, 
                     triviacategory: discord.Option(str, description="Category for trivia questions", choices=category),
                     triviadifficulty: discord.Option(str, description="The difficulty of the questions", choices=difficulty)):
          await ctx.defer()
          
          response = cogs.combinebot.getTrivia(category=triviacategory, difficulty=triviadifficulty)
          response = response["results"][0]
          titlequestion = cogs.combinebot.remove_html_entities(text=response["question"])
          questions = [
                      response["correct_answer"],
                      response["incorrect_answers"][0],
                      response["incorrect_answers"][1],
                      response["incorrect_answers"][2]
                ]
          random.shuffle(questions)
          label1 = questions[0]
          label2 = questions[1]
          label3 = questions[2]
          label4 = questions[3]
          print(label1, label2, label3, label4)
          class QuestionView(discord.ui.View):
            def __init__(self):
                super().__init__()

            @discord.ui.button(label=label1, style=discord.ButtonStyle.gray)
            async def _question1(self, button, ctx):
                self.disable_all_items()
                await ctx.response.edit_message(view=self)
                if label1 == response["incorrect_answers"][0] or response["incorrect_answers"][1] or response["incorrect_answers"][2]:
                      await ctx.respond("Correct answer was **{}**.".format(response["correct_answer"]))
                elif label4 == response["correct_answer"]:
                      await ctx.respond(":white_check_mark: Correct answer!")
            
            @discord.ui.button(label=label2, style=discord.ButtonStyle.gray)
            async def _question2(self, button, ctx):
                self.disable_all_items()
                await ctx.response.edit_message(view=self)
                if label2 == response["incorrect_answers"][0] or response["incorrect_answers"][1] or response["incorrect_answers"][2]:
                      await ctx.respond("Correct answer was **{}**.".format(response["correct_answer"]))
                elif label4 == response["correct_answer"]:
                      await ctx.respond(":white_check_mark: Correct answer!")
            
            @discord.ui.button(label=label3, style=discord.ButtonStyle.gray)
            async def _question3(self, button, ctx):
                self.disable_all_items()
                await ctx.response.edit_message(view=self)
                if label3 == response["incorrect_answers"][0] or response["incorrect_answers"][1] or response["incorrect_answers"][2]:
                      await ctx.respond("Correct answer was **{}**.".format(response["correct_answer"]))
                elif label4 == response["correct_answer"]:
                      await ctx.respond(":white_check_mark: Correct answer!")

            @discord.ui.button(label=label4, style=discord.ButtonStyle.gray)
            async def _question4(self, button, ctx):
                self.disable_all_items()
                await ctx.response.edit_message(view=self)
                if label4 == response["incorrect_answers"][0] or response["incorrect_answers"][1] or response["incorrect_answers"][2]:
                      await ctx.respond("Correct answer was **{}**.".format(response["correct_answer"]))
                elif label4 == response["correct_answer"]:
                      await ctx.respond(":white_check_mark: Correct answer!")



          embed = cogs.combinebot.makeEmbed(title=titlequestion, description="Choose your answer.", color=discord.Color.blurple(),)
          await ctx.respond(embed=embed, view=QuestionView())
                
           

           
                  

           

    

           

   
           
        
    
         
         
         
        

        








def setup(bot): # this is called by Pycord to setup the co
    bot.add_cog(Apis(bot)) # add the cog to the bot


