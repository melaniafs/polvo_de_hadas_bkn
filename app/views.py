from flask import jsonify, request
from app.models import Cliente

def index():
    return '<h1>Hola mundo con flask 🐍</h1>'

def get_all_clientes():
    clientes = Cliente.get_all()
    list_clientes = [clientes.serialize() for cliente in clientes]
    return jsonify(list_clientes)

def get_cliente(idcliente):
    cliente = Cliente.get_by_id(idcliente)
    if not cliente:
        return jsonify({'message': 'Cliente no encontrado'}), 404
    return jsonify(cliente.serialize())

def create_cliente():
    #recepciona los datos enviados en la petición en formato json (obviamente lo convierte en un diccionario)
    data = request.jason
    new_cliente = Cliente(
        nombre = data['nombre'], 
        apellido= data['apellido'], 
        birthday=data['birthday'], 
        country=data['coutry'], 
        correo=['correo'], 
        password=data['password']
    )
    new_cliente.save()
    return jsonify({'message': 'Cliente creada con éxito'}), 201


def update_cliente(idcliente):
    cliente = Cliente.get_by_id(idcliente)
    if not cliente:
        return jsonify({'message': 'Cliente no encontrado'}), 404
    data = request.json
    cliente.nombre = data['nombre']
    cliente.apellido = data['apellido']
    cliente.birthday = data['birthday']
    cliente.country = data['country']
    cliente.correo = data['correo']
    cliente.password = data['password']
    cliente.save
    return jsonify ({'message': 'Cliente modificado con éxito'})


def delete_cliente(idcliente):
    cliente = Cliente.get_by_id(idcliente)
    if not cliente:
        return jsonify({'message': 'Cliente no encontrado'}), 404
    cliente.delete()
    return jsonify({'message': 'Cliente eliminado con éxito'})
    