import discord
from discord.ext import commands
from itertools import cycle
import botLib
import asyncio
import os

#enable intents and set command prefix
intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix = "!", intents = intents)

#events
@client.event
async def on_ready():
    print("Bot is online!")
    print("Running on version: " + str(discord.__version__))
    print("    ________")

    #set status
    await client.wait_until_ready()
    activities = cycle(botLib.activityList)

    while not client.is_closed():
        current_activity = next(activities)
        await client.change_presence(activity = discord.Game(current_activity))
        await asyncio.sleep(300)

#commands
#load extension
@client.command()
async def load(ctx, extension):
    client.load_extension("cogs." + extension)

#unload extension
@client.command()
async def unload(ctx, extension):
    client.unload_extension("cogs." + extension)

#reload extension
@client.command()
async def reload(ctx, extension):
    try:
        client.reload_extension("cogs." + extension)
        await ctx.message.add_reaction("✅")
    except:
        await ctx.message.add_reaction("❌")

#load cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension("cogs." + filename[:-3])


#bot token
client.run(botLib.token)
