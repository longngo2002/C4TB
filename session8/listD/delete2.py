a = ['one', 'two','three']
print(*a)
b = 'LOL'
if b in a:
    a.remove('LOL')
    print(*a)
else:
    print("Phan tu khong co trong list.")