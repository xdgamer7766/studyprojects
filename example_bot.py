import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def hello(ctx):
        await ctx.send('Hello!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        'Szeva cigó, kössz hogy betoppantál a szerverre'
    )

client.run('NzQwMjQ0Mzc5MzkzOTgyNDk2.XymMTQ.Xn2mNyXox1i_Cmaer9fAwXawaGs')