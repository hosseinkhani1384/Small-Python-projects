l = list(map(float,input("Numbers: ").split(",")))
l1 = []
l2 = []
for i in l:
    x = l.count(i)
    if l1.count(x)>=1:
        continue
    l1.append(x)
m = max(l1) 
for i in l:
    if l.count(i)==m and l2.count(i)==0:
        l2.append(i)
print(l2)        