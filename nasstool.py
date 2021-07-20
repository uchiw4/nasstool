from discord.ext import commands
from pyfade import Fade, Colors
from pycenter import center
import discord
import time
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




bot = commands.Bot(command_prefix= "", self_bot=True)

#entrée du token
TOKEN = input("\033[1;31;40m Ton token :  \033")

#statut
n = int(input("\033[1;31;40m Combien de statuts veux-tu (entre 1 et 5)  ?  \033"))
b=0
if n == 1:
    status1 = input("\033[1;31;40m Statut :  \033")
    b=1
elif n ==2:
    status1 = input("\033[1;31;40m Statut 1:  \033")
    status2 = input("\033[1;31;40m Statut 2:  \033")
    b=2
elif n ==3:
    status1 = input("\033[1;31;40m Statut 1:  \033")
    status2 = input("\033[1;31;40m Statut 2:  \033")
    status3 = input("\033[1;31;40m Statut 3:  \033")
    b=3
elif n ==4:
    status1 = input("\033[1;31;40m Statut 1:  \033")
    status2 = input("\033[1;31;40m Statut 2:  \033")
    status3 = input("\033[1;31;40m Statut 3:  \033")
    status4 = input("\033[1;31;40m Statut 3:  \033")
    b=4
elif n ==5:
    status1 = input("\033[1;31;40m Statut 1:  \033")
    status2 = input("\033[1;31;40m Statut 2:  \033")
    status3 = input("\033[1;31;40m Statut 3:  \033")
    status4 = input("\033[1;31;40m Statut 4:  \033")
    status5 = input("\033[1;31;40m Statut 5:  \033")
    b=5





#evenement du bot
@bot.event
async def on_ready():
    print("\033[1;31;40m C'est bon, tu peux maintenant profiter de ton nouveau statut animé !\033")
    print("")
    print("\033[1;31;40m(ne ferme pas cette fenêtre si tu veux que le logiciel continue de fonctionner)\033")
    

    if b == 1:
        await bot.change_presence(activity=discord.Game(name=status1))
    elif b == 2:
        while True:
            await bot.change_presence(activity=discord.Game(name=status1))
            await asyncio.sleep(10)
            await bot.change_presence(activity=discord.Game(name=status2))
            await asyncio.sleep(10)
    elif b == 3:
        while True:
            await bot.change_presence(activity=discord.Game(name=status1))
            await asyncio.sleep(10)
            await bot.change_presence(activity=discord.Game(name=status2))
            await asyncio.sleep(10)
            await bot.change_presence(activity=discord.Game(name=status3))
            await asyncio.sleep(10)
    elif b == 4:
        while True:
            await bot.change_presence(activity=discord.Game(name=status1))
            await asyncio.sleep(10)
            await bot.change_presence(activity=discord.Game(name=status2))
            await asyncio.sleep(10)
            await bot.change_presence(activity=discord.Game(name=status3))
            await asyncio.sleep(10)
            await bot.change_presence(activity=discord.Game(name=status4))
            await asyncio.sleep(10)
    elif b == 5:
        while True:
            await bot.change_presence(activity=discord.Game(name=status1))
            await asyncio.sleep(10)
            await bot.change_presence(activity=discord.Game(name=status2))
            await asyncio.sleep(10)
            await bot.change_presence(activity=discord.Game(name=status3))
            await asyncio.sleep(10)
            await bot.change_presence(activity=discord.Game(name=status4))
            await asyncio.sleep(10)
            await bot.change_presence(activity=discord.Game(name=status5))
            await asyncio.sleep(10)


        



#connection

bot.run(TOKEN, bot=False)
    



