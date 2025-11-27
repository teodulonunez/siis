# import psycopg2
# # class conectar_postrgres: #no usa parentesis por que son opcionales cuando no se hereda
# class Conectar_postgres:
#     def __enter__(self):
#         #las variables aca deben tener self para ser accesibles al resto de la clase sin instanciar 
#         try:
#             self.conexion = psycopg2.connect(
#                 host = "wazuh-server.cm.com.ve",
#                 database = "siis",
#                 user = "siis",
#                 password = "siis"
#             )
        
#             self.cursor = self.conexion.cursor()
#             self.cursor.execute("SELECT version();")
#             self.version = self.cursor.fetchone()

#             print("Conexion ok Version: ", self.version)
#             return self.cursor
        
        
        
#         except Exception as e: 
#             print("ERROR",e)

    # def consultar(self, query):
    #     resp = self.cursor.execute(query)
    


#conn = Conectar_postgres()
    # select = cursor.execute("SELECT * FROM razas;")
    # consulta = cursor.fetchall()
    # for consulta_resp in consulta:
    #     print(f"select:")
    #     print(consulta_resp)

import psycopg2

class Conexion:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password


    def __enter__(self):
        try:
            self.conexion = psycopg2.connect(self.host, self.database, self.user, self.password)
            self.cursor = self.conexion.cursor()
            print("Conexión establecida")
            return self.cursor
        except Exception as e:
            print("ERROR al conectar:", e)

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.conexion.close()
        print("Conexión cerrada")


# Uso con contexto
with Conexion("wazuh-server.cm.com.ve","siis","siis","siis") as cursor:
    cursor.execute("SELECT version();")
    for fila in cursor.fetchall():
        print(fila)