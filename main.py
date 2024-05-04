import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command()
async def residuos(ctx):
    await ctx.send(f'Debes separar los residuos que se pueden reciclar de los que no. Los materiales que se pueden reciclar son: cartón, papel, metal, plástico y vidrio.')

@bot.command()
async def contenedores(ctx):
    await ctx.send(f'El papel y el cartón van en el contenedor azul, el metal y el plástico van en el contenedor amarillo y el vidrio va en el contenedor verde.')

@bot.command()
async def reutilizar(ctx):
    await ctx.send(f'Aquí tienes algunas ideas para reutilizar: puedes usar envases para guardar otras cosas, como lápices, tijeras, etc. También puedes usar botellas de plástico como macetas.')

bot.run("Token")
