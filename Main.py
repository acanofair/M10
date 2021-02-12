import discord
import os
import asyncio
import bs4 as soup
from discord.ext import commands 

releases = []

def DISORD():
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



async def eyesoverheaven():
    task 1 = 
    url = "https://www.nike.com/launch/t/dunk-high-vast-grey"
    view = soup(url).BeautifulSoup.text
    return view


print(eyesoverheaven())

