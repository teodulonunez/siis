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

    def verificar_estado(self):
        """Devuelve True si el perro está despierto y listo para actuar."""
        if self.estado == True:
            return True # Ya está despierto, puede continuar
        
        # Si self.estado es False (dormido):
        respuesta = input("El perro está dormido. ¿Despertar? (S/N): ").upper()
        
        if respuesta == "S":
            # CORRECCIÓN: Asignación (=)
            self.estado = True 
            print("Perro despierto y listo.")
            return True
        else:
            print("Dormido")

    def ladrar(self):
        self.verificar_estado()
        print("GUAU")

    def dormir(self):
        if self.verificar_estado() == True:
            self.estado = False

    def comer(self):
        self.verificar_estado()

    def ofrecer_comida(self):
        if self.verificar_estado():
            with open('alimento.txt', 'w') as archivo:
                archivo.write("Y esta es la segunda línea.")
    
    



perro1 = Perro()
print("estado: ",perro1.estado)
#perro1.dormir()
perro1.ladrar()
perro1.dormir()
perro1.ofrecer_comida()
perro1.ladrar()
print("estado: ",perro1.estado)


