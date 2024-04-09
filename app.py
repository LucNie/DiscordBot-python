import discord
import os # default module
# import datController (./commands/dataController.py)
from commands.dataController import player, cards, ids, init, saveAllPlayerData, createPlayerData, savePlayerData, setPlayerDefaultImage
from commands.embedController import profileEmbed
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
bot = discord.Bot()



@bot.event
async def on_ready():
    init()
    print(f"Logged in as {bot.user.name} ({bot.user.id})")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.slash_command(name = "create", description = "Create a new player data")
async def create(ctx):
    discordID = str(ctx.author.id)
    if discordID in player:
        await ctx.respond("You already have a player data!")
    else:
        createPlayerData(discordID)
        savePlayerData(discordID)
        await ctx.respond("Player data created!")

@bot.slash_command(name = "profile", description = "Show your profile")
async def profile(ctx):
    discordID = str(ctx.author.id)
    if discordID in player:
        await ctx.respond(embed = profileEmbed(discordID, ctx))
    else:
        await ctx.respond("You don't have a player data!")

@bot.slash_command(name = "setimage", description = "Set your profile image")
async def setimage(ctx, url: str):
    discordID = str(ctx.author.id)
    if discordID in player:
        setPlayerDefaultImage(discordID, url)
        await ctx.respond("Image set!")
    else:
        await ctx.respond("You don't have a player data!")

bot.run(os.getenv('TOKEN')) # run the bot with the token