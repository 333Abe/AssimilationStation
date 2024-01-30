from flask import Flask
from db import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)