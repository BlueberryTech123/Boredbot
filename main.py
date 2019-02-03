import discord
import time
import sys
import datetime

client = discord.Client()
curdt = datetime.datetime.now()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=">help in this barrel 🛢️"))
    print("Playing status...Done")
    await client.send_message(client.get_channel("539595664674390017"), "```" + str(curdt) + "\nBot online```")
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(">ping"):
        await client.send_message(message.channel, "Pong! :ping_pong:")
    if message.content.startswith(">help"): # help command
        embed = discord.Embed(
            description = "Help for commands. Pffffft... OBVIOUSLY :smirk:",
            colour = discord.Colour.gold()
        )
        embed.set_footer(text="You\'re welcome")
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        embed.add_field(name="Information", value="`>botinfo` `>help` `>ping`", inline=False)
        embed.add_field(name="Fun", value="`>weebify` `>emojify`")
        embed.add_field(name="(Exposed) Developer Commands", value="`>change_stat` `>shutdown`", inline=False)
        await client.send_message(message.channel, embed = embed)
    if message.content.startswith(">botinfo"):
        botinfEmbed = discord.Embed(
            title = "Bot Info",
            description = ":robot: Client ID: 532689187191914538\n:timer: Date created: " + str(client.user.created_at) + "\n:snake: Discord.py version: " + discord.__version__ + "\n:file_cabinet: Servers: " + str(len(client.servers)),
            colour = discord.Colour.gold()
        )
        await client.send_message(message.channel, embed = botinfEmbed)
    if message.content.startswith(">weebify"):
        if message.content == ">weebify": await client.send_message(message.channel, ":x: What shouwd I weebify?")
        else:
            weebify = message.content.replace(">weebify ", '')
            weebify = weebify.replace("r", 'w', len(weebify))
            weebify = weebify.replace("l", 'w', len(weebify))
            weebify = weebify.replace("ai", 'aiy', len(weebify))
            await client.send_message(message.channel, weebify)
    if message.content.startswith(">emojify"):
        await client.send_message(message.channel, ":x: I can\'t do that! I need training!")
    # -------------------------------------------------------------------------------------------------------
    if message.content.startswith(">shutdown"):
        await client.purge_from(message.channel, limit=1, check=None)
        try:
            await client.send_message(client.get_channel("539595664674390017"), "```" + str(curdt) + "\nBot shutdown was requested by " + message.author.id + "```")
            sys.exit()
        except:
            print("failed to exit")
            await client.send_message(client.get_channel("539595664674390017"), "```" + str(curdt) + "\nBot has been attempted shut down by " + message.author.id + " but failed```")

    if message.content.startswith(">change_stat"): # change boredbot's game status
        if message.content.replace(">change_stat ", '') == "~def~": # set to default boredbotstatus
            await client.change_presence(game=discord.Game(name=">help in this barrel 🛢️"))
        else:
            await client.change_presence(game=discord.Game(name=message.content.replace(">change_stat ", '')))
        await client.send_message(client.get_channel("539595664674390017"), "```" + str(curdt) + "\nBot status was changed by " + message.author.id + "```")


client.run("NTMyNjg5MTg3MTkxOTE0NTM4.DyveYw.G-aD4V5tyIVQC1gH3pkIGjx3uu8")
