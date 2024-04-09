import os
import json
from pathlib import Path
player = {}
cards = {
    "standard": {},
    "ego": {}
}
ids = {} # character identity



playerFilesPath =  os.listdir(os.path.join(Path(__file__).parent, "../DATA/users/"))
cardsFilesPath = os.listdir(os.path.join(Path(__file__).parent, "../DATA/cards/"))
idFilesPath = os.listdir(os.path.join(Path(__file__).parent, "../DATA/ids/"))



def init():
    loadPlayerData()
    loadCardData()
    loadIDData()

def loadPlayerData():
    for file in playerFilesPath:
        with open(os.path.join(Path(__file__).parent, "../DATA/users/", file), "r") as f:
            player[file[:-5]] = json.load(f)

def loadCardData():
    for file in cardsFilesPath:
        with open(os.path.join(Path(__file__).parent, "../DATA/cards/", file), "r") as f:
            cards[file[:-5]] = json.load(f)

def loadIDData():
    for file in idFilesPath:
        with open(os.path.join(Path(__file__).parent, "../DATA/ids/", file), "r") as f:
            ids[file[:-5]] = json.load(f)

def savePlayerData(discordID):
    with open(os.path.join(Path(__file__).parent, f"../DATA/users/{discordID}.json"), "w") as f:
        json.dump(player[discordID], f, indent = 4)

def saveAllPlayerData():
    for discordID in player:
        savePlayerData(discordID)

def setPlayerDefaultImage(discordID, url):
    player[discordID]["image"]["default"] = url
    savePlayerData(discordID)

def createPlayerData(discordID, name = "joe", faction = "P corp backstreet resident"):
    player[discordID] = {
        "id": discordID,
        "image" : {
            "default": "",
        },
        "name": name, # discord name
        "Faction": faction, # Faction name
        "MS": 0, # Mental Stability
        "HP": 50, # Health Points
        "Identity": 0, # Identity ( define player's max HP,MS ect)
        "Stagger": 25, # Stagger Points
        "Staggered": False, # Staggered status
        "BattlePassif": {}, # Battle passif
        "status": {}, # Status effect (poison, burn ect)
        "inventory": {}, # Inventory
        "cards": {}, # max 4
        "EGOCards": {},
        "energy": 0,
        "EGO": 0,
        "emotionLevel": 0, # 0 to 5
        "emotion": 0 # 1(3),2(3),3(5),4(5),5(7)
    }
    savePlayerData(discordID)

def getPlayerData(discordID):
    if discordID not in player:
        createPlayerData(discordID)
    return player[discordID]

def setPlayerData(discordID, key, value):
    player[discordID][key] = value
    savePlayerData(discordID)

def addPlayerData(discordID, key, value):
    player[discordID][key] += value
    savePlayerData(discordID)

def removePlayerData(discordID, key, value):
    player[discordID][key] -= value
    savePlayerData(discordID)
