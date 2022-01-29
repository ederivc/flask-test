from api import db
from api.models.models import Book
from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from api.helpers.helpers import response, item_not_found_response, generate_id

book = Blueprint('books', __name__)

@book.route("/", methods=["GET"])
def get():
    books = Book.query.all()
    
    books_list = [book.serialize() for book in books]

    return response(books_list, 200)


@book.route("/<id>", methods=["GET"])
def getBook(id):
    book = Book.query.get(id)

    if not book: return item_not_found_response("Book")

    book_response = book.serialize()

    return response(book_response, 200)


@book.route("/create", methods=["POST"])
def post():
    for i in request.json:
        if request.json[i] == "":
            return response(
                "You must include all of the fields",
                400,
                "error"
            )

    id = generate_id()
    name = request.json["name"]
    year = request.json["year"]
    price = request.json["price"]
    author = request.json["author"]
    pages = request.json["pages"]
    publisher = request.json["publisher"]
    description = request.json["description"]

    book = Book(
        id = id, name = name, year = year, price = price, author = author,
        pages = pages, publisher = publisher, description = description
    )

    db.session.add(book)

    try:
        db.session.commit()

    except IntegrityError:
        return response("Book already exists", 400, "error")

    return response("Book created", 200, "success")


@book.route("/update/<id>", methods=["PUT"])
def update(id):
    book = Book.query.get(id)

    if not book: return item_not_found_response("Book")

    book.name = request.json["name"]
    book.year = request.json["year"]
    book.price = request.json["price"]
    book.author = request.json["author"]
    book.pages = request.json["pages"]
    book.publisher = request.json["publisher"]
    book.description = request.json["description"]

    try:
        db.session.commit()

    except IntegrityError:
        return response("Book already exists", 400, "error")

    return response("Book updated", 200, "success")


@book.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    book = Book.query.get(id)

    if not book: return item_not_found_response("Book")

    db.session.delete(book)
    db.session.commit()

    return response("Book deleted", 200, "success")