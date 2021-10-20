import discord
from discord.ext import commands, tasks
from discord.utils import get
import giphy_client
import random
import botLib
import asyncio

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    #commands
    #flip a coin
    @commands.command(aliases = ["coin"], description = "Flips a coin")
    async def flip(self, ctx):
        num = random.randint(1,2)
        if num == 1:
            await ctx.send("It's heads.")
        elif num == 2:
            await ctx.send("It's tails.")

    #8ball
    @commands.command(aliases = ["8ball"], description = "Tells your fortune (requires a question to be asked)")
    async def _8ball(self, ctx, *, question):
        await ctx.send("Your question: " + question + "\nYour Answer: " + random.choice(botLib.eightBallResponses))

    #someone
    @commands.command(description = "Mentions a random user in the server")
    @commands.has_permissions(administrator = True)
    async def someone(self, ctx):
        await ctx.send(random.choice(ctx.channel.guild.members).mention)

    #echo user message
    @commands.command(description = "Repeats your message")
    async def echo(self, ctx, *, message):
        await ctx.send(message)

    #say user message after deleting the original
    @commands.command(description = "Repeats your message, but deletes your message")
    async def isay(self, ctx, *, message):
        await ctx.channel.purge(limit = 1)
        await ctx.send(message)

    #send a gif based on a specified search
    @commands.command(aliases = ["giphy"], description = "Sends a gif from Giphy based on a search")
    async def gif(self, ctx, *, query):
        limit = 100
        api_instance = giphy_client.DefaultApi()

        try:
            response = api_instance.gifs_search_get(botLib.giphyToken, query, limit = limit)
            lst = list(response.data)
            gif = random.choices(lst)

            await ctx.send(gif[0].url)

        except ApiException as e:
            await ctx.send("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

    #insult
    @commands.command(aliases = ["sendembed", "embed"], description = "Sends a template embed")
    async def sendEmbed(self, ctx):
        #create and edit embed
        testEmbed = discord.Embed(title = "Title", description = "Description", color = discord.Color.blue())
        testEmbed.set_image(url = "https://cdn.discordapp.com/attachments/510681636833329163/900235422381252608/black-cat.jpg")
        #send embed
        message = await ctx.send(embed = testEmbed)

        #react to embed
        await message.add_reaction("👍")

def setup(client):
    client.add_cog(Fun(client))
