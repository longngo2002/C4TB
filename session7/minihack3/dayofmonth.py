while True:
    a = int(input("Nhap thang:"))
    if a <= 12: 
        break
if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
    print("Thang co 31 ngay.")
elif a == 4 or a == 6 or a == 9 or a == 11:
    print("Thang co 30 ngay.")
else:
    print("Thang co 28 hoac 29 ngay.")
