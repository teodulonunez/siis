import psycopg2

class Conexion:
    def __init__(self, host, database, user, password):
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
            return self.cursor
        except Exception as e:
            print("ERROR al conectar:", e)

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.conexion.close()
        print("Conexión cerrada")

    def insertar (self, nombre, raza, dueno):
        try:
            query ="INSERT INTO perros (nombre, raza, dueno) VALUES (%s, %s, %s)"
            self.cursor.execute(query,(nombre, raza, dueno))
            self.conexion.commit
            print("Perro insertado")
        except Exception as e:
            print("Error al insertar", e)
            self.conexion.rollback()


# Uso con contexto
with Conexion("wazuh-server.cm.com.ve","siis","siis","siis") as cursor:
    cursor.execute("SELECT version();")
    for fila in cursor.fetchall():
        print(fila)