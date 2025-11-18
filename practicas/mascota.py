from perro import Perro
import random

def validar(func):
    def wrapper(self, *args, **kwargs):
        res = int(input("edad:"))
        if res >= 18:
            print("ok")
            func(self)
        else:
            print("Menor de edad", res)
    return wrapper

class Mascota(Perro):
    def __init__(self):
        self.estado = True
        self.color1 = ("negro", "amarillo", "rojo", "marron")
        self.color_base = random.choice(self.color1)
        self.tamano = "mediano"
        self.pelo_op = "largo"   
        print("pastor color",self.color_base,"tamaño",self.tamano, "pelo:",self.pelo_op)

    
    @validar
    def jugar(self):
        print("fun jugar")

    #jugar()

# 

class Mascota_hija (Mascota):
    def __init__(self):
        super(). __init__()

    @validar
    def ladrar(self):
        print("hola")

m = Mascota_hija()
m.ladrar()

        