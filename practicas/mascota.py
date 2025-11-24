from perro import Perro, requiere_despierto
import random

def validar(func):
    def wrapper(self, *args, **kwargs):
        res = int(input("edad:"))
        if res >= 5:
            print("ok")
            func(self)
        else:
            print("Menor de edad", res)
    return wrapper

class Mascota(Perro):
    def __init__(self):
        super().__init__()
        self.estado = True
        self.color1 = ("negro", "amarillo", "rojo", "marron")
        self.color_base = random.choice(self.color1)
        self.tamano = "mediano"
        self.pelo_op = "largo"   
        print("pastor color",self.color_base,"tamaño",self.tamano, "pelo:",self.pelo_op)

    @requiere_despierto
    @validar
    def jugar(self):
        print("fun jugar")

# m = Mascota()
# m.jugar()



        