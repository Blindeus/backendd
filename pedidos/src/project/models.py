from . import db
import uuid

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer,nullable=False)
    descripcion = db.Column(db.String,nullable=False)
    direccion = db.Column(db.String,nullable=False)
    fecha = db.Column(db.String,nullable=False)
    uuid = db.Column(db.String,nullable=True)


    def __init__(self, *args, **kwgars):
        super(Pedido,self).__init__(*args,**kwgars)
        self.uuid = uuid.uuid4()
