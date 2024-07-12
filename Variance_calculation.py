l = list(map(int,input("Numbers: ").split(",")))
f = len(l)
x = 0
for i in l:
    x+=i
a = x/f  
x = 0
for i in l:
    x+=(i-a)**2
v = x/f
print("varianc:",v)    