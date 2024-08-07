from flask import Blueprint, jsonify, request
from models import Cell
from app import db

api_bp = Blueprint('api', __name__)

@api_bp.route('/cells', methods=['GET'])
def get_cells():
    cells = Cell.query.all()
    result = [{'id': cell.id, 'discharge_capacity': cell.discharge_capacity, 'nominal_capacity': cell.nominal_capacity} for cell in cells]
    return jsonify(result)

@api_bp.route('/cells/<int:cell_id>', methods=['GET'])
def get_cell_data(cell_id):
    cell = Cell.query.get_or_404(cell_id)
    # Fetch additional data for cell and calculate SoH
    soh = (cell.discharge_capacity / cell.nominal_capacity) * 100
    return jsonify({'id': cell.id, 'soh': soh})
