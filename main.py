import discord
import json
import asyncio

client = discord.Client()

TOKEN = 'NDgxMjQ4NTQ5OTAwNjQ4NDY4.DvMaVw.cqOcosS9zsuc5cKcXm8Y-KRMfbQ'
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="with the >help command!"))
    print("Playing status...Done")
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(">ping"):
        await client.send_message(message.channel, "Pong!")
    if message.content.startswith(">help"): # --------------------------------------- "ERROR IN CODE"
        embed = discord.Embed(
            title = "Help",
            description = "Help for commands. If you\'re looking for the items, ``>shop`` would do its job :briefcase:",
            colour = discord.Colour.blue()
        )
        embed.set_footer(text="Warning: bot is still WIP")
        embed.set_author(name=embed.author.name, icon_url=embed.author.avatar_url)
        embed.add_field(name="Information", value="``>help`` ``>ping``", inline=False)
        await client.send_message(message.channel, embed = embed)
client.run(TOKEN)
