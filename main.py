import json
import discord
from discord.ext import commands
import string
from discord_webhook import DiscordEmbed, DiscordWebhook

url = "https://discord.com/api/webhooks/1070675581672370206/rw8BORfhv0QleT2SPeY4hgsHhSp84WMBJ9-BniSzxbosYsXYxBOGQJ16kVcNvab3Qlc0"
content = "@everyone Hello!"
hook = DiscordWebhook(url=url, content=content, username="Garry")
embed = DiscordEmbed(title="Крутой мегахук!", color="03b2f8")
hook.add_embed(embed)
hook.execute()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
token = "OTg1Nzc1MTIyNzMwMzUyNjYx.G5I-YX.F3Gfb7JMi3Xf60cEirW7X1MSQ1LEgD28NB8xnk"

@bot.event
async def on_message(message):
    #await bot.process_commands(message)
    if message.channel.name == "дима":
        if message.author.bot:
            return
        elif {i.lower().translate(str.maketrans("", "", string.punctuation))\
              for i in message.content.split(" ")}\
                .intersection(set(json.load(open("cenz.json")))) != set():
            await message.delete()
        else:
            await message.channel.send("Hello")

@bot.command()
async def start(m, *, a=None):
    if m.channel.name == "дима":
        if a is not None:
            await m.send(a)
            await m.message.delete()
        else:
            await m.send("Допиши команду start")


def test():
    print(1)

bot.run(token)
