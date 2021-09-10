import pyfiglet
import sys
from colorama import Fore
from algos import algo_md4,algo_md5,algo_sha256,algo_sha512
from intro import intro_hashcracker

intro_hashcracker() #introduction function

print(Fore.YELLOW+"-----------The available algorithms---------------- ")
print(Fore.BLUE+"1- md5")
print(Fore.BLUE+"2- md4")
print(Fore.BLUE+"3- SHA256")
print(Fore.BLUE+"4- SHA512")

choice = str(input(Fore.CYAN+"Please Enter your choice [1/2/3/4]: "+Fore.WHITE))


if( choice == '1'):
     algo_md5()
elif ( choice =='2'):
     algo_md4()
elif( choice == '3'):
     algo_sha256()
elif( choice == '4'):
     algo_sha512()
else:
 print(Fore.RED+"[-] Your choice is INVALID, Please Try again ...")
