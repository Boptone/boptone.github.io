import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add project root to path
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boptone.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Import models
from src.models.user import User
from src.models.conversation import Conversation, UserProfile

# Create tables
with app.app_context():
    db.create_all()
    print("✅ Database tables created successfully!")
    print("✅ Conversation table created")
    print("✅ UserProfile table created")
    print("✅ All tables are ready for use")
