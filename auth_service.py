import json


def register(username, email, password):
    user_obj = {
        'username': username,
        'email': email,
        'password': password
    }

    user_json = json.dumps(user_obj)
    with open('./db/users.txt', 'r+') as file:
        for user_line in file:
            existing_user = json.loads(user_line.strip())
        if existing_user['username'] == username:
            return False

