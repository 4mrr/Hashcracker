import pyfiglet
from colorama import Fore
from datetime import datetime


def intro_hashcracker():
 intro = pyfiglet.figlet_format("\nHash--Cracker\n")
 print(Fore.RED+intro)

 now =datetime.now()
 dt = now.strftime("%d/%m/%Y %H:%M:%S")


 print(Fore.YELLOW+"============================================================")
 print("[*_*] Starting HASH CRACKER ... "+ "         "+dt)
 print("============================================================")
