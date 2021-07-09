import requests
from functools import wraps
from werkzeug.exceptions import Forbidden, InternalServerError, NotFound, Unauthorized
from flask import request


class Usuario:
    def __init__(self,id,nombre,email,rut,numeroDocumento,fechaNacimiento,telefono,):
        self.id = id
        self.nombre = nombre 
        self.email = email
        self.rut = rut
        self.numeroDocumento = numeroDocumento
        self.fechaNacimiento = fechaNacimiento
        self.telefono = telefono


def autorizar (f):
    @wraps(f)
    def wreapper(*args,**kwargs):
        authorization= request.headers.get('authorization')
        response = requests.get(
            url='https://usuarios:5000/usuario_actual', ##duda##
            headers=
                {'Authorization': authorization}
            )
        if response.status_code == 200:
            usuario = Usuario(**response.json())
            return f(usuario, *args, **kwargs)
        elif response.status_code == 401:
            raise Unauthorized  
        elif response.status_code == 403:
            raise Forbidden 
        else:
            raise InternalServerError     
    return wreapper

