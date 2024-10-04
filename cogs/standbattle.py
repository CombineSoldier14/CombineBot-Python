import discord
from discord.ext import commands
import os
import cogs.combinebot
import random
from dotenv import load_dotenv
import dotenv
import mysql.connector
from cogs.combinebot import mysqlcnx

dotenv.load_dotenv()

use_db = os.getenv("USE_DB")
SQLHOST = os.getenv("SQLHOST")
SQLUSERNAME = os.getenv("SQLUSERNAME")
SQLDB = os.getenv("SQLDB")
SQLPW = os.getenv("SQLPASSWORD")

if use_db != 0:
    creds = mysql.connector.connect(user=SQLUSERNAME, password=SQLPW, host=SQLHOST, database=SQLDB)
    m = mysqlcnx(cnx=creds, canUseDatabase=use_db)
    cnx = m.cnx
    cursor = m.cursor

async def levelUp(id, cnx):
    cursor.execute("SELECT COUNT(*) FROM levels WHERE id = %s", [id])
    r = cursor.fetchone()
    if r[0] == 0:
        cursor.execute("INSERT INTO levels (id) values (%s)", [id])
    cursor.execute("UPDATE levels SET battles_won = battles_won + 1 WHERE id = %s;", [id])
    cursor.execute("UPDATE levels SET level = level + 1 WHERE id = %s;", [id])
    cursor.execute("SELECT level FROM levels WHERE id = %s", [id])
    newlevel = cursor.fetchone()
    cnx.commit()
    n = ("<@{0}> you have leveled up to {1}!".format(id, newlevel[0]))
    return n

async def finishBattle(winperson, winbot, loseperson, losebot):
    n = "As {0}'s {1} landed the final blow on {2}'s {3}, both {4} and {5} exploded brutally leaving {6} and {7} as our **WINNERS!**".format(
        winperson.name, winbot.name, loseperson.name, losebot.name, losebot.name, loseperson.name, winperson.name, winbot.name
    )

    return n


async def attackEmbed(turnperson, turnbot, unturnperson, unturnbot, turnteamhp, unturnteamhp):
    embed = cogs.combinebot.makeEmbed(
             title="{}'s turn".format(turnperson.name),
             color=discord.Color.red()
         )
    embed.add_field(name="Your Team", value="User: {0}\nBot: {1}\n HP: {2}".format(turnperson.name, turnbot.name, str(turnteamhp)))
    embed.add_field(name="Team 2", value="User: {0}\nBot: {1}\n HP: {2}".format(unturnperson.name, unturnbot.name, str(unturnteamhp)))
    embed.add_field(name="Attacks", value="You can do a small attack which has a 50Percent chance of working, and does 5-10 damage.\nYou can do a large attack which has a 33Percent chance of working, and does 15-25 damage.")
    return embed

class AttackView(discord.ui.View):
    def __init__(self, thread, unturnteamhp, turnteamhp, turnperson, turnbot, unturnperson, unturnbot):
       super().__init__(timeout=None)
       self.thread = thread
       self.turnteamhp = turnteamhp
       self.unturnteamhp = unturnteamhp
       self.turnperson = turnperson
       self.turnbot = turnbot
       self.unturnperson = unturnperson
       self.unturnbot = unturnbot
       self.damagetexts = [
           {
               "misstextsmall":"{0}'s {1} tried to throw a small punch at {2} but missed!".format(self.turnperson.name, self.turnbot.name, self.unturnbot.name),
               "misstextlarge":"{0}'s {1} tried to throw a large blast attack at {2} but missed!".format(self.turnperson.name, self.turnbot.name, self.unturnbot.name),
               "hittextsmall":"{0}'s {1} threw a small punch at {2} and knocked them back a little!".format(self.turnperson.name, self.turnbot.name, self.unturnbot.name),
               "hittextlarge":"{0}'s {1} fired a large blast attack at {2} and blew it and {3} away with major damage!".format(self.turnperson.name, self.turnbot.name, self.unturnbot.name, self.unturnperson.name),
           }
       ]
    @discord.ui.button(label="Small Attack", style=discord.ButtonStyle.green)
    async def smallattack(self, Button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user != self.turnperson:
            await self.thread.send(":x: It's not your turn!")
            return
        self.disable_all_items()
        Button.label = "Small Attack Chosen!"
        await interaction.response.edit_message(view=self)
        f = random.randint(1, 2)
        if f == 2:
            self.unturnteamhp -= random.randint(5, 10)
            if self.unturnteamhp <= 0:
                n = await finishBattle(winperson=self.turnperson, winbot=self.turnbot, loseperson=self.unturnperson, losebot=self.unturnbot)
                await self.thread.send(n)
                r = await levelUp(id=self.turnperson.id, cnx=cnx)
                await self.thread.send(r)
                return
            else:
                await self.thread.send(self.damagetexts[0]["hittextsmall"])
                embed = await attackEmbed(turnperson=self.unturnperson, turnbot=self.unturnbot, unturnperson=self.turnperson, unturnbot=self.turnbot, turnteamhp=self.unturnteamhp, unturnteamhp=self.turnteamhp)
                await interaction.respond(embed=embed, view=AttackView(turnperson=self.unturnperson, turnbot=self.unturnbot, unturnperson=self.turnperson, unturnbot=self.turnbot, turnteamhp=self.unturnteamhp, unturnteamhp=self.turnteamhp, thread=self.thread))
        else:
            await self.thread.send(self.damagetexts[0]["misstextsmall"])
            embed = await attackEmbed(turnperson=self.unturnperson, turnbot=self.unturnbot, unturnperson=self.turnperson, unturnbot=self.turnbot, turnteamhp=self.unturnteamhp, unturnteamhp=self.turnteamhp)
            await interaction.respond(embed=embed, view=AttackView(turnperson=self.unturnperson, turnbot=self.unturnbot, unturnperson=self.turnperson, unturnbot=self.turnbot, turnteamhp=self.unturnteamhp, unturnteamhp=self.turnteamhp, thread=self.thread))
    
    @discord.ui.button(label="Large Attack", style=discord.ButtonStyle.red)
    async def largeattack(self, Button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user != self.turnperson:
            await self.thread.send(":x: It's not your turn!")
            return
        self.disable_all_items()
        Button.label = "Large Attack Chosen!"
        await interaction.response.edit_message(view=self)
        f = random.randint(1, 3)
        if f == 3:
            self.unturnteamhp -= random.randint(15, 25)
            if self.unturnteamhp <= 0:
                n = await finishBattle(winperson=self.turnperson, winbot=self.turnbot, loseperson=self.unturnperson, losebot=self.unturnbot)
                await self.thread.send(n)
                r = await levelUp(id=self.turnperson.id, cnx=cnx)
                await self.thread.send(r)
                return
            else:
                await self.thread.send(self.damagetexts[0]["hittextlarge"])
                embed = await attackEmbed(turnperson=self.unturnperson, turnbot=self.unturnbot, unturnperson=self.turnperson, unturnbot=self.turnbot, turnteamhp=self.unturnteamhp, unturnteamhp=self.turnteamhp)
                await interaction.respond(embed=embed, view=AttackView(turnperson=self.unturnperson, turnbot=self.unturnbot, unturnperson=self.turnperson, unturnbot=self.turnbot, turnteamhp=self.unturnteamhp, unturnteamhp=self.turnteamhp, thread=self.thread))
        else:
            await self.thread.send(self.damagetexts[0]["misstextlarge"])
            embed = await attackEmbed(turnperson=self.unturnperson, turnbot=self.unturnbot, unturnperson=self.turnperson, unturnbot=self.turnbot, turnteamhp=self.unturnteamhp, unturnteamhp=self.turnteamhp)
            await interaction.respond(embed=embed, view=AttackView(turnperson=self.unturnperson, turnbot=self.unturnbot, unturnperson=self.turnperson, unturnbot=self.turnbot, turnteamhp=self.unturnteamhp, unturnteamhp=self.turnteamhp, thread=self.thread)) 





class StartView(discord.ui.View):
     def __init__(self, acceptor, challenger, bot1, bot2, thread):
       super().__init__(timeout=None)
       self.acceptor = acceptor
       self.challenger = challenger
       self.bot1 = bot1
       self.bot2 = bot2
       self.thread = thread

     @discord.ui.button(label="Accept the Battle!", style=discord.ButtonStyle.primary)
     async def acceptbattle(self, Button: discord.ui.Button, interaction: discord.Interaction):
         if interaction.user != self.acceptor:
             await self.thread.send(":x: Only the challenged fighter can accept the battle!")
             return
         Button.disabled = True
         Button.label = "Battle Accepted!"
         await interaction.response.edit_message(view=self)
         turnid = self.challenger.id
         team1hp = 100
         team2hp = 100
         embed = cogs.combinebot.makeEmbed(
             title="{}'s turn".format(self.challenger.name),
             color=discord.Color.red()
         )
         embed.add_field(name="Team 1", value="User: {0}\nBot: {1}\n HP: {2}".format(self.challenger.name, self.bot1.name, str(team1hp)))
         embed.add_field(name="Team 2", value="User: {0}\nBot: {1}\n HP: {2}".format(self.acceptor.name, self.bot2.name, str(team2hp)))
         embed.add_field(name="Attacks", value="You can do a small attack which has a 50Percent chance of working, and does 5-10 damage.\nYou can do a large attack which has a 33Percent chance of working, and does 15-25 damage.")
         await interaction.respond(embed=embed, view=AttackView(thread=self.thread, turnteamhp=team1hp, turnbot=self.bot1, turnperson=self.challenger, unturnbot=self.bot2, unturnperson=self.acceptor, unturnteamhp=team2hp))
       

class StandBattle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.message = None
        self.thread = None

    @commands.slash_command(name="standbattle", description="Engage in a jojo-style stand battle between bots and their users!")
    async def standbattle(self, interaction,
                          bot1: discord.Option(discord.Member, description="Your bot"), # type: ignore
                          person2: discord.Option(discord.Member, description="Person #2"), # type: ignore
                          bot2: discord.Option(discord.Member, description="Person #2's bot")): # type: ignore
        person1 = interaction.author
        if bot1.bot == False or bot2.bot == False:
            await interaction.response.send_message(":x: One of the specified bots are not bots.")
            return
        if person1.bot == True or person2.bot == True:
            await interaction.response.send_message(":x: One of the specified people are bots.")
            return
        if person1 == interaction.author:
            acceptor = person2
            challenger = person1
        else:
            acceptor = person1
            challenger = person2
        await interaction.response.send_message("Request has been sent!")
        self.message = await interaction.channel.send("Please continue in this thread.")
        self.thread = await self.message.create_thread(name="{}'s Battle".format(interaction.author.name))
        embed = cogs.combinebot.makeEmbed(
            title="An enemy is approaching!",
            description="A new battle has been started.",
            color=discord.Color.blurple()
        )
        embed.add_field(name="Team 1", value="Person: {0}\nBot: {1}".format(person1.name, bot1.name))
        embed.add_field(name="Team 2", value="Person: {0}\nBot: {1}".format(person2.name, bot2.name))
        await self.thread.send("<@{0}> <@{1}>".format(acceptor.id, challenger.id), embed=embed, view=StartView(acceptor=acceptor, challenger=challenger, bot1=bot1, bot2=bot2, thread=self.thread))
        
        










def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(StandBattle(bot)) # add the cog to the bot
