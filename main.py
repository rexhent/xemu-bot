from compatibility import find_by_id, data
import json
import nextcord
from nextcord.ext import commands

with open('.api.json', 'r') as api_file:
    api_key_file = json.load(api_file)
api_key = api_key_file['token']

TESTING_GUILD_ID = 123456789  # Replace with your guild ID

# Enable necessary intents
intents = nextcord.Intents.default()
intents.message_content = True  # Enable message content intent


bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def repeat(ctx, *, message):
    await ctx.send(message)

@bot.command()
async def compat(ctx, *, message):
    await ctx.send(find_by_id(data, message))

bot.run(api_key)
