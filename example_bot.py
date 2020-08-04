import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('§hello'):
        await message.channel.send('Hello!')

client.run('NzQwMjQ0Mzc5MzkzOTgyNDk2.XymMTQ.Xn2mNyXox1i_Cmaer9fAwXawaGs')