import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from resources.user import UserRegister 
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # it only turns off flask_sqlalchemy modification tracker because sqlalchemy modification(the original version) is better.
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request # before any request to the app, this function below creates all the tables. It only creates tables that it sees imported. Make sure to import the Models.
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # /auth (new endpoint)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
