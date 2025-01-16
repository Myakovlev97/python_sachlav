a = input("Enter a first word: ")
b = input("Enter a second word: ")
print("YES") if a == b[::-1] else print("NO")
