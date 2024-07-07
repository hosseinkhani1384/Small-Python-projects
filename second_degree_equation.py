import math
print("ax2 + bx + c = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
y = (b**2)-(4*a*c)
if y>0:
    print("x1 =",(-b+math.sqrt(y))/(2*a))
    print("x2 =",(-b-math.sqrt(y))/(2*a))
elif y==0:
    print("x =",-b/(2*a))   
elif y<0:
    print("The equation has no answer")  