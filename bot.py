# bot.py
import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_message(message):
    if message.content.startswith('!help'):
        embedVar = discord.Embed(title="Help", description="This command is used to seek help for Zain", color=0x0ff00)
        embedVar.add_field(name="Crab Game", value="Grab your Crab Game script here, up to date as of 1st November 2021: https://bit.ly/31oMXBy", inline=True)
        embedVar.add_field(name="My Crab Game cheats are not working", value="This may be because you need Python 3.9 installed, you can get this from the MS Store, or by using this link: https://bit.ly/3ELDYbX", inline=True)
        embedVar.add_field(name="GTA V", value="Grab Kiddion's Modest Menu here, up to date as of 22nd March 2021: https://bit.ly/3kaKsJD", inline=True)
        embedVar.add_field(name="Warzone", value="You can find Warzone cheats provided by EngineOwning here: https://bit.ly/3BNFzMw", inline=True)
        embedVar.add_field(name="GTA V", value="Grab Kiddion's Modest Menu here, up to date as of 22nd March 2021: https://bit.ly/3kaKsJD", inline=True)
        embedVar.add_field(name="Black Ops 3 & 4", value="You can find files and information on cheats for Black Ops 3 & 4 here: https://pastebin.com/HhrHktyw", inline=True)
        embedVar.add_field(name="Battlefield 1", value="You can find a selection of Battlefield 1 cheats here at UnknownCheats: https://bit.ly/3ENAohH", inline=True)
        embedVar.add_field(name="Cold War", value="Get GeoGeo's menu and the address scanner here: https://bit.ly/30q0KaO", inline=True)
        await message.channel.send(embed=embedVar)

bot.run(TOKEN)
