# app/__init__.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate  
from datetime import datetime

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Specify the login view endpoint
login_manager.login_message_category = 'info'  # Optional: style for the flash message

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    
    db.init_app(app)
    migrate.init_app(app, db) 
    login_manager.init_app(app)
    
    # Import blueprints
    from app.routes.main import main
    from app.routes.blog import blog
    from app.routes.portfolio import portfolio
    from app.routes.auth import auth  # Add this import
    
    # Register blueprints
    from app.routes import main, blog, portfolio
    app.register_blueprint(main)
    app.register_blueprint(blog, url_prefix='/blog')
    app.register_blueprint(portfolio, url_prefix='/portfolio')
    
    # Register auth blueprint
    from app.routes.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
    
    # Add global context processor for current year
    @app.context_processor
    def inject_year():
        return {'current_year': datetime.now().year}
    
    return app
