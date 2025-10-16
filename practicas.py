import random

class Perro:
    def __init__(self, ):
        color1 = ("marron", "negro", "blanco", "amarillo")
        color2 = ("marron", "negro", "blanco", "amarillo")
        color_base = random.choice(color1)
        color_seg = random.choice(color2)
        
        tamano_op = ("pequeño", "mediano", "grande")
        tamano = random.choice(tamano_op)

        pelo_op = ("corto", "largo")
        pelo = random.choice(pelo_op)

        if color_base != color_seg:
            manchas = color_seg
            print("Color base",color_base, "manchas", color_seg, "tamaño", tamano)
        else:
            print("Color base",color_base, "SIN manchas", "tamaño", tamano)
#perro = Perro(input("Introduce: "))
perro2 = Perro()