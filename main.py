
import os
from pydoc import describe
import re
import discord
import requests
import json
from sources.Help import Help 
from sources.url_shortener import URLShoter
from sources.food_random import Food
from sources.waifu import Anime
from discord.ext import commands,tasks
from sources.outside import Outside 

prefix = ["?"]
custom_prefixes = {}

async def determine_prefix(bot, message):
    guild = message.guild
    if guild:
        return custom_prefixes.get(guild.id, prefix)
    else:
        return prefix

client = commands.Bot(command_prefix = determine_prefix,help_command=None)

@client.command()
@commands.guild_only()
async def setprefix(ctx, *, prefixes=""):
    custom_prefixes[ctx.guild.id] = prefixes.split() or prefix
    await ctx.send(f"Chuyển prefix thành `{prefixes}` ")

#Run server
if __name__=="__main__":
  client.add_cog(Anime(client))
  client.add_cog(Food(client))
  client.add_cog(Outside(client))
  client.add_cog(Help(client))
  client.add_cog(URLShoter(client))
  client.run(os.getenv('TOKEN'))
