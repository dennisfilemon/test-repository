from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')
    # category = db.Column(db.String(80))
    # country = db.Column(db.String(80))
    # title = db.Column(db.String(120))
    # content = db.Column(db.Text)


    def __init__(self, name, price, store_id):
    # def __init__(self, category, country, title, content):
        self.name = name
        self.price = price
        self.store_id = store_id
        # self.category = category
        # self.country = country
        # self.title = title
        # self.content = content

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
