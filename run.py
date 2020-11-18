from app import app
from db import db

db.init_app(app)


@app.before_first_request # before any request to the app, this function below creates all the tables. It only creates tables that it sees imported. Make sure to import the Models.
def create_tables():
    db.create_all()