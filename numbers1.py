def number(x):
    y = x+1
    k = ""
    for i in range(10):
        k += f"{y}"
        y += x
        if i!=9:
            k += "," 
    print(k)
