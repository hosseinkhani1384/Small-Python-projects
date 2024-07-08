l = []
x = int(input("Enter: "))
for i in range(1,x):
    y = 2**i
    l.append(y)
    if x<y:
        break
s = len(l)
a1 = l[s-1] - x
a2 = x - l[s-2]   
if x+10>=l[s-1] or x-10<=l[s-2] :
    if a1<a2  :
        print(l[s-1],s)
    if a1>a2 :
        print(l[s-2],s-1)
    if a1==a2 :
        print(l[s-1],s)
        print(l[s-2],s-1)
else :
    print("None")

