from .dataController import player, cards, ids, init, saveAllPlayerData, createPlayerData, savePlayerData
from .emoji import emoji
import discord

EMOJI_SERVEUR = 1149336713655758939 

def profileEmbed(discordID, bot: discord.Bot):
    embed = discord.Embed(
        title= player[discordID]["name"],
        description= player[discordID]["Faction"],
        color= discord.Color.blue()
        )
    embed.add_field(name = "Health Points", value = emoji["HP"] + str(player[discordID]["HP"]), inline = True)
    embed.add_field(name = "Mental Stability", value = emoji["MS"] + str(player[discordID]["MS"]), inline = True)
    embed.add_field(name = "Identity", value = emoji["Identity"] + player[discordID]["Identity"], inline = True)
    # pour chaque status 
    StrStatus = ""
    for status in player[discordID]["status"]:
        localStatus = player[discordID]["status"]
        if localStatus[status]["turn"] >= 0:
            # si >= 0 alors status non permanent
            StrStatus += f"{localStatus[status]['count']}{emoji[status]} {localStatus[status]['name']} : {localStatus[status]['turn']} tours\n"
        else:
            StrStatus += f"{localStatus[status]['count']}{emoji[status]} {localStatus[status]['name']} : Permanent\n"
    embed.add_field(name = "Status", value = StrStatus, inline = False)



    embed.image = player[discordID]["image"]["default"]



    return embed