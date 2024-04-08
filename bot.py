import os
import discord
import dotenv
import random
import datetime

from discord.ext import commands
from discord.commands import Option, slash_command  # Import slash_command

dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True  # Enable intents for member events, if needed.

# Use a command prefix of your choice; it won't affect slash commands.
bot = commands.Bot(command_prefix='!', intents=intents)

what_words = ['what', 'wat', 'waht', 'wjat']
anime_ref = ['WEEB ALERT!', 'A WILD WEEB HAS APPEARED', 'IS THIS A JOJO REFERENCE?']

timezone = datetime.timezone(datetime.timedelta(hours=-8))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    greeting_message = "Hello! Welcome to the server!"
    await member.send(greeting_message)

@bot.event
async def on_message(message):
    # Important: Add this line to process commands and allow both message and slash commands.
    await bot.process_commands(message)

    if message.author == bot.user:
        return

    for word in what_words:
        if ''.join([i for i in message.content.lower() if i.isalpha()]).endswith(word):
            await message.reply('CHICKEN BUTT :rofl:')
    if ''.join([i for i in message.content.lower() if i.isalpha()]).endswith('why'):
            await message.reply('CHICKEN THIGH :rofl:')
    if ''.join([i for i in message.content.lower() if i.isalpha()]).endswith('who'):
            await message.reply('CHICKEN POO :rofl:')
    if 'stfu' in message.content.lower() or 'kys' in message.content.lower() or 'no u' in message.content.lower() or 'nou' in message.content.lower():
            await message.reply('no u')
    if 'dp' in message.content.lower():
         await message.reply(random.choice(["Dunking Porridge?", "Dinosaur Prostate?", "Dead People?"]))

    with open('weeb.txt', 'r') as fin:
        for word in fin.read().split('|'):
            if word in message.content.lower():
                await message.reply(random.choice(anime_ref))

# Slash command
@bot.slash_command(name="ping", description="Responds with Pong!")
async def ping(ctx):
    await ctx.respond("Pong!")

bot.run(TOKEN)
