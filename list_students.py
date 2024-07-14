l = list()
while True:
    print("1.add   2.remove") 
    x = input("number: ")
    y = input("name: ") 
    if x=="1" :
        l.append(y)
        d = len(l)
        for k,q in zip(range(1,d+1),l) :
            print(str(k)+". "+str(q))
    if x=="2" :
        l.remove(y)
        d = len(l)
        for k,q in zip(range(1,d+1),l) :
            print(str(k)+". "+str(q))    
