from perro import Perro, requiere_despierto
import random
from pathlib import Path

class Pastor(Perro):
    def __init__(self):
        # Llama al constructor del padre para asegurar la inicialización de self.estado.
        super().__init__()

        self.estado = True
        self.color1 = ("blanco", "negro", "griz")
        self.color_base = random.choice(self.color1)
        self.tamano = "grande"
        self.pelo_op = "corto"
        
        print("pastor color",self.color_base,"tamaño",self.tamano, "pelo:",self.pelo_op)

    def crear_rebano(self):
        with open("rebano.txt", "a") as rebano:
            entrada = input("escribir:")
            #escribe 1 para pastorear
            rebano.write("\n"+entrada)
            
    @requiere_despierto
    def buscar_rebano(self):
        ruta_rebano = Path("rebano.txt")
        try:
            with open ("rebano.txt", "r") as existe_rebano:
                contenido = existe_rebano.readlines()
                ultima_linea = contenido[-1].strip()
                
                if ultima_linea == "1":
                    print("rebaño encontrado:", ultima_linea)
                    return True
                else:
                    print("rebaño encontrado pero:", ultima_linea)
                    return False
                
        except FileNotFoundError:
            print("no existe archivo")

    @requiere_despierto
    def pastorear(self):
        if self.correr() and self.buscar_rebano():
            print("pastoreando")
        else:
            print("error en el archivo")

# pastor = Pastor()
# pastor.crear_rebano()
# pastor.pastorear()