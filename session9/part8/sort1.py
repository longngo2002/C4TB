a=[45,67,56,78]
print("Hign score :")
a.sort(reverse = True)
for i,a in enumerate(a):
    print(i+1,'.',a)
c=[45,67,56,78]
b=int(input("Enter your new highscore:"))
c.append(b)
c.sort(reverse = True)
for i,c in enumerate(c):
     print(i+1,'.',c)