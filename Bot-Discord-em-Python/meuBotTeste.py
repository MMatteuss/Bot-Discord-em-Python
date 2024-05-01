import discord
from discord.ext import commands
import os

tk = "token"

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == 'regras':
            await message.channel.send(f'{message.author.name} as regras: {os.linesep}1- sem spam {os.linesep}2-sem secso')

client = MyClient(intents=intents)
client.run(tk)