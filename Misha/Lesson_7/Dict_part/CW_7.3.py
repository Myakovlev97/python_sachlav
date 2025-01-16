import pprint

user = {
    "id": 4170,
    "uid": "435hbjh34b53jh4b34",
    "password": "ShjSHJhc1j5",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@gmail.com",
    "gender": "Non-binary",
    "phone_number": "+674 234.257.234.2996",
    "social_insurance_number": "73823742",
    "date_of_birth": "1993-08-17"
}
a = user.pop("password")
b = user.pop("last_name")
user.update({"secret": a, "surname": b})
pprint.pprint(user)