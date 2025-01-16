password = input("Enter your password: ")
if len(password) < 7:
    print("Short")
else:
    password2 = input("Confirm your password: ")
    if password == password2:
        print("OK")
    else:
        print("Difference")