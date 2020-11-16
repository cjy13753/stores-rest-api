from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic') # By using 'lazy=dynamic', we can save computing resources because we no longer create objects for every item row that matches the store id.

    def __init__(self, name):
        self.name = name
    
    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]} # when using lazy='dynamic', don't forget to add '.all()' method to 'self.items'

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM __tablename__ WHERE name=name LIMIT 1

    def save_to_db(self):
        db.session.add(self) #save and update as well
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    

    