def dars(x) :
    d = 0
    w = 0
    while True :
        c = float(input("nomre dars: "))
        if c==0 :
            break
        if c<10:
            continue
        x = float(input("zarib: "))
        d += c*x
        w += x
    return d/w
print(dars(1))
    
