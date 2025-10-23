from perro import Perro
import random
#
class Guardian (Perro):
    def __init__(self):
        self.estado = True
        self.color1 = ("marron", "negro", "griz")
        self.color_base = random.choice(self.color1)
        self.tamano = "grande"
        self.pelo_op = "largo"
        
        print("guardian de color",self.color_base,"tamaño",self.tamano, "pelo:",self.pelo_op)

    def vigilar(self):
        if self.verificar_estado():
            print("vigilando")
        return True
    
    def patrullar(self):
        if self.vigilar() and self.correr():
            print("patrullando")


#guardian = Guardian()
#guardian.ladrar()
#print("estado",guardian.estado)
#guardian.vigilar()
#guardian.dormir()
#guardian.patrullar()