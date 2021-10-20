import discord
from discord.ext import commands

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    #commands
    #ping
    @commands.command(description = "pings the bot")
    async def ping(self, ctx):
        await ctx.send("Pong! Latency: " + str(round(self.client.latency * 1000)) + "ms")

    #clear messages
    @commands.command(aliases = ["delete"], description = "clears messages, default num is 1, only admin can use")
    @commands.has_permissions(administrator = True)
    async def clear(self, ctx, amount = 1):
        await ctx.channel.purge(limit = amount + 1)
        
def setup(client):
    client.add_cog(Basic(client))
