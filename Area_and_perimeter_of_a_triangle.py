import math
x=0
m1 = list(map(float,input("m1: ").split(",")))
m2 = list(map(float,input("m2: ").split(",")))
m3 = list(map(float,input("m3: ").split(",")))
z1 = math.sqrt(((m1[0]-m2[0])**2)+((m1[1]-m2[1])**2))
z2 = math.sqrt(((m1[0]-m3[0])**2)+((m1[1]-m3[1])**2))
z3 = math.sqrt(((m2[0]-m3[0])**2)+((m2[1]-m3[1])**2))
p = round(z1+z2+z3,2)
np = p/2
if m1[0]==m2[0]==m3[0] or m1[1]==m2[1]==m3[1] or m1==m2 or m2==m3 or m1==m3 or m1[1]-m1[0]==m2[1]-m2[0]==m3[1]-m3[0]  :
    print("This is not a triangle shape")
    x+=1
if x==0:
    a = round(math.sqrt((np*(np-z1)*(np-z2)*(np-z3))),2)
    print("triangle perimeter =",p)
    print("triangle area =",a)

