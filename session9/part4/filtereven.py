a = [5,1,8,92,-1,80]
print(*a,sep=", ")
b = []
for i in a:
    if i%2==0:
        b.append(i)

print(*b,sep=", ")
