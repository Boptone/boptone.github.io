#!/usr/bin/env python3
"""
Initialize the database with proper tables
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.models.user import db, User
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boptone.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    return app

def init_database():
    app = create_app()
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database tables created successfully!")
        
        # Print the schema to verify
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"Created tables: {tables}")
        
        if 'user' in tables:
            columns = inspector.get_columns('user')
            print("User table columns:")
            for col in columns:
                print(f"  - {col['name']}: {col['type']}")

if __name__ == '__main__':
    init_database()
