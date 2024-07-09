g = 0
i = 0
x = int(input("number: "))
y = int(input("tavan: "))
while y**i<=x:
    i+=1
    g+=x//(y**i)
print(g)    
