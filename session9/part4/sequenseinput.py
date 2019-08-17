a = ['5','1','8','92','-1','80']
print(*a,sep=", ")
b = []
c = []
for i in a:
    c.append(int(i))
for i in c:
    if i%2==0:
        b.append(i)

print(*b,sep=", ")