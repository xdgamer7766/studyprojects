import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_command_error(ctx,error):
    if isinstance(error, command.errors.CheckFailure):
        await ctx.send('Nem elég erős a szereped vérem, kérjé magad mellé egy admint')

@client.command()
async def hello(ctx):
        await ctx.send('Hello!')

@client.event
async def on_message(ctx):
    if 'bella ciao' in ctx.content.lower():
        emoji = 'dali:712598298745241670'
        await ctx.add_reaction(emoji)

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        'Szeva cigó, kössz hogy betoppantál a szerverre'
    )


@client.command()
@command.has_role('poller')
async def strawpoll(ctx):
    await ctx.send('What is the debate about?')
    # reading in the message
    await ctx.send('What is the first option?')
    # reading in the first option
    await ctx.send('What is the second option?')
    # reading in the second option
    # await ctx.send()

client.run('NzQwMjQ0Mzc5MzkzOTgyNDk2.XymMTQ.Xn2mNyXox1i_Cmaer9fAwXawaGs')