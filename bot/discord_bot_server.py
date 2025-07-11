import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is online and ready.')

@bot.command()
async def status(ctx):
    await ctx.send("✅ KX9-Z7D3R1 Codex bot is active and listening.")

@bot.command()
async def push(ctx):
    os.system("python3 scripts/git_agent.py")
    await ctx.send("📤 Changes pushed to GitHub.")

bot.run(TOKEN)
