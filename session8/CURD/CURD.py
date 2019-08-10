while True:
    print("CRUD")
    a = ["Creat","Read","Update","Delete"]
    for i,a in enumerate(a):
        print(i,".",a)
    print()
    b =int(input("Chon thao tac: "))
    danhsach = ["one","two","three","four"]
    if b == 0:
        c = input("Noi dung them vao:")
        danhsach.append(c)
        print(danhsach)
        break
    elif b == 1:
        d = len(danhsach)
        if d == 0:
            print("khong co phan tu. ")
        else:
            for danhsach in danhsach:
                print(danhsach)
            break
    elif b == 2:
        print(danhsach)
        e = int(input("Vi tri muon cap nhat: "))
        f = input("Noi dung: ")
        danhsach[e]=f
        print(danhsach)
        break
    elif b == 3:
        print(danhsach)
        g = int(input("Vi tri muon xoa: "))
        danhsach.pop(g)
        print(danhsach)
        break