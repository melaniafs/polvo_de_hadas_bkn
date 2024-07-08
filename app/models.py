from app.database import get_db

class Cliente:

    #constuctor
    def __init__(self,idcliente=None,nombre=None,apellido=None,birthday=None,country=None,correo=None,password=None):
        self.idcliente=idcliente
        self.nombre=nombre
        self.apellido=apellido
        self.birthday=birthday
        self.country=country
        self.correo=correo
        self.password=password

    
    @staticmethod # el métodos estatico se utiliza para poder utilizar la clase sin instanciarla
    def get_all():
        db = get_db() #crea la conexión a la base de datos
        cursor = db.cursor() #cursor es un objeto de la conexión que permite poder ejecutar comandos SQL en la base de datos y recuperar los resultados de la consulta
        query = "SELECT * FROM clientes"
        cursor.execute(query)
        rows = cursor.fetchall() #Me devuelve una lista de tuplas

        #instancia de la clase cliente
        clientes = [Cliente(idcliente=row[0], nombre=row[1], apellido=row[2], birthday=row[3], country=row[4], correo=row[5]) for row in rows]

        cursor.close()
        return clientes
        
    @staticmethod
    def get_by_id(idcliente):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM clientes WHERE idcliente = %s", (idcliente,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Cliente(idcliente=row[0],nombre=row[1], apellido=row[2], birthday=row[3], country=row[4], correo=row[5])
        return None

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.idcliente:
            cursor.execute("""
                 UPDATE clientes SET nombre = %s, apellido = %s, birthday= %s, country = %s, correo = %s, password = %s 
                WHERE idcliente = %s""", 
                (self.nombre, self.apellido, self.birthday, self.country, self.correo,self.password,self.idcliente))
        else:
            cursor.execute("""
                INSERT INTO clientes (nombre, apellido, birthday, country, correo, password) 
                VALUES (%s, %s, %s, %s, %s, %s)""", 
                (self.nombre, self.apellido, self.birthday, self.country, self.correo,self.password))
            self.idcliente = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM clientes WHERE idcliente = %s", (self.idcliente,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'idcliente': self.idcliente,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'birthday': self.birthday,
            'country': self.country,
            'correo': self.correo,
            'password':self.password

        }
        