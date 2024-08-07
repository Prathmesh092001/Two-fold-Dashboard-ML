import unittest
from app import app, db
from models import Cell

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_cells(self):
        response = self.app.get('/api/cells')
        self.assertEqual(response.status_code, 200)

    def test_get_cell_data(self):
        cell = Cell(id=5308, discharge_capacity=2992.02, nominal_capacity=3000)
        db.session.add(cell)
        db.session.commit()
        response = self.app.get('/api/cells/5308')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
    
    


