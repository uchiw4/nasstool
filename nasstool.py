from discord.ext import commands
from pyfade import Fade, Colors
from pycenter import center
import discord
import asyncio


text ="""
███╗   ██╗ █████╗ ███████╗███████╗████████╗ ██████╗  ██████╗ ██╗     
████╗  ██║██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██╔██╗ ██║███████║███████╗███████╗   ██║   ██║   ██║██║   ██║██║     
██║╚██╗██║██╔══██║╚════██║╚════██║   ██║   ██║   ██║██║   ██║██║     
██║ ╚████║██║  ██║███████║███████║   ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
by uchiw4 le beau gosse



"""
print(Fade.Vertical(Colors.red_to_blue, center(text)))




client = discord.Client(self_bot=True)

#entrée du token
TOKEN = input("\033[1;31;40m Ton token :  \033")

#statut
list = []
cmb = int(input("\033[1;31;40m Combien de statuts veux-tu ?  \033"))

for i in range(cmb):
    
    whatstatus = input(f"\033[1;31;40m Statut {i+1}:  \033")
    list.append(whatstatus)


        

#evenement du bot
@client.event
async def on_ready():
    print("\033[1;31;40m Connecté au compte de {0.user} tu peux maintenant profiter de ton statut perso !\033".format(client))
    print("")
    print("\033[1;31;40m(ne ferme pas cette fenêtre si tu veux que le logiciel continue de fonctionner)\033")
    while True:
        for i in range(cmb):
            i = int(i)
            status1 = list[i]
            await client.change_presence(activity=discord.Game(name=status1))
            await asyncio.sleep(10)

#connection

client.run(TOKEN, bot=False)
    



