users = []
users.extend(["Kevin", "Bob", "Alice"])
print(users)
del users[1]
print(users)
rev_users = list(reversed(users))
print(rev_users)
users.insert(1, "Melody")
print(users)
users.extend(["Andy", "Wanda", "Jim"])
print(users)
center_users = users[2:4]
print(center_users)
# cut = users.pop(2)
# cut2 = users.pop(2)
# print(f"['{cut}'], ['{cut2}']")