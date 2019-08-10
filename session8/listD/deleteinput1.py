a = ['one', 'two','three']
print(*a)
b = int(input("Nhap vi tri muon xoa:"))
a.pop(b-1)
print(*a)