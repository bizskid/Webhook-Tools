import requests
import os
from colorama import Fore
from discord_webhook import DiscordWebhook, DiscordEmbed
import sys
import time
from time import sleep
print(Fore.RED)
print("""

░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
                                         Ouais je sais c'est nul comme titre
""")

print("[1] Envoyer des messages")
print("[2] Spamer")
print("[3] Supprimer un webhook")
print("[4] Envoyer un message embed")
 #print("[5] HOHO je vois que tu regardes le script")
a = int(input("[?]: "))
if a == 1:
	while 1:
		jesaispasquoimettre = input("ce que le bot va dire : ")
		url = input("L'url du webhook : ")
		webhook = DiscordWebhook(url=url, content=jesaispasquoimettre)
		respond = webhook.execute()

if a == 2:
   jesaispasquoimettre = input("ce que le bot va dire : ")
   url = input("L'url du webhook : ")
   webhook = DiscordWebhook(url=url, content=jesaispasquoimettre)
   while 1:
   	respond = webhook.execute()
   
if a == 3:
  webhook = str(input("l'url du webhook : "))
  requests.delete(webhook)

if a == 5:
  	print("Appuis sur 1 tu l'oses")
  	q = int(input("[?]: "))

  	if q == 1:
  		print("""Ooh ooh

We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you


We've known each other for so long
Your heart's been aching but
You're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you


(Ooh, give you up)
(Ooh, give you up)
(Ooh)
Never gonna give, never gonna give
(Give you up)
(Ooh)
Never gonna give, never gonna give
(Give you up)

We've know each other for so long
Your heart's been aching but
You're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it

I just wanna tell you how I'm feeling
Gotta make you understand

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
            """)
if a == 4:
	while 1:
	   oof = input("Le titre du embed : ")
	   yey = input ("La description du embed : ")
	   url = input("L'url du webhook : ")
	   webhook = DiscordWebhook(url=url)
	   embed = DiscordEmbed(title=oof, description=yey, color=0000000)
	   webhook.add_embed(embed)
	   response = webhook.execute()
