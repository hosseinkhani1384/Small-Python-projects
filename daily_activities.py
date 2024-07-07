from colorama import Fore
def prn():
    print(Fore.YELLOW+"1.add    2.remove   3.edit   4.ed.edit "+Fore.RESET)
def prn2():
    for i,p in enumerate(l,1):
            print(Fore.RED+f"{i}. {p}"+Fore.RESET)
l = []
while 1:
    prn2()
    prn()
    x = input("number: " )
    if x =="1":
        d = input("Enter: ")
        l.append(d)
    if x=="2":
        if len(l)==0:
             continue
        y = int(input("select the number of the daily task you want to remove: "))
        l.pop(y-1)
    if x=="3":
        if len(l)==0:
             continue
        s = int(input("select the number of the daily task you want to edit: "))
        l[(s-1)] = input("Enter: ") 
        continue
    if x=="4":
        o = int(input("number change: "))
        o1 = input("Enter: ")
        l.insert(o-1,o1)
