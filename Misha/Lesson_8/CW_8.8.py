a = int(input("Enter a first num: "))
b = int(input("Enter a second num: "))
c = int(input("Enter a third num: "))
if a == b == c:
    print("3")
elif a == b != c or a == c != b or b == c != a:
    print("2")
else:
    print("1")