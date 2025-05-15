from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MateriaPrima(db.Model):
    __tablename__ = 'materia_prima'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cantidad_unidad = db.Column(db.Float, nullable=False)
    cantidad_gramos = db.Column(db.Float, nullable=False)
    fecha_vencimiento = db.Column(db.Date, nullable=False)
    costo = db.Column(db.Float, nullable=False)
    imagen = db.Column(db.String(200))

    def __repr__(self):
        return f'<MateriaPrima {self.nombre}>'
    
    def __to_dict__(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'cantidad': str(self.cantidad),
            'unidad_medida': self.unidad_medida,
            'fecha_vencimiento': str(self.fecha_vencimiento),
            'costo_unitario': str(self.costo_unitario),
            'imagen': self.imagen
        }