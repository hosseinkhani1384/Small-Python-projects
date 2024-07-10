from colorama import Fore
a = int(input(Fore.RED+"aval: "+Fore.RESET))
r = int(input(Fore.RED+"akhar: "+Fore.RESET))
z = 0
x = input(Fore.RED+"number: "+Fore.RESET)
for i in range(a,r+1):
    if str(i).count(x)>=1:
        print(Fore.BLUE+str(i)+Fore.RESET)
        z += 1
print(Fore.GREEN+str("all numbers = ")+Fore.YELLOW+str(z)+Fore.RESET)        