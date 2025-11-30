from pymongo import MongoClient
from flask_bcrypt import Bcrypt

client = MongoClient('mongodb://localhost:27017/')
db = client['adb']
admin_users_collection = db['admin']

bcrypt = Bcrypt()

admin_user = {
    "username": "admin",
    "password": bcrypt.generate_password_hash("admin123").decode('utf-8')
}

admin_users_collection.insert_one(admin_user)
print("Admin user created successfully!")
