import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv("credentials.env")
TOKEN = os.getenv('TOKEN')
# start bot
intents = discord.Intents.all()
intents.members = True
loaded = False
client = commands.Bot(command_prefix="-", help_command=None,
                      intents=intents)


async def load_cogs():
    client.load_extension('jishaku')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
            print(f'Loaded {filename}')
    loaded = True


@client.event
async def on_ready():
    print('Bot is ready.')
    # turn presence to watching "Chads"
    ecsguild = client.get_guild(902975048514678854)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=ecsguild.member_count + " Chads"))

asyncio.run(load_cogs())
# run bot
client.run(TOKEN)
