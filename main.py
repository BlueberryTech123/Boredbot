import discord
import json
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="something. I\'m bored..."))
    print("Playing status...Done")
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(">ping"):
        await client.send_message(message.channel, "Pong!")
    if message.content.startswith(">help"):
        embed = discord.Embed(
            description = "Help for commands. Pffffft... OBVIOUSLY :smirk:",
            colour = discord.Colour.gold()
        )
        embed.set_footer(text="You\'re welcome")
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        embed.add_field(name="Information", value="`>botinfo` `>help` `>ping`", inline=False)
        await client.send_message(message.channel, embed = embed)
    if message.content.startswith(">botinfo"):
        botinfEmbed = discord.Embed(
            title = "Bot Info",
            description = ":robot: Client ID: 532689187191914538\n:timer: Date created: " + str(client.user.created_at) + "\n:snake: Discord.py version: " + discord.__version__ + "\n:file_cabinet: Servers: " + str(len(client.servers)),
            colour = discord.Colour.gold()
        )
        await client.send_message(message.channel, embed = botinfEmbed)
client.run(TOKEN)
