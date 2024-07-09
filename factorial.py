l = [1]
i = 1
j = 1
x = int(input("number foct: "))
while  max(l)<x:
    i += 1
    for d in range(1,i+1):
        j *= d
    l.append(j)
    j = 1
if x in l:
    print("True")
else :
    print("False")        