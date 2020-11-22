from dhooks import Webhook
from pynput.keyboard import Listener
import time
import os
from colorama import Fore, Back, Style
from colorama import init as cinit
import platform
os.system('cls')
os.system('title Speaking Your Webhook!')

print(Fore.WHITE + """

           ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ███████╗██████╗ ███████╗ █████╗ ██╗  ██╗
           ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔══██╗██╔════╝██╔══██╗██║ ██╔╝
           ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ███████╗██████╔╝█████╗  ███████║█████╔╝ 
           ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ╚════██║██╔═══╝ ██╔══╝  ██╔══██║██╔═██╗ 
          ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ███████║██║     ███████╗██║  ██║██║  ██╗
           ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

 
     """ + Fore.WHITE + "                                                                                                          Dev: Hiroyuki#" + Fore.LIGHTRED_EX + "1342")


print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.LIGHTGREEN_EX + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.LIGHTGREEN_EX + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.LIGHTGREEN_EX + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         Welcome To The"+Fore.LIGHTGREEN_EX+" Webhook-Speak ")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         Modes: "+Fore.LIGHTGREEN_EX+"Normal and Custom\n\n")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                      ["+Style.BRIGHT + Fore.LIGHTGREEN_EX + Back.BLACK +"1"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"Normal "  + Fore.WHITE + Back.BLACK +"["+Style.BRIGHT + Fore.LIGHTRED_EX + Back.BLACK +"Avatar ve İsim Değiştirilemez."+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                      ["+Style.BRIGHT + Fore.LIGHTGREEN_EX + Back.BLACK +"2"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"Custom " + Fore.WHITE + Back.BLACK + "["+Style.BRIGHT + Fore.LIGHTRED_EX + Back.BLACK +"Avatar ve İsimimi Değiştirilebilir."+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.LIGHTGREEN_EX + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.LIGHTGREEN_EX + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.LIGHTGREEN_EX + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")

secim = input(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + ">" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + "Please prefer: " + Fore.LIGHTWHITE_EX)

if secim == '1':
    webhook = input(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + ">" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + "Your Webhook: " + Fore.LIGHTWHITE_EX)
    hook = Webhook(webhook)
    user = input(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + ">" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + "Webhook Name:" + Fore.LIGHTWHITE_EX)
    avatar=input(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + ">" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX +"Webhook Avatar: "+ Fore.LIGHTWHITE_EX)
    while True:
        say = input(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + ">" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + "Webhook Say:" + Fore.LIGHTWHITE_EX)
        hook.send(say, username=user, avatar_url=avatar)
        print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + ">" + Fore.WHITE + "]" + "[" + Fore.RED + f"{say}" + Fore.WHITE + "]" + " Sent Successfully.")


elif secim == '2':
    webhook = input(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + ">" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + " Your Webhook: " + Fore.LIGHTWHITE_EX)
    hook = Webhook(webhook)
    while True:
        say = input(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + ">" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + "Webhook Say:" + Fore.LIGHTWHITE_EX)
        user = input(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + ">" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + "Webhook Name:" + Fore.LIGHTWHITE_EX)
        avatar=input(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + ">" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX +"Webhook Avatar: "+ Fore.LIGHTWHITE_EX)
        hook.send(say, username=user, avatar_url=avatar)
        print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + ">" + Fore.WHITE + "]" + "[" + Fore.RED + f"{say}" + Fore.WHITE + "]" + " Sent Successfully.")
    