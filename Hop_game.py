from colorama import Fore
s = int(input("fasele: "))
x = 1
while 1:
    if x%s!=0:
        print(x)
    if x%s==0:
        print(Fore.RED+"hoop"+Fore.RESET)
    y = input(Fore.LIGHTBLUE_EX+"number: "+Fore.RESET)
    if y.isdigit():
        k = int(y)
        if k!=x+1:
            print("hahah I win")
            break
        if (x+1)%s==0:
            if y!="hoop":
                print("hahah I win")
                break
    if y.isdigit()==False:
        if (x+1)%s==0:
            if y!="hoop":
                print("hahah I win")
                break  
        if (x+1)%s!=0: 
            if y!=x+1:
                print("hahah I win")
                break      
    x += 2        