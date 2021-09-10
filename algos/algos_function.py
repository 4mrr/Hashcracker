import hashlib
import pyfiglet
import sys
from colorama import Fore
from datetime import datetime
import os.path
from os import path




def algo_md5():

 wordlist = str(input(Fore.BLUE+"Enter Wordlist Location : "+Fore.WHITE))
 hash_v = str(input(Fore.BLUE+"Enter Hash value : "+Fore.WHITE))



 if(path.exists(wordlist) == True) :
  passwd_list = open(wordlist).read()
  passwds = passwd_list.splitlines()
  for line in passwds:
   try:
      print(Fore.YELLOW+"[!] CHECK PASSWORD [MD5] : "+ line.strip())
      hash_ob = hashlib.md5(line.strip().encode())
      hashed_pass = hash_ob.hexdigest()
      if hashed_pass == hash_v:
        print(Fore.GREEN+"[+] PASSWORD FOUND : " + line.strip())
        break
   except Exception as e :
      print(e)
      pass

  print(Fore.RED+"------------------END of HashCracker------------------")

 else :
  print(Fore.RED+"[-] INVALID FILE, Please try again ...")

def algo_sha256():

 wordlist = str(input(Fore.BLUE+"Enter Wordlist Location : "+Fore.WHITE))
 hash_v = str(input(Fore.BLUE+"Enter Hash value : "+Fore.WHITE))



 if(path.exists(wordlist) == True) :
  passwd_list = open(wordlist).read()
  passwds = passwd_list.splitlines()
  for line in passwds:
   try:
      print(Fore.YELLOW+"[!] CHECK PASSWORD [SHA256] : "+ line.strip())
      hash_ob = hashlib.sha256(line.strip().encode())
      hashed_pass = hash_ob.hexdigest()
      if hashed_pass == hash_v:
        print(Fore.GREEN+"[+] PASSWORD FOUND [SHA256] : " + line.strip())
        break
   except Exception as e :
      print(e)
      pass

  print(Fore.RED+"------------------END of HashCracker------------------")

 else :
  print(Fore.RED+"[-] INVALID FILE, Please try again ...")  

def algo_md4():

 wordlist = str(input(Fore.BLUE+"Enter Wordlist Location : "+Fore.WHITE))
 hash_v = str(input(Fore.BLUE+"Enter Hash value : "+Fore.WHITE))



 if(path.exists(wordlist) == True) :
  passwd_list = open(wordlist).read()
  passwds = passwd_list.splitlines()
  for line in passwds:
   try:
      print(Fore.YELLOW+"[!] CHECK PASSWORD [MD4] : "+ line.strip())
      hash_ob = hashlib.md4(line.strip().encode())
      hashed_pass = hash_ob.hexdigest()
      if hashed_pass == hash_v:
        print(Fore.GREEN+"[+] PASSWORD FOUND [MD4] : " + line.strip())
        break
   except Exception as e :
      print(e)
      pass

  print(Fore.RED+"------------------END of HashCracker------------------")

 else :
  print(Fore.RED+"[-] INVALID FILE, Please try again ...")


def algo_sha512():

 wordlist = str(input(Fore.BLUE+"Enter Wordlist Location : "+Fore.WHITE))
 hash_v = str(input(Fore.BLUE+"Enter Hash value : "+Fore.WHITE))



 if(path.exists(wordlist) == True) :
  passwd_list = open(wordlist).read()
  passwds = passwd_list.splitlines()
  for line in passwds:
   try:
      print(Fore.YELLOW+"[!] CHECK PASSWORD [SHA512] : "+ line.strip())
      hash_ob = hashlib.sha512(line.strip().encode())
      hashed_pass = hash_ob.hexdigest()
      if hashed_pass == hash_v:
        print(Fore.GREEN+"[+] PASSWORD FOUND [SHA512] : " + line.strip())
        break
   except Exception as e :
      print(e)
      pass

  print(Fore.RED+"------------------END of HashCracker------------------")

 else :
  print(Fore.RED+"[-] INVALID FILE, Please try again ...")