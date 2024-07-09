l = []
k = ""
x = input("number: ")
if x.isdigit():
    for y in x:
        l.append(y)          
while len(l)!=0 :    
    m = min(l)
    k += m
    i = l.index(str(m))
    l.pop(i)
print(k)    
    