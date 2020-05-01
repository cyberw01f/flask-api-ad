import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres://jvqtmuqvfijyqu:ce1216a08e8a13666b5f6f2abb06688a7ce000240af3e2af8698a0b05299fa38@ec2-54-88-130-244.compute-1.amazonaws.com:5432/dd9npm4nnisl7j')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'abhineet'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    app.run(port=5000)
