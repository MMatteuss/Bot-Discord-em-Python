import discord
from discord.ext import commands
import os

# Servidor01 = 
tk = "token"

intents = discord.Intents.default()
intents.messages = True 

bot = commands.Bot(command_prefix='!', intents=intents)

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print(f'Logged on as {self.user}!')

#     async def on_message(self, message, ctx):
#         print(f'Message from {message.author}: {message.content}')
#         if message.content == '?regras':
#             await message.channel.send(f'{message.author.name} as regras do serve:{os.linesep} 1- Não coisa o coisado{os.linesep} 2-secso{os.linesep}')

@bot.event
async def on_member_update(before,after):
    print('Lest go')

@bot.command('novidades')
async def novidades(ctx):
    usuario = ctx.author.name
    await ctx.send(f'Olá {usuario} O bot receberá atualizações em breve, espere para ver :)')



# client = MyClient(intents=intents)
bot.run(tk)
