from colorama import Fore
x1 = list(map(int,input(Fore.GREEN+"The first number is the number of members in the row and the second number is for rows: "+Fore.RESET).split("*")))
l1 = []
q1 = 1
a1 = 0
while 1:
    x2 = list(map(int,input(Fore.BLUE+f"row {q1} : "+Fore.RESET).split(",")))
    if len(x2)!=x1[0]:
        print(Fore.RED+"Please enter the number of rows correctly"+Fore.RESET)
        continue
    q1+=1
    l1 = l1 + x2
    if len(l1)==x1[0]*x1[1]:
        break
for j in range(0,x1[0]):
    i = x1[0]    
    k=0 
    for m in range(x1[1]-1):  
        if l1[j+k]<l1[j+i]:
            a1+=1
        i+=x1[0]    
        k+=x1[0]          
a2 = (x1[1]-1)*x1[0] 
if a1==a2:
    print(Fore.GREEN+"True"+Fore.RESET) 
if a1!=a2:
    print(Fore.RED+"False"+Fore.RESET)          