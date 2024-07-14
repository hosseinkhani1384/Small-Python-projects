l = []
a1 = 1
a2 = 0
x = input("Number: ")
f = len(x)
for i in range(0,f):
    l.append(int(x[i]))
while 1:
    a2+=1
    for i in l:
        a1*=i
    l = []    
    if 0<int(a1)<9:
        break
    else :
        a1 = str(a1)
        k = len(a1)
        for j in range(0,k):
            l.append(int(a1[j])) 
        a1 = 1       
print(a2)              
