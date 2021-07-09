import jwt
from functools import wraps
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from werkzeug.exceptions import Forbidden, NotFound
from .models import Usuario
from .decorators import autorizar, log
from .serializers import UsuarioSchema
from . import db, bcrypt


usuariosb = Blueprint('usuarios',__name__)


@usuariosb.route('/register', methods=['POST'])
def index():
    usuario = UsuarioSchema().load(request.json)
    
    db.session.add(usuario)
    db.session.commit()

    return UsuarioSchema().dump(usuario), 201


@usuariosb.route('/usuarios', methods=['GET'])
@autorizar
@log
def listar_usuarios(usuario):
    usuarios = Usuario.query.all()

    return jsonify(UsuarioSchema().dump(usuarios, many=True)), 200


@usuariosb.route('/usuarios/<id>', methods=['GET'])
@autorizar
def obtener_usuario(usuario, id):
    if str(usuario.id) != id:
        raise Forbidden

    usuario_encontrado = Usuario.query.get_or_404(id)

    return UsuarioSchema().dump(usuario_encontrado), 200


@usuariosb.route('/usuarios/<id>', methods=['PUT'])
@autorizar
def actualizar_usuario(usuario, id):
    if str(usuario.id) != id:
        raise Forbidden

    usuario_encontrado = Usuario.query.get_or_404(id)

    usuario_encontrado = UsuarioSchema().load(
        request.json,
        instance=usuario_encontrado)

    db.session.add(usuario_encontrado)
    db.session.commit()

    return UsuarioSchema().dump(usuario_encontrado), 200


@usuariosb.route('/usuarios/<id>', methods=['DELETE'])
@autorizar
def eliminar_usuario(usuario, id):
    if str(usuario.id) != id:
        raise Forbidden

    usuario_encontrado = Usuario.query.get_or_404(id)

    db.session.delete(usuario_encontrado)
    db.session.commit()

    return '', 204


@usuariosb.route('/login', methods=['GET', 'POST'])
def login():
    datos = request.get_json()

    usuario = Usuario.query.filter_by(
        email=datos['email']).first()

    if usuario is None:
        raise NotFound

    if not bcrypt.check_password_hash(usuario.password, datos['password']):
        raise NotFound

    secret = '123ABC'

    payload = {
        'sub': usuario.id,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() +  timedelta(days=1)
    }

    return jwt.encode(payload, secret, algorithm='HS256')

usuariosb.route('usuario_actual',methods=['GET'])
@autorizar
def obtener_usuario_actual(usuario):
    return UsuarioSchema().dump(usuario),200
