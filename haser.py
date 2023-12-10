import requests , os
from colorama import Fore , init
os.system('cls')
clear = lambda: os.system('cls' or "clear")
init()
passwordlist = open('10-million-password-list-top-1000000.txt','r')
passwordhash = open('password-hash.txt','a')
conter=1000001
for i in passwordlist:
    conter-=1
    str1conter=str(conter)
    req = requests.post('http://www.md5.cz/getmd5.php',data={'what': str(i)}).text
    slais1 = req[:32].replace("\n","")
    print(Fore.WHITE+i.replace("\n","")+Fore.RED+" ====> "+Fore.GREEN+slais1+"      "+Fore.LIGHTMAGENTA_EX+(str1conter))
    passwordhash.write(i.replace("\n","")+" ====> "+slais1+'\n')
passwordlist,passwordhash.close()
print('\a')
