a = ['blue','red','yellow']
print(*a,sep=", ")
b = input("Enter a new color:")
a.append(b)
print(*a,sep=", ")