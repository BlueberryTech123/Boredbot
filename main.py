import discord
import json
import asyncio as asio

client = discord.Client();

TOKEN = 'NDgxMjQ4NTQ5OTAwNjQ4NDY4.DvMaVw.cqOcosS9zsuc5cKcXm8Y-KRMfbQ';
async def on_message(message):
    if message.content.startwith(">ping"):
        await client.send_message(message.channel, "Pong!");
    # return message "Pong!"
client.run(TOKEN);
