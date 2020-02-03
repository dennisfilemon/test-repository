from db import db
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import ModelSchema

ma = Marshmallow()


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80))
    country = db.Column(db.String(80))
    title = db.Column(db.String(120))
    content = db.Column(db.Text)


   def __init__(self, category, country, title, content):
        self.category = category
        self.country = country
        self.title = title
        self.content = content

    @classmethod
    def find_by_category(cls, category, country):
        return cls.query.filter_by(category=category, country=country)

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class ItemModelSchema(ma.ModelSchema):
    class Meta:
        model = ItemModel