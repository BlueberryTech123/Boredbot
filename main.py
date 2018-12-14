import discord
import json
import asyncio

client = discord.Client()

TOKEN = 'NDgxMjQ4NTQ5OTAwNjQ4NDY4.DvMaVw.cqOcosS9zsuc5cKcXm8Y-KRMfbQ'
@client.event
async def on_ready():
    print("Bot online")
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(">ping"):
        await client.send_message(message.channel, "Pong!")
    if message.content.startswith(">help"): # --------------------------------------- "ERROR IN CODE"
        embed = discord.Embed(
            title = "Help",
            description = ">ping",
            colour = discord.colour.blue()
        )
        embed.set_footer(text="Warning: bot is still WIP")
        embed.set_author(name="User request")
        await client.say(embed = embed)
client.run(TOKEN)
