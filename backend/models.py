# models.py
from db_setup import db

class Cell(db.Model):
    __tablename__ = 'cell'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    value = db.Column(db.Float)

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f'<Cell {self.name}>'
