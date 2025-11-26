import psycopg2
# class conectar_postrgres: #no usa parentesis por que son opcionales cuando no se hereda
class Conectar_postgres:
    def __init__(self):
        #las variables aca deben tener self para ser accesibles al resto de la clase sin instanciar 
        try:
            self.conexion = psycopg2.connect(
                host = "wazuh-server.cm.com.ve",
                database = "siis",
                user = "siis",
                password = "siis"
            )
        
            self.cursor = self.conexion.cursor()
            self.cursor.execute("SELECT version();")
            self.version = self.cursor.fetchone()

            print("Conexion ok Version: ", self.version)
        
        except Exception as e:
            print("ERROR",e)

    # def consultar(self, query):
    #     resp = self.cursor.execute(query)
        


conn = Conectar_postgres()
    # select = cursor.execute("SELECT * FROM razas;")
    # consulta = cursor.fetchall()
    # for consulta_resp in consulta:
    #     print(f"select:")
    #     print(consulta_resp)