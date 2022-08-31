import discord
from discord.ext import commands
import asyncio


class Verification(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        pass


async def setup(client):
    await client.add_cog(Verification(client))
