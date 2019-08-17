a = ['5','1','8','92','-1','80']
print(*a,sep=", ")
c = []
for i in a:
    b = int(i)
    c.append(b)
print(sum(c))