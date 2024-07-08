while True :  
    a = int(input("saat kari: "))
    if 0<a<=140 :
        print(a*30000)
        continue
    elif 190>a>140 :
        print(((a-140)*50000)+(140*30000)) 
        continue
    else :
        print("az 0 ta 190 entechab konid")    
