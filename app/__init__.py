from flask import Flask
from flask_mail import Mail
from .config import Config

app = Flask(__name__)  # Define the app instance
app.config.from_object(Config)

mail = Mail(app)  # Initialize Flask-Mail

from app import views  # Import views after app is defined

