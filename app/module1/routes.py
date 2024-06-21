# app/module1/routes.py
from flask import Blueprint, request, jsonify, session, current_app
from .models import create_user, validate_user, delete_user

mod1 = Blueprint('auth', __name__)

@mod1.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    user_id = create_user(current_app.db, username, password)
    if user_id is None:
        return jsonify({"error": "Username already exists"}), 409
    return jsonify({"message": "User created successfully", "username": username, "user_id": user_id}), 201

@mod1.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    user = validate_user(current_app.db, username, password)
    if user:
        session['username'] = username
        session['user_id'] = str(user['_id'])
        return jsonify({"message": "Login successful", "username": username, "user_id": str(user['_id'])}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@mod1.route('/delete', methods=['DELETE'])
def delete_account():
    if 'username' in session:
        username = session['username']
        if delete_user(current_app.db, username):
            return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"error": "Failed to delete user or not logged in"}), 400
