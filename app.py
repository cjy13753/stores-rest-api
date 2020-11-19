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
app.secret_key = 'jose' # # This is for authentication by jwt. When it comes to production, this key must be more complicated and hidden for the public to be unable to see it.
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth (new endpoint)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
