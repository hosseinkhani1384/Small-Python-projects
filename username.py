while True :
    a = input("name: ")
    b = input("last name: ")
    if a.isalpha()==True and b.isalpha()==True:
        print("welcome {} {}".format(a,b)) 
        break
    else :
         print("please enter your name and last name correctly")    