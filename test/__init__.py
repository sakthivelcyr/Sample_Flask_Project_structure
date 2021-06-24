from flask import Flask
from .rotes import app_bp

app = Flask(__name__)
app.register_blueprint(app_bp)