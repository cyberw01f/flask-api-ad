from flask_restful import Resource, reqparse
# from flask_jwt import jwt_required
from models.store import StoreModel


class Store(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('price',
    #                     type=float,
    #                     required=True,
    #                     help="This field cannot be blank"
    #                     )
    # parser.add_argument('store_id',
    #                     type=int,
    #                     required=True,
    #                     help="Every item needs a store id"
    #                     )

    # @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A Store with name {} already exists".format(name)}, 400
        # data = store.parser.parse_args()
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occured inserting the item"}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'message': 'Store deleted.'}
        return {'message': 'Store not found.'}, 404


class StoreList(Resource):
    def get(self):
        return {'store': [store.json() for store in StoreModel.query.all()]}