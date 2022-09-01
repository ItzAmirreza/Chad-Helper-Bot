import discord
import aiohttp
import asyncio
from discord.ext import tasks, commands


class PluginInformation(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.loaded = False

    @commands.Cog.listener()
    async def on_ready(self):
        if self.loaded:
            return
        self.loaded = True
        self.update_plugin_information.start()

    @tasks.loop(seconds=60)
    async def update_plugin_information(self):
        # send GET request to "https://api.spiget.org/v2/resources/90411"
        # make a fake header
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        }
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.spiget.org/v2/resources/90411", headers=headers) as resp:
                data = await resp.json()
                if "error" in data:
                    print("Error: " + data["error"])
                else:
                    downloads_count = data['downloads']
                    that_channel = self.client.get_channel(1014827843231957002)
                    await that_channel.edit(name=str(downloads_count) + " Spigot Downloads")


async def setup(client):
    await client.add_cog(PluginInformation(client))
    print("PluginInformation LOADED")
