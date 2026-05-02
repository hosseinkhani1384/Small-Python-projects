l1 = list()
l2 = list()
while True:
    x = input("Product name: ")
    if x==" " :
        break
    y = input("price: ")
    l1.append(x)
    l2.append(y)
print(l1)
d = input("product name: ")
s = (l1.index(d))
print(str(l2[s])+" toman")

