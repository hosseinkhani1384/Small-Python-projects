l4 = []
l3 = []
l2 = []
l1 = list(map(int,input("Enter: ").split(",")))
q = len(l1)  
for i in l1:
    for j in range(1,i+1):
        if i%j==0:
            l2.append(j)  
            if l3.count(j)==0:
                l3.append(j)
for x in l3:
    if l2.count(x)==q:
        l4.append(x)
print(max(l4))        