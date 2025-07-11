import os
import discord
from discord.ext import commands
from flask import Flask

# Load token from secret
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Set up Discord bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Respond to /start
@bot.command(name='start')
async def start(ctx):
    await ctx.send("✅ KX9-Z7D3R1 notification system is active.")

# Respond to /status
@bot.command(name='status')
async def status(ctx):
    await ctx.send("📡 System status: Monitoring...")

# Optional: HTTP Flask server for keep-alive (if needed on Render)
app = Flask(__name__)

@app.route('/')
def home():
    return "Discord Bot Webhook is live."

# Start both Flask and Discord bot
if __name__ == '__main__':
    import threading

    def run_flask():
        app.run(host='0.0.0.0', port=5000)

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    bot.run(DISCORD_BOT_TOKEN)
