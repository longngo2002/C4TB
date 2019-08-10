a = ['one','two','three']
print(a)
b = input("Noi dung them : ")
c = b.split(',')
for i in c:
    c = a.append(i)
print(a)