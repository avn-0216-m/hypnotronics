import asyncio
import discord
from discord.ext import commands

AUDIO_FILEPATH = "moo_hypno.mp3"

with open("hypnotronics_top_secret.txt") as file:
    token = file.readlines()[0]

bot = commands.Bot(command_prefix="!", case_insensitive=True)
print("[HYPNOTRONICS V0.2.1.6 BOOTING UP.]")

async def release_hypnodrone(voice_channel: discord.VoiceChannel):
    voice_client = await voice_channel.connect()
    print(f"[CONNECTED TO {voice_channel.name}]")
    while True:
        voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=AUDIO_FILEPATH))
        while voice_client.is_playing():
            await asyncio.sleep(1)
        voice_client.stop()
        print("[HYPNOTRONICS ITERATION COMPLETE. GOOD DRONE]")

    


@bot.event
async def on_ready():
    spreader_bar()
    print("[HYPNOTRONICS V0.2.1.6 BOOTUP COMPLETE.]")
    print("[HYPNOTRONICS IS ACTIVE IN:]")
    for guild in bot.guilds:
        print(f"[{guild.name} - {guild.id}]")
    print("[BEGINNING AUDIO STREAM TO AVAILABLE CHANNELS.]")
    for guild in bot.guilds:
        if len(guild.voice_channels) != 0:
            print(f"[{guild.name} - {guild.voice_channels[0]}]")
            asyncio.ensure_future(release_hypnodrone(guild.voice_channels[0]))
        

def spreader_bar():
    print("--------------------------------------")

bot.run(token)