a = ['blue','red','yellow']
print(*a,sep=", ")
b = input("Item to delete:")
if b.isalpha() :
    a.remove(b)
else:
    c = int(b)
    a.pop(c-1)
print(*a,sep=", ")