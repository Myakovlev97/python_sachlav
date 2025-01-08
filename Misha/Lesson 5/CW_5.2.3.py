t = input("enter a word, at least 6 characters: ")
# t = t.replace(t, t.lower())
# t = t.replace(t[:3], str.upper(t[:3]))
# t = t.replace(t[-3:], str.upper(t[-3:]))
# print(t)

a = t[:3].upper() + t[3:-3].lower() + t[-3:].upper()
print(a)