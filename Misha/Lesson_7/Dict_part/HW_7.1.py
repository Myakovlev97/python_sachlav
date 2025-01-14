email = {
    "ashley": "ashley@gmail.com",
    "craig": "craig@gmail.com",
    "elizabeth": "elizabeth@gmail.com"
}
print(email)

del email["craig"]
print(email)

email["dalton"] = "dalton@gmail.com"
print(email)

users = email.keys()
print(users)

email_list = email.values()
print(email_list)

pairs = dict(zip(users, email_list))
print(pairs)