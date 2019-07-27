import random
sign = random.randint(1, 4)
point = 0
while True:
    if sign == 1 : #plus
        a = random.randint(0, 99)
        b = random.randint(0, 99)
        c = a+b
        result = random.randint(0,1)
        if result == 0: #true
            print(a,"+",b,"=",c)
            answer = input("true or false?")
            if answer == "true":
                point = point + 1
            elif answer == "false":
                print("Gameover.")
                break
        else: #false
            d = random.randint(0, 99)
            print(a,"+",b,"=",d)
            answer = input("true or false?")
            if answer == "true":
                print("Gameover.")
                break
            elif answer == "false":
                point = point + 1

    elif sign == 2: #minus
        a = random.randint(0, 99)
        b = random.randint(0, 99)
        c = a-b
        result = random.randint(0,1)
        if result == 0: #true
            print(a,"-",b,"=",c)
            answer = input("true or false?")
            if answer == "true":
                point = point + 1
            elif answer == "false":
                print("Gameover.")
                break
        else: #false
            d = random.randint(0, 99)
            print(a,"-",b,"=",d)
            answer = input("true or false?")
            if answer == "true":
                print("Gameover.")
                break
            elif answer == "false":
                point = point + 1

    elif sign == 3: #multiply
        a = random.randint(0, 99)
        b = random.randint(0, 99)
        c = a*b
        result = random.randint(0,1)
        if result == 0: #true
            print(a,"*",b,"=",c)
            answer = input("true or false?")
            if answer == "true":
                point = point + 1
            elif answer == "false":
                print("Gameover.")
                break
        else: #false
            d = random.randint(0, 99)
            print(a,"*",b,"=",d)
            answer = input("true or false?")
            if answer == "true":
                print("Gameover.")
                break
            elif answer == "false":
                point = point + 1

    else: #divine
        a = random.randint(0, 99)
        b = random.randint(0, 99)
        c = a/b
        result = random.randint(0,1)
        if result == 0: #true
            print(a,":",b,"=",c)
            answer = input("true or false?")
            if answer == "true":
                point = point + 1
            elif answer == "false":
                print("Gameover.")
                break
        else: #false
            d = random.randint(0, 99)
            print(a,":",b,"=",d)
            answer = input("true or false?")
            if answer == "true":
                print("Gameover.")
                break
            elif answer == "false":
                point = point + 1
print("So diem cua ban la:",point)