# setup_db.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create app instance
app = Flask(__name__)

# Get the absolute path to the project directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Configure the database with absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "app", "site.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create database instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models (add your models here)
# This is just a placeholder - you'll need to import your actual models
# from app.models import User, Project, BlogPost

if __name__ == '__main__':
    # Make sure the app directory exists
    os.makedirs(os.path.join(basedir, "app"), exist_ok=True)
    
    with app.app_context():
        db.create_all()
        print(f"Database created successfully at: {os.path.join(basedir, 'app', 'site.db')}")
