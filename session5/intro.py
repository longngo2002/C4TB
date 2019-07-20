a = int(input("Nam sinh ?"))
b = 2019 - a
print(b)

if b < 10:
    print("Baby")
elif b < 18:
    print("Teenager")
else:
    print("Adult")