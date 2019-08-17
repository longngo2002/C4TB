a=[45,67,56,78,53]
print("Hign score :")
a.sort(reverse = True)
for i,a in enumerate(a):
    print(i+1,'.',a)
c=[45,67,56,78,53]
b = int(input("Enter your new highscore:"))
c.append(b)
c.sort(reverse = True)
for i,c in enumerate(c):
    print(i+1,'.',c)
e=[45,67,56,78,53]
d = int(input("Enter your new highscore :"))
e.append(d)
e.sort(reverse = True)
print("New high scores:")
for i in range(5):
    print(i+1,e[i])