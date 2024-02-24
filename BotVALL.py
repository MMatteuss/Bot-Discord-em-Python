import discord 
from discord import app_commands
import random

idDoServidor = 1210274340395024405
tk = "token"

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        if not self.synced:
            await tree.sync(guild=discord.Object(id=idDoServidor))
            self.synced = True
        print(f'entramos como {self.user}.')

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild=discord.Object(id=idDoServidor), name="teste", description="Testando Bot")
async def testeCmd(interaction: discord.Interaction):
    await interaction.response.send_message(content='Estou funcionando corretamente', ephemeral=False)

@tree.command(guild=discord.Object(id=idDoServidor), name='dados', description='Número aleatório')
async def dados(interaction: discord.Interaction):
    numero = random.randint(1, 5)
    await interaction.response.send_message(content=f'Dados Número: {numero}', ephemeral=False)

aclient.run(tk)