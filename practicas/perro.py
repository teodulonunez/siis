import random

class Perro:
    def __init__(self ):
        self.estado = True
        self.color1 = ("marron", "negro", "blanco", "amarillo")
        self.color2 = ("marron", "negro", "blanco", "amarillo")
        self.color_base = random.choice(self.color1)
        self.color_seg  = random.choice(self.color2)
        
        self.tamano_op = ("pequeño", "mediano", "grande")
        self.tamano    = random.choice(self.tamano_op)

        self.pelo_op = ("corto", "largo")
        self.pelo    = random.choice(self.pelo_op)

        if self.color_base != self.color_seg:
            manchas = self.color_seg
            print("Color base",self.color_base, "manchas", self.color_seg, "tamaño", self.tamano)
        else:
            print("Color base",self.color_base, "SIN manchas", "tamaño", self.tamano)

    def ladrar(self):
        if self.estado == False:
            respuesta = input("¿Despertar?: S/N ").upper()
            if respuesta == "S":
                print("respuesta ", respuesta)
                self.estado == True
            else:
                print("sigue dormido")
        else:
            print("GUAU")

    def dormir(self):
        if self.estado == True:
            self.estado = False
            print("domido")
        else:
            print("Ya esta dormido")

    def comer(self):
        pass



perro1 = Perro()
print("estado: ",perro1.estado)
perro1.dormir()
perro1.ladrar()
perro1.dormir()
print("estado: ",perro1.estado)


