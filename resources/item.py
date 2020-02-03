from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel, ItemModelSchema
import requests
import json

items_schema = ItemModelSchema(many=True)
item_schema = ItemModelSchema()

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('country',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    @jwt_required()
    def get(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_category(name, data['country'])
        if item.count() > 0:
            return items_schema.dump(item)
        return {'message': 'Item not found'}, 404

    @jwt_required()
    def post(self, name):

        data = Item.parser.parse_args()

        url = ('https://newsapi.org/v2/top-headlines?category=' + name + '&country=' + data['country'] + '&apiKey=8b6adf725c5746738a10b64ad98c8445')

        response = requests.get(url)
        json_data = response.text
        parsed = json.loads(json_data)

        if parsed['status'] != 'ok':
            return {'message': "An error occurred when retrieving the data."}, 500

        output = parsed['articles']
        for i in output:
            if not ItemModel.find_by_title(i['title']):
                title = i['title']
                content = i['content']
                break

        if not title:
            return {"message": "No more news, please try again later."}, 500

        item = ItemModel(name, data['country'], title, content)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item_schema.dump(item), 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_id(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.', 'data': item_schema.dump(item)}, 201
        return {'message': 'Item not found.'}, 404


class ItemList(Resource):
    def get(self):
        items = ItemModel.query.all()
        return items_schema.dump(items)
