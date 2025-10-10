import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add the project root to the path
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, send_from_directory
from flask_cors import CORS
from src.models.user import db
from src.routes.user import user_bp
from src.routes.stripe_routes import stripe_bp
from src.routes.auth_routes import auth_bp
from src.routes.ai_routes import ai_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'src/static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Enable CORS for frontend-backend communication
CORS(app)

app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(stripe_bp, url_prefix='/api/stripe')
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(ai_bp, url_prefix='/api/ai')

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'boptone.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
# Database tables are already created via init_new_tables.py

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
