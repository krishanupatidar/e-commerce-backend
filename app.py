from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# Import Blueprints for different functionalities
from routes.auth_routes import auth_bp
from routes.product_routes import product_bp
from routes.cart_routes import cart_bp

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration for JWT token
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "your_secret_key")  # Use the JWT secret key from environment

# Initialize the JWT manager for creating tokens
jwt = JWTManager(app)

# Register Blueprints for different functionalities
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(product_bp, url_prefix='/product')
app.register_blueprint(cart_bp, url_prefix='/cart')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
