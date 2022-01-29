from api import db

class Item(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(150), nullable=False)


class Book(Item):
    year = db.Column(db.Integer, nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    author = db.Column(db.String(20), nullable=False)
    publisher = db.Column(db.String(20), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "year": self.year,
            "price": self.price,
            "pages": self.pages,
            "author": self.author,
            "publisher": self.publisher,
            "description": self.description,
        }

    # def __repr__(self) -> str:
    #     return f"Programmer({self.id}, {self.name})"