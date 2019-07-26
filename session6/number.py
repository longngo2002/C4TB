while True:
    num = input("Nhap 1 so:")
    count = len(num)

    if num.isalpha():
        print("Phai nhap so.")
    else:
        print("So vua nhap co so chu so la:",count)
        break
    