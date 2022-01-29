from . import book

def register_views(app):
    PREFIX = "api"
    app.register_blueprint(book.book, url_prefix=f"/{PREFIX}/books")