from user import User

external_data = {
    "id": "123",
    "name": "John",
    "signup_ts": "2017-06-21 12:22",
    "friends": [1, "2", b"3"],
}

user = User(**external_data)

print(user)
print(user.id)
