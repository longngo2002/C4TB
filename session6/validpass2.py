while True:
     a = input("Nhap mat khau:")
     if a.isalpha():
         print("Khong co chu so.")
     elif len(a) < 8:
         print("Khong du dai.")
     else:
         break