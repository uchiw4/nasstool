import os 
import json
import ctypes

try:
    import asyncio
except Exception:
    os.system("python3 -m pip install asyncio")
    import asyncio

try:
    from pyfade import Fade, Colors
except Exception:
    os.system("python3 -m pip install pyfade")
    from pyfade import Fade, Colors

try:
    from pycenter import center
except Exception:
    os.system("python3 -m pip install pycenter")
    from pycenter import center

try:
    import discord
except Exception:
    os.system("python3 -m pip install discord")
    import discord

text ="""
███╗   ██╗ █████╗ ███████╗███████╗████████╗ ██████╗  ██████╗ ██╗     
████╗  ██║██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██╔██╗ ██║███████║███████╗███████╗   ██║   ██║   ██║██║   ██║██║     
██║╚██╗██║██╔══██║╚════██║╚════██║   ██║   ██║   ██║██║   ██║██║     
██║ ╚████║██║  ██║███████║███████║   ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
by uchiw4 le beau gosse



"""
os.system("clear")

ctypes.windll.kernel32.SetConsoleTitleW("nastool rafael le beau gosse")


def nasstool(): 
    print(Fade.Vertical(Colors.red_to_purple, center(text)))

nasstool()


client = discord.Client(self_bot=True)


with open("hello.json","r+") as f:
        data_raw = json.load(f)
        stattry = data_raw["token"]

if stattry == "":
    TOKEN = input("\033[1;31;40m Ton token :  \033")

    #statut
    statuslist = []
    cmb = int(input("\033[1;31;40m Combien de statuts veux-tu ?  \033"))

    for i in range(cmb):
        
        whatstatus = input(f"\033[1;31;40m Statut {i+1}:  \033")
        statuslist.append(whatstatus)
    

    asktosave = input("\033[1;31;40m Souhaites-tu enregistrer un nouveau profil pour pouvoir le réutiliser la prochaine fois ? [o/n]  \033")
    if asktosave == "o":
        with open("hello.json","r+") as f:
            data_raw = json.load(f)
            data_raw["token"] = TOKEN
            data_raw["statuts"] = statuslist
            data_raw["cmb"] = cmb
            f.seek(0)
            json.dump(data_raw,f,indent=4)
            f.truncate() 

else:
    loadstatus = input("\033[1;31;40m Tu as déjà un profil enregistré, souhaites-tu le charger ? [o/n] \033")
    if loadstatus =="o":
        with open("hello.json","r+") as f:
            data_raw = json.load(f)
            TOKEN = data_raw["token"]
            statuslist = data_raw["statuts"]
            cmb = data_raw["cmb"]
        print("\033[1;31;40m Profil chargé avec succès !  \033")

    elif loadstatus == "n":

        TOKEN = input("\033[1;31;40m Ton token :  \033")

        #statut
        statuslist = []
        cmb = int(input("\033[1;31;40m Combien de statuts veux-tu ?  \033"))

        for i in range(cmb):

            whatstatus = input(f"\033[1;31;40m Statut {i+1}:  \033")
            statuslist.append(whatstatus)

        asktosave = input("\033[1;31;40m Souhaites-tu remplacer ton ancien profil par ce que tu viens de créer ? [o/n]  \033")
        if asktosave == "o":
            with open("hello.json","r+") as f:
                data_raw = json.load(f)
                data_raw["token"] = TOKEN
                data_raw["statuts"] = statuslist
                data_raw["cmb"] = cmb
                f.seek(0)
                json.dump(data_raw,f,indent=4)
                f.truncate() 


#evenement du bot
@client.event
async def on_ready():
    os.system("clear")
    nasstool()

    print("")
    print("\033[1;31;40m Connecté au compte de {0.user} tu peux maintenant profiter de ton statut perso !\033".format(client))
    print("")
    print("\033[1;31;40m(ne ferme pas cette fenêtre si tu veux que le logiciel continue de fonctionner)\033")
    while True:
        for i in range(cmb):
            status1 = statuslist[i]
            await client.change_presence(activity=discord.Game(name=status1))
            await asyncio.sleep(10)

#connection
client.run(TOKEN, bot=False)
