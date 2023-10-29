import discord
import mcquery
from mcquery import mcquery
from discord import *
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="+", intents=intents)
intents = discord.Intents().all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
@bot.event
async def on_ready():
 print('Online')
 try:
    synced = await bot.tree.sync()
    print(f"------\n{len(synced)} commands Lancer\n------")
 except Exception as c:
      print(c)
@bot.tree.command(name="query", description="Voire les informations d'un serveur via l'ip et sont port !")
async def db_slash(interaction: discord.Interaction, ip: str, port: int):
        await interaction.response.send_message("```Les informations sont en cours de traitement...```\n*(si je ne vous renvoie pas les information cela veux surement dire que l'ip ou le port est mauvais)*")
        with mcquery(ip, port=port, timeout=10) as data:
            embed = discord.Embed()
            embed.set_author(name=f"Information | {ip}")
            embed.add_field(name='salut', value=f"Voici la liste de toutes les informations sur le serveur que vous avez entré (certains serveurs peuvent contourner cette requête):\n\n- Nombre de joueurs en ligne :```{data.num_players}/{data.max_players}```\n- Plugins :```{data.plugins}```")
            embed.set_footer(text=f"{bot.user.name}・ By rito.off")
            response_message = await interaction.followup.send(embed=embed)
            await response_message.add_reaction('✅')
      

bot.run('TOKEN')