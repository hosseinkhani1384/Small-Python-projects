import random
r = random.randint(1,100)
while True :
    n = int(input("number: "))
    if n>r and 100>n>0 :
        print("kamtar")
        continue
    elif n<r and 100>n>0  :
        print("bishtar")
        continue
    elif n==r and 100>n>0  : 
        print("afarin dorost gofti")
        a = input("aya mikhahi edame bade ba bale ya na javab bedeh: ")
        if a.endswith("bale") :
           r = random.randint(1,100)
           continue 
        elif a.endswith("na") :
            break
        else :
            break
    else :
        print("adad 1 ta 100 entekhab konid") 

