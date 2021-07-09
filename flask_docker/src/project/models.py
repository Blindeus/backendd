from . import db
from . import bcrypt


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    rut = db.Column(db.String,nullable=False)
    numeroDocumento = db.Column(db.String, nullable=False)
    fechaNacimiento = db.Column(db.String, nullable=False)
    telefono = db.Column(db.String,nullable=False )
    password = db.Column(db.String, nullable=False)

    def __init__(self, **kwargs):
        super(Usuario, self).__init__(**kwargs)
        self.password = self.generar_password(**kwargs)

    def generar_password(self, **kwargs):
        if 'password' not in kwargs:
            return None

        return bcrypt.generate_password_hash(kwargs['password']).decode()