a = input("account name:")

while True:
    b = input("password:")
    s = 0
    for i in b:
        s = s+1
    if b.isalpha():
        print("invalid password, must include number.")
    elif b.isdigit():
        print("invalid password, must include alpha.")
    elif s <= 8:
        print("password must have at least 8 characters.")
    else:
        print("valid password")
        break

while True:
    c = input("enter your password again:")
    if b == c :
        break
    else:
        print("incorrect password, try again.")

while True:
    d = input("email:")
    if '@' in d and '.' in d:
        break
    else:
        print("invalid email, must include @ and . ")