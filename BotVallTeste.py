import discord 
from discord import app_commands
import random

# teste DataBase
from psycopg2 import sql
import psycopg2

db_config = {
    "dbname": "postgres",
    "user": "Bot",
    "password": "1234",
    "host": "localhost",
    "port": "5432"
}

idDoServidor = 1210274340395024405
tk = "token"

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild= discord.Object(id=idDoServidor))
            self.synced = True
        print(f'entramos como {self.user}.')

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild=discord.Object(id=idDoServidor), name="teste", description="Testando Bot")
async def testeCmd(interaction: discord.Interaction):
    await interaction.response.send_message(f'Estou funcioanando corretamente', ephemeral = False)

@tree.command(guild=discord.Object(id=idDoServidor), name= 'dados', description='Número aleatorio')
async def dados(interaction: discord.Interaction):
    numero = random.randint(1, 5)
    await interaction.response.send_message(f'Dados Número: {numero}', ephemeral = False)


# teste
@tree.command(guild=discord.Object(id=idDoServidor), name= 'meunome', description='Pegar nome do usuário')
async def dados(interaction: discord.Interaction):
    
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("select nome from usuarios ", ())
    nome = cursor.execute

    await interaction.response.send_message(f'Dados Número: {nome}', ephemeral = False)



aclient.run(tk)

