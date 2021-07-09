from sqlalchemy.orm import load_only
from . import ma
from .models import Usuario


class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        load_only = ('password',)
        load_instance = True
