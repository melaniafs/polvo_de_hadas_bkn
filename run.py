from flask import Flask
from app.views import *
from app.database import init_app
from flask_cors import CORS


#inicializacion del proyecto Flask
app = Flask(__name__) #este parametro ayuda a indicar donde está ubicado el módulo para que despues pueda acceder a distintos directorios dentro del proyecto

init_app(app)
#permitir solicitudes desde cualquier origen
CORS(app)
#permitir solicitudes desde un origen específico
# CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000"}})


app.route('/', methods=['GET'] )(index)
app.route('/api/registros', methods=['GET'])(get_all_clientes)
app.route('/api/registros/create', methods=['POST'])(create_cliente)
app.route('/api/registros/delete', methods=['DELETE'])(delete_cliente)
app.route('/api/registros/modificar', methods=['PUT'])(update_cliente)
app.route('/api/registros/<int:idcliente>', methods=['GET'])(get_cliente)

if __name__=='__main__':
        app.run(debug=True)

