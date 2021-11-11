# bot.py
import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='crabgame')
async def crabgame(ctx):
    crabgamecheats = [
        "Grab your Crab Game script here, up to date as of 1st November 2021: https://bit.ly/31oMXBy"
        ]
    response = (crabgamecheats)
    await ctx.send(response)

@bot.command(name='gta')
async def gta(ctx):
    gtacheats = [
        "Grab Kiddion's Modest Menu here, up to date as of 22nd March 2021: https://bit.ly/3kaKsJD"
        ]
    response = (gtacheats)
    await ctx.send(response)

@bot.command(name='bo3')
async def bo3(ctx):
    bo3cheats = [
        "You can find files and information on cheats for Black Ops 3 & 4 here: https://pastebin.com/HhrHktyw"
        ]
    response = (bo3cheats)
    await ctx.send(response)

@bot.command(name='warzone')
async def warzone(ctx):
    warzonecheats = [
        "You can find Warzone cheats provided by EngineOwning here: https://bit.ly/3BNFzMw"
        ]
    response = (warzonecheats)
    await ctx.send(response)

@bot.command(name='bf1')
async def bf1(ctx):
    bf1cheats = [
        "You can find a selection of Battlefield 1 cheats here at UnknownCheats: https://bit.ly/3ENAohH"
        ]
    response = (bf1cheats)
    await ctx.send(response)


@bot.event
async def on_message(message):
    if message.content.startswith('!help'):
        embedVar = discord.Embed(title="Help", description="This command is used to seek help for Zain", color=0x0ff00)
        embedVar.add_field(name="What are the commands for cheats?", value="Use the command prefix '!' followed by these games: crabgame, gta, bo3, warzone, bf1", inline=False)
        embedVar.add_field(name="My Crab Game cheats are not working", value="This may be because you need Python 3.9 installed, you can get this from the MS Store, or by using this link: https://bit.ly/3ELDYbX", inline=False)
        await message.channel.send(embed=embedVar)

bot.run(TOKEN)
