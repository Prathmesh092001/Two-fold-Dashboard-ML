# app.py
from flask import Flask
from flask_cors import CORS
from db_setup import db
from routes import api_bp

app = Flask(__name__)
CORS(app)
app.config.from_object('config.Config')

db.init_app(app)

app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)
