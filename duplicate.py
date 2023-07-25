li=[2,6,4,3,2,4,6,8,9,10,191,19,19]
dup=[]
for i in range(0,len(li)-1):
    if li[i] not in dup:
        dup.append(li[i])
print(dup)