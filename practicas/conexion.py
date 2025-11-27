import psycopg2

class Conexion:
    def __init__(self, host, database, user, password):
        print("__INIT__")
        self.host = host
        self.database = database
        self.user = user
        self.password = password


    def __enter__(self):
        try:
            self.conexion = psycopg2.connect(
                host = self.host,
                database = self.database, 
                user =self.user, 
                password = self.password
                )
            self.cursor = self.conexion.cursor()
            print("Conexión establecida")
            return self
        except Exception as e:
            print("ERROR al conectar:", e)

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.conexion.close()
        print("Conexión cerrada")


    def listar(self):
        try:
            query = "SELECT * FROM perros"
            self.cursor.execute(query)
            resp = self.cursor.fetchall()
            print("***Lista de perros disponibles***")
            for fila in resp:
                print(f"Id: {fila[0]}, nombre: {fila[1]}, raza: {fila[2]}, dueno {fila[3]}")
            
            return resp #el return es opcional
        except Exception as e:
            print("ERROR listando")
            return []


    def insertar(self, nombre, raza, dueno):
        try:
            query ="INSERT INTO perros (nombre, raza, dueno) VALUES (%s, %s, %s)"
            self.cursor.execute(query,(nombre, raza, dueno))
            self.conexion.commit()
            print("Perro insertado")
        except Exception as e:
            print("Error al insertar", e)
            self.conexion.rollback()

        
    def eliminar(self, id):
        try:
            query ="DELETE FROM perros WHERE id =  %s"
            self.cursor.execute(query, (id,))
            self.conexion.commit()
            print("Perro Eliminado")
        except Exception as e:
            print("Error al eliminar", e)
            self.conexion.rollback()



### ESTO CREAS UNA INSTANCIA Se llama de esta forma por que se necesita ajecutar el bloque __enter__ y __exit__
# with Conexion ("wazuh-server.cm.com.ve", "siis", "siis", "siis")as conn:
#     conn.listar()
#     conn.eliminar(5)
#     conn.listar()
