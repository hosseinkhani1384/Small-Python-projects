a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
b = a.copy()
b.reverse()
def t(x):
    w = ""
    for y in x:
        if y == " " :
            w += " "
            continue
        index = (a.index(y.lower()))
        if y.isupper():
            w += (b[index].upper())
        else:
            w += (b[index].lower())
    return w
print(t(input("Enter: ")))