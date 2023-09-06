from odoo import fields, models

class Book(models.Model):
    _name = "librarypractice.book"
    _description = "Book information"

    name = fields.Char(string = "name", required=True)
    active = fields.Boolean(default=True)
    isbn = fields.Char(string = "isbn")
    genre = fields.Char(string = "genre")
    summary = fields.Text(translate=True)
    author = fields.Char(string = "author")
    format = fields.Selection(string = "format",
                              selection =[
                                  ("paperback","Paperback"),
                                  ("hardcover", "Hardcover"),
                                  ("audiobook", "Audiobook"),
                                  ("e-book","E-Book")
                              ],copy=False)
    language = fields.Selection(string= "language",
                                selection =[
                                    ("en","EN"),
                                    ("es","ES"),
                                    ("fr","FR"),
                                    ("de","DE")
                                ],copy=False)
    edition = fields.Integer(string="edition")
    publisher = fields.Char(string = "publisher")
    publish_date = fields.Date(index=True)
    #price = fields.Monetary(string= "Total")
