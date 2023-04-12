#bot.py
import os, discord, dotenv, random

dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

what_words = ['wdym', 'what', 'wat', 'waht', 'wjat', 'wtf']
anime_ref = ['WEEB ALERT!', 'A WILD WEEB HAS APPEARED', 'IS THIS A JOJO REFERENCE?']

client = discord.Client(intents = discord.Intents.all())

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    greeting_message = "Hello! Welcome to the server!"
    await member.send(greeting_message)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for word in what_words:
        if ''.join([i for i in message.content.lower() if i.isalpha()]).endswith(word):
            await message.reply('CHICKEN BUTT :rofl:')
    if ''.join([i for i in message.content.lower() if i.isalpha()]).endswith('why'):
            await message.reply('CHICKEN THIGH :rofl:')
    if ''.join([i for i in message.content.lower() if i.isalpha()]).endswith('who'):
            await message.reply('CHICKEN POO :rofl:')
    if 'stfu' in message.content.lower():
            await message.reply('no u')
    with open('weeb.txt', 'r') as fin:
        for word in fin.read().split('|'):
            if word in message.content.lower():
                await message.reply(random.choice(anime_ref))

client.run(TOKEN)
