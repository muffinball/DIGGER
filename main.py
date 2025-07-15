import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord-log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='?', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Buried Fossils Bot ready! Logged in as {bot.user}")

# Ping to check bot latency
@bot.command()
async def ping(ctx):
    latency_ms = round(bot.latency * 1000)
    await ctx.send(f"Pong! {latency_ms} ms")

# Basic welcome message command
@bot.command()
async def welcome(ctx, *, membername=None):
    membername = membername or ctx.author.name
    await ctx.send(f"Welcome to the Buried Fossils server, {membername}! Dig deep and have fun!")

# Info about the game
@bot.command()
async def info(ctx):
    await ctx.send(
        "🌟 **Buried Fossils** is a Roblox mining adventure where you dig, discover rare fossils, and level up! "
        "Check out the game here: [[Buried Fossils](https://www.roblox.com/games/99225351779258/Buried-Fossils)]\n"
        "Join events, trade fossils, and dominate the leaderboard!"
    )

# Command to share game link
@bot.command()
async def game(ctx):
    await ctx.send("Play Buried Fossils on Roblox now: [[Buried Fossils](https://www.roblox.com/games/99225351779258/Buried-Fossils)] 🚀")

# Fossil facts (random fact command)
import random
fossil_facts = [
    "Did you know? Fossils can be millions of years old!",
    "In Buried Fossils, some fossils are rarer than others — keep digging!",
    "Fossils tell us stories about dinosaurs and ancient creatures.",
    "The deeper you dig, the better fossils you find!",
    "Some fossils have special powers in the game — hunt them down!"
]

@bot.command()
async def fact(ctx):
    fact = random.choice(fossil_facts)
    await ctx.send(f"🦴 Fossil Fact: {fact}")

# Leaderboard placeholder
@bot.command()
async def leaderboard(ctx):
    await ctx.send("Leaderboard is coming soon! Stay tuned for the top fossil hunters! 🏆")

# Help command override (shows your custom commands)
@bot.command()
async def help(ctx):
    help_text = """
    **Buried Fossils Bot Commands:**
    `?ping` - Check bot latency
    `?welcome [name]` - Send a welcome message
    `?info` - Info about Buried Fossils game
    `?game` - Get the game link
    `?fact` - Get a random fossil fact
    `?leaderboard` - See the leaderboard (coming soon)
    """
    await ctx.send(help_text)

# Fun command to “dig”
@bot.command()
async def dig(ctx):
    outcomes = [
        "You dug up a rare fossil! 🦕",
        "Just dirt... keep trying!",
        "You found some ancient bones! 🦴",
        "Nothing here... but keep your hopes high!",
        "You uncovered a mysterious artifact! 🔮"
    ]
    result = random.choice(outcomes)
    await ctx.send(result)

# Command to show server rules (replace with your actual rules)
@bot.command()
async def rules(ctx):
    rules_text = """
    **Server Rules:**
    1. Be respectful to others.
    2. No spamming or advertising.
    3. Keep channels on topic.
    4. No cheating or exploits in the game.
    5. Have fun and help each other out!
    """
    await ctx.send(rules_text)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)