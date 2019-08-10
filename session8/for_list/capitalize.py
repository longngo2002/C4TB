a = ['one', 'two','three']
b = input("Them vao danh sach:")
a.append(b)
l = len(a)
for i,a in enumerate(a):
    print(i,'.',a.capitalize())