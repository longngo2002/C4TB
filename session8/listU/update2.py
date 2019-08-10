a = ['one', 'two','three']
print(*a)
b = input('Them vao danh sach: ')
a.append(b)
print(*a)
a[0] = input('Phim yeu thich:')
print(*a)
a[-1] = input('Sach yeu thich:')
print(*a)