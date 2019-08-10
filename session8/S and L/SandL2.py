import random
a = input("Nhap noi dung : ")
b = list(a)
print(b)
shuffle = random.sample(b,len(b))
print("Jumpled word:")
for i in shuffle:
    print(i.upper())