import discord
from discord.ext import commands
import os
from discord import reaction
from discord import Reaction
import json
import cogs.combinebot
from cogs.combinebot import name
from cogs.combinebot import game
from cogs.combinebot import icon
from cogs.combinebot import VERSION
from cogs.combinebot import LATESTADDITION



class Role(commands.Cog):
    group = discord.SlashCommandGroup(name="role", description="Commands for managing roles")

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None





    @group.command(name="addrole", description="Adds a role to a user.")
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, interaction, user: discord.Option(discord.Member, description="User to give role to", required=True), role: discord.Option(discord.Role, description="Role to give user", required=True)): # type: ignore
       await user.add_roles(role, atomic=True)
       await interaction.response.send_message("The role has been added to the user!")

    @group.command(name="removerole", description="Removes a role from a user.")
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, interaction, user: discord.Option(discord.Member, description="User to remove role from", required=True), role: discord.Option(discord.Role, description="Role to remove", required=True)): # type: ignore
       await user.remove_roles(role, atomic=True)
       await interaction.response.send_message("The role has been removed from the user!")

    @group.command(name="createrole", description="Creates a basic no perms role.")
    @commands.has_permissions(manage_roles=True)
    async def createrole(self, interaction, name: discord.Option(str, description="Name of role", required=True), server: discord.Option(discord.Guild, description="Name of the server to make role in. Case sensitive!", required=True)): # type: ignore
       await server.create_role(name=name)
       await interaction.response.send_message("The role **" + name + "** has been created.")

    @group.command(name="roleinfo", description="Gets detailed info on a role")
    async def roleinfo(self, interaction, role: discord.Option(discord.Role, description="Role to get info on")): # type: ignore
         embed = cogs.combinebot.makeEmbed(
              title = "Info on {0}".format(role.name),
              description = """
              **Created at:** {0} 
              **Hoisted:** {1} 
              **Mentionable:** {2}
              **Position:** {3} 
              
              
              """.format(role.created_at, role.hoist, role.mentionable, str(role.position)),
              color = role.colour,
         
         )
         
         await interaction.response.send_message(embed=embed)



def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Role(bot)) # add the cog to the bot

