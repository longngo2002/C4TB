a = ['ST','BĐ','BLT','CG','ĐĐ','HBT']
b = [150300,247100,333300,266800,420900,318000]
c=0
d=0
gtln=b[0]
gtnn=b[0]
for i in b:
    if i > gtln:
        gtln=i
    elif i < gtnn:
        gtnn=i
for i in b:
    if i == gtln:
        print("Quan co dan so cao nhat la:",a[c])
    else:
        c=c+1
    if i == gtnn:
        print("Quan co dan so thap nhat la:",a[d])
    else:
        d=d+1

