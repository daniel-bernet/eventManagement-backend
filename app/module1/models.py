# app/module1/models.py
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId

def create_user(db, username, password):
    if db.users.find_one({"username": username}):
        return None

    password_hash = generate_password_hash(password)
    user_data = {"username": username, "password": password_hash}
    result = db.users.insert_one(user_data)
    return str(result.inserted_id)

def validate_user(db, username, password):
    user = db.users.find_one({"username": username})
    if user and check_password_hash(user['password'], password):
        return user
    return None

def delete_user(db, username):
    result = db.users.delete_one({"username": username})
    return result.deleted_count > 0

def is_user_valid(user_id):
    if not ObjectId.is_valid(user_id):
        return False
    return True