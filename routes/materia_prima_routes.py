from flask import Blueprint, request, jsonify
from models.materia_prima import MateriaPrima, db

materia_prima_bp = Blueprint('materia_prima', __name__)

@materia_prima_bp.route('/materia_prima', methods=['POST'])
def create_materia_prima():
    data = request.get_json()

    if not data or 'nombre' not in data or 'cantidad' not in data or 'unidad_medida' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    new_materia_prima = MateriaPrima(
        nombre=data['nombre'],
        cantidad=data['cantidad'],
        unidad_medida=data['unidad_medida'],
        fecha_vencimiento=data['fecha_vencimiento'],
        costo_unitario=data['costo_unitario'],
        imagen=data.get('imagen')
    )

    db.session.add(new_materia_prima)
    db.session.commit()
    return jsonify(new_materia_prima.__to_dict__()), 201