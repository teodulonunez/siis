import psycopg2

# class conectar_postrgres: #no usa parentesis por que son opcionales cuando no se hereda

#     def __init__(self, host, database, usuario, password):
#         self.conn_params


try:
    conexion = psycopg2.connect(
        host = "wazuh-server.cm.com.ve",
        database = "siis",
        user = "siis",
        password = "siis"
    )

    print("Conexion OK")
    
    cursor = conexion.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    select = cursor.execute("SELECT * FROM razas;")
    consulta = cursor.fetchall()
    for consulta_resp in consulta:
        print(f"select:")
        print(consulta_resp)
    print("Version: ", version)
  
except Exception as e:
    print("ERROR",e)