from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
import requests
import json


class Item(Resource):
    parser = reqparse.RequestParser()
    # parser.add_argument('price',
    #                     type=float,
    #                     required=True,
    #                     help="This field cannot be left blank!"
    #                     )
    # parser.add_argument('store_id',
    #                     type=int,
    #                     required=True,
    #                     help="This field cannot be left blank!"
    #                     )
    parser.add_argument('country',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    # parser.add_argument('category',
    #                     type=str,
    #                     required=True,
    #                     help="Please specify the category of the news."
    #                     )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_category(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    @jwt_required()
    def post(self, name):
        # if ItemModel.find_by_name(name):
        #     return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()

        url = ('https://newsapi.org/v2/top-headlines?category=' + name + '&country=' + data['country'] + '&apiKey=8b6adf725c5746738a10b64ad98c8445')

        response = requests.get(url)
        json_data = response.text
        parsed = json.loads(json_data)

        if parsed['status'] != 'ok':
            return {'message': "An error occurred when retrieving the data."}, 500

        output = parsed['articles']
        stop_loop = True
        for i in output:
            for k,v in i.items():
                if not stop_loop:
                    continue
                elif k == 'title':
                    if ItemModel.find_by_title(v):
                        stop_loop = False
                    else:
                        title = v
                        stop_loop = True
                elif k == 'content':
                    content = v
            if stop_loop:
                break

        item = ItemModel(name, data['country'], title, content)

        # item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_title(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404

    # def put(self, name):
    #     data = Item.parser.parse_args()
    #
    #     item = ItemModel.find_by_name(name)
    #
    #     if item:
    #         item.price = data['price']
    #     else:
    #         item = ItemModel(name, **data)
    #
    #     item.save_to_db()
    #
    #     return item.json()

@jwt_required()
class ItemList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
