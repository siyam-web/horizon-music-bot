import discord
from discord.ext import commands
from discord.utils import get

# Intents
intents = discord.Intents.default()
intents.voice_states = True

# Bot prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Function to join a voice channel
async def join_channel(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You need to be in a voice channel to use this command.")

# Function to leave a voice channel
async def leave_channel(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I'm not currently in a voice channel.")

# Command to play music
@bot.command()
async def play(ctx, url):
    if not ctx.voice_client:
        await join_channel(ctx)
    voice_client = ctx.voice_client

    try:
        voice_client.stop()
        await voice_client.play(discord.FFmpegPCMAudio(url))
    except Exception as e:
        await ctx.send(f"An error occurred while trying to play the music: {e}")

# Command to stop playing music
@bot.command()
async def stop(ctx):
    voice_client = ctx.voice_client
    if voice_client:
        voice_client.stop()

# Command to disconnect the bot from the voice channel
@bot.command()
async def disconnect(ctx):
    await leave_channel(ctx)

# Run the bot
bot.run('MTIzODgxNzE3Nzc5MzIwNDI1NQ.GLtEJ1.oDTF11u5P4Qnrs8cCSZAc_xb_9Hx_Y5SbuSs4g')
