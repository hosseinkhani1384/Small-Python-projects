import random
q = {"1":"sang","2":"kaghaz","3":"gheiche"}
i=0
while True :
    print("............")
    print("point",i)
    print("............")
    print("1:sang")
    print("2:kaghaz")
    print("3:gheiche")
    a = int(input("adad: "))
    x = (random.randint(1,3))
    print(q[str(x)])
    if (a==1 and x==3)or(a==2 and x==1)or (a==3 and x==2) :
        i += 1
        print("win".center(50))
        y=int(input("aya mikhay bazam bazi koni 1=are 0=na: "))
        if y==1 :
            continue
        elif y==0 :
            break   
    elif (a==3 and x==1)or(a==1 and x==2)or (a==2 and x==3)  :
        i -= 1
        print("lose".center(50))
        y=int(input("aya mikhay bazam bazi koni 1=are 0=na: "))
        if y==1 :
            continue
        elif y==0 :
            break
    elif (a==3 and x==3)or(a==2 and x==2)or (a==1 and x==1)  :
        print("draw".center(50))
        y=int(input("aya mikhay bazam bazi koni 1=are 0=na: "))
        if y==1 :
            continue
        elif y==0 :
            break
    else :
        print("adad 1 ta 3 type kon")    
