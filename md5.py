import hashlib
import pyfiglet
import sys
from colorama import Fore
from datetime import datetime
import os.path
from os import path


intro = pyfiglet.figlet_format("MD5\nHash--Cracker\n")
print(Fore.RED+intro)

now =datetime.now()
dt = now.strftime("%d/%m/%Y %H:%M:%S")


print(Fore.YELLOW+"============================================================")
print("[*_*] Starting HASH CRACKER ... "+ "         "+dt)
print("============================================================")




wordlist = str(input(Fore.BLUE+"Enter Wordlist Location : "+Fore.WHITE))
hash = str(input(Fore.BLUE+"Enter Hash value : "+Fore.WHITE))


#passwd_list = open(wordlist).read()
#passwds = passwd_list.splitlines()

if(path.exists(wordlist) == True) :
 passwd_list = open(wordlist).read()
 passwds = passwd_list.splitlines()
 for line in passwds:
   try:
      print(Fore.YELLOW+"[!] CHECK PASSWORD [MD5] : "+ line.strip())
      hash_ob = hashlib.md5(line.strip().encode())
      hashed_pass = hash_ob.hexdigest()
      if hashed_pass == hash:
        print(Fore.GREEN+"[+] PASSWORD FOUND [MD5] : " + line.strip())
        break
   except Exception as e :
      print(e)
      pass

 print(Fore.RED+"------------------END of HashCracker------------------")

else :
  print(Fore.RED+"[-] INVALID FILE, Please try again ...")
