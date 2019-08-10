import random
a = ["One","Two","Three","Four"]
print(*a)
b = random.choice(a)
c = list(b)
shuffle = random.sample(c,len(c))
print("Jumpled word:")
for i in shuffle:
    print(i)
d = input("Dap an cua ban: ")
if d == b:
    print("Dap an chinh xac.")
elif d != b:
    print("Dap an sai.")