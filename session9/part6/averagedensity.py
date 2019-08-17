a = ['ST','BĐ','BLT','CG','ĐĐ','HBT']
b = [150300,247100,333300,266800,420900,318000]
c = [117.43,9.224,43.35,12.04,9.96,10.09]
d = []
for i,g in enumerate(c):
    d.append(round(b[i]/g, 2))
print(*d,sep=", ")
e = sum(d)/len(a)
print("Mat do dan so trung binh:",round(e,2))