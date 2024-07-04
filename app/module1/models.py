# app/module1/models.py
from datetime import datetime
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
    user = db.users.find_one({"username": username})
    if not user:
        return False

    user_id = user['_id']

    db.events.update_many({}, {"$pull": {"attendees": user_id}})

    db.events.delete_many({"creator": user_id})

    result = db.users.delete_one({"_id": user_id})
    return result.deleted_count > 0

def is_user_valid(user_id):
    if not ObjectId.is_valid(user_id):
        return False
    return True

def get_dashboard_data(db):
    total_events = db.events.count_documents({})
    total_users = db.users.count_documents({})
    upcoming_events = db.events.count_documents({"timestamp": {"$gte": datetime.now()}})
    past_events = db.events.count_documents({"timestamp": {"$lt": datetime.now()}})

    user_activity = db.events.aggregate([
        {"$unwind": "$attendees"},
        {"$group": {
            "_id": "$attendees",
            "count": {"$sum": 1}
        }},
        {"$group": {
            "_id": None,
            "average": {"$avg": "$count"}
        }}
    ])
    average_events_per_user = list(user_activity)[0]['average'] if user_activity else 0

    return {
        "totalEvents": total_events,
        "totalUsers": total_users,
        "upcomingEvents": upcoming_events,
        "pastEvents": past_events,
        "averageEventsPerUser": average_events_per_user
    }