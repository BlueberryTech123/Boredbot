import discord
import json
import asyncio

client = discord.Client()

TOKEN = 'NDgxMjQ4NTQ5OTAwNjQ4NDY4.DvMaVw.cqOcosS9zsuc5cKcXm8Y-KRMfbQ'
@client.event
async def on_message(message):
    if message.author == client.user: return
    if message.content.startswith(">ping"):
        await client.send_message(message.channel, "Pong!")
    # return message "Pong!"
client.run(TOKEN)
