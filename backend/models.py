from app import db

class Cell(db.Model):
    __tablename__ = 'cell'
    id = db.Column(db.Integer, primary_key=True)
    discharge_capacity = db.Column(db.Float)
    nominal_capacity = db.Column(db.Float)

# Define other models as needed
