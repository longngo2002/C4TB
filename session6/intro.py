while True:
    a = input("Nhap 1 so:")
    print(a)
    if a.isdigit():
        print("A number.")
        break
    else:
        print("Not a number.")

print(2019 - int(a))