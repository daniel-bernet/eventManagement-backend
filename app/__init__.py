# app/__init__.py
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Setup MongoDB connection
    client = MongoClient(os.getenv('MONGO_URI'))
    app.db = client.your_database_name

    # Import blueprints
    from .module1.routes import mod1
    app.register_blueprint(mod1)

    return app
