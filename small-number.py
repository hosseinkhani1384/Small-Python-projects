l = list(map(int,input("number: ").split(",")))
for k in l:
    l1 = []
    l2 = []
    l3 = [1]
    l4 = []
    a1 = ""
    for j in range(2,k):
        if k%j==0:
            break
    else :
        l4.append(k)   
    if len(l4)==1:
        print(f"{k} = 1 x {k}")  
        continue   
    for i in range(2,k):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l3.append(i)       
    for j in range(2,k):
        if k%j==0:
            l1.append(j)
        if len(l1)==1:
            break
    if len(l1)!=0:    
        l1.append(round(k/l1[0]))   
    if len(l1)!=0: 
        while l1[1] not in l3 : 
            for i in range(2,l1[1]): 
                if l1[1]%i==0:
                    l2.append(i)
                    l1.append(round(l1[1]/i))
                    l1.pop(1)
                if l1[1] in l3:
                    break    
    l4 = l2 + l1
    if 1 in l4:
        l4.pop(l4.index(1))
    l4 = sorted(l4)
    a2 = len(l4)
    for s in l4:
        a1+=f"{str(s)}" 
        if l4.index(s)!=(a2-1):
            a1+=" x " 
    print(f"{k} =",a1) 