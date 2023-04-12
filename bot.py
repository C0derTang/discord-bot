#bot.py
import os, discord, dotenv, random, datetime

dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

what_words = ['what', 'wat', 'waht', 'wjat']
anime_ref = ['WEEB ALERT!', 'A WILD WEEB HAS APPEARED', 'IS THIS A JOJO REFERENCE?']

timezone = datetime.timezone(datetime.timedelta(hours=-8))

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
    for user in message.mentions:
        if user.id == 752956559885205697:
            current_time = datetime.datetime.now(timezone)
            target_time = current_time.replace(hour=22, minute=0, second=0, microsecond=0)
            if current_time < target_time:
                nickname = message.author.nick if message.author.nick else message.author.name
                await message.reply(f"{nickname} is currently focusing on homework, please do not ping until after 10:00 PM PST.")
            
client.run(TOKEN)
