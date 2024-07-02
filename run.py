from flask import Flask
from app.views import *
from app.database import init_app
from flask_cors import CORS

#inicializacion del proyecto Flask
app = Flask(__name__) #este parametro ayuda a indicar donde está ubicado el módulo para que despues pueda acceder a distintos directorios dentro del proyecto

init_app(app)

app.route('/', methods=['GET'] )(index)
app.route('/api/registros', methods=['GET'])(get_all_clientes)
app.route('/api/registros/create', methods=['POST'])(create_cliente)

if __name__=='__main__':
        app.run(debug=True)



app.route('/',methods=['GET'])(index)
app.route('/api/registers',methods=['GET'])(get_all_registers)

if __name__=='__main__':
    app.run(debug=True) """