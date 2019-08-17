a = ['ST','BĐ','BLT','CG','ĐĐ','HBT']
b = [150300,247100,333300,266800,420900,318000]
gtln=b[0]
gtnn=b[0]
for i in b:
    if i > gtln:
        gtln=i
    elif i < gtnn:
        gtnn=i
print("Dan so cao nhat la:",gtln)
print("Dan so thap nhat la:",gtnn)