a = [5,1,8,92,-1,80]
print(*a,sep=", ")
b = input("Enter a number:")
if b in a:
    c = 0
    for i in a:
        if i == b:
            print("Found, position", c+1)
            break
        else:
            c = c + 1
else:
    print("Not in list.")