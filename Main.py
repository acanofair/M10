import discord
import os
from discord.ext import commands 


client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print('New participant has entered!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Jin Kazama'):
        await message.channel.send('Welcome to The King of Iron First Tournament!')

client.run(os.environ.get('DISCORD'))
