def tashkhis(x):
    a1 = 0
    a2 = 0
    a3 = 0
    for i in x:
        if i.isdigit():
            a1 += 1
        if i.isalpha():
            a2 += 1
        else :
            a3 += 1
    print(f"algha = {a2}    digit = {a1}    else = {a3}")        

