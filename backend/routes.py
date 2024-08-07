# routes.py
from flask import Blueprint, jsonify
from models import Cell

api_bp = Blueprint('api', __name__)

@api_bp.route('/cells', methods=['GET'])
def get_cells():
    cells = Cell.query.all()
    return jsonify([{'id': cell.id, 'name': cell.name, 'value': cell.value} for cell in cells])
