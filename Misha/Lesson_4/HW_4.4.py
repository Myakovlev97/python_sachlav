a = map(int, input("Enter 3 values: ").split())
b = list(a)
print(b[0] == b[1] or b[0] == b[2] or b[2] == b[1])