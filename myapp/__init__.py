from flask import Flask
from myapp.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from myapp import routes,models