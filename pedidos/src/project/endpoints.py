from flask import Blueprint, request, jsonify
from . import db
from project.models import Pedido
from project.serializers import PedidoSchema
from project.decoradores import autorizar

blueprint = Blueprint('usuarios',__name__)


@blueprint.route('/pedidos/',methods=['GET'])
@autorizar
def listar_pedidos(usuario):
    pedidos = Pedido.query.filter_by(usuario_id=usuario.id).all()

    return jsonify(PedidoSchema().dump(pedidos, many=True))

@blueprint.route('/pedidos',methods=['POST'])
@autorizar
def crear_pedido(usuario):
    datos = request.json
    datos = request.json | {'usuario_id' : usuario.id }

    pedido = PedidoSchema().load(datos)

    db.session.add(pedido)
    db.session.commit()

    return PedidoSchema().dump(pedido),201
   
@blueprint.route('/pedidos/<uuid>',methods=['GET'])
@autorizar
def obtener_pedidos(usuario,uuid):
    pedidos = Pedido.query.filter_by(usuario_id=usuario.id,uuid=uuid).firts()

    return jsonify(PedidoSchema().dump(pedidos))