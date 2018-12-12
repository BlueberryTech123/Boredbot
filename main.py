import discord
import json
import asyncio as asio

TOKEN = '481248549900648468'
async def on_message(message):
    if message.content.startwith(">ping"):
        await client.send_message(message.channel, "Pong!");
    # return message "Pong!"
client.run(TOKEN);
