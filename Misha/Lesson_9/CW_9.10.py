start = 25
end = 50
for x in range(start, end+1):
    if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
        print(x)