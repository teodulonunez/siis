import yaml
from conexion import Conexion

class Exportar_yaml():
    def __init__(self, archivo="exportar.yaml"):
        self.archivo = archivo

    def obtener_perros(self):
        with Conexion("wazuh-server.cm.com.ve", "siis", "siis", "siis") as conn:
            return conn.listar()
        
    def exportar(self):
        lista = self.obtener_perros()

        data = {"perros": []}
        for fila in lista:
            perro = {
                "id":       fila[0],
                "nombre":   fila[1],
                "raza":     fila[2],
                "dueno":    fila[3]
            }
            data ["perros"].append(perro)

            with open(self.archivo, "w") as f:
                yaml.dump(data, f, default_flow_style=False, sort_keys=False)

                print(f"Archivo .YAML creado : {self.archivo}")

