a = int(input("Enter a first num: "))
b = int(input("Enter a second num: "))
if a < b:
    minimum = a
    maximum = b
    print(f"minimum - {minimum}, maximum - {maximum}")
elif b < a:
    minimum = b
    maximum = a
    print(f"minimum - {minimum}, maximum - {maximum}")
else: print("The values are equal")