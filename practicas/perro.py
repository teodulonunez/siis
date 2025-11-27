import random
from pathlib import Path

# --- ESta FUNCIÓN debe ser GLOBAL VERIFICACIÓN DE ESTADO ---
def verificar_estado(instancia_perro):
    """Devuelve True si el perro está despierto o se despierta."""
    if instancia_perro.estado is True:
        return True # Ya está despierto, puede continuar
    # Si instancia_perro.estado es False (dormido):
    respuesta = input("MSM desde clase perro El perro está dormido. ¿Despertar? (S/N): ").upper()
    
    if respuesta == "S":
        instancia_perro.estado = True 
        print("Perro despierto y listo.")
        return True
    else:
        print("Dormido, no se puede realizar la acción.")
        return False

# --- DECORADOR ---
def requiere_despierto(func):
    """Decorador que verifica el estado del perro antes de ejecutar el método."""
    def wrapper(self, *args, **kwargs): #kwargs tambien se usa para decir cualquier cantida de argumentos nombrados
        if verificar_estado(self):
            return func(self, *args, **kwargs)
        # Si verificar_estado devuelve False, el método simplemente no se ejecuta
    return wrapper


class Perro:
    def __init__(self):
        self.estado = True
        self.color1 = ("marron", "negro", "blanco", "amarillo")
        self.color2 = ("marron", "negro", "blanco", "amarillo")
        self.color_base = random.choice(self.color1)
        self.color_seg = random.choice(self.color2)
        
        self.tamano_op = ("pequeño", "mediano", "grande")
        self.tamano = random.choice(self.tamano_op)

        self.pelo_op = ("corto", "largo")
        self.pelo = random.choice(self.pelo_op)

        if self.color_base != self.color_seg:
            print("Perro Color base", self.color_base, "manchas", self.color_seg, "tamaño", self.tamano)
        else:
            print("Perro Color base", self.color_base, "SIN manchas", "tamaño", self.tamano)


    @requiere_despierto
    def ladrar(self):		   
        print("GUAU")


    # El método dormir ahora solo cambia el estado, la verificación se hace con el decorador
    @requiere_despierto
    def dormir(self):
        self.estado = False					   
        print("perro dormido")


    @requiere_despierto
    def comer(self):						   
        ruta_comida = Path('alimento.txt')
        if ruta_comida.exists() and ruta_comida.is_file():
            print("comiendo")
        else:
            print("sin comida")
        

    @requiere_despierto
    def ofrecer_comida(self):
        # NOTA: Esto CREA el archivo, lo que es útil para la función comer
        with open('alimento.txt', 'w') as archivo:
            archivo.write("Comida fresca para el perro.")
        print("Comida ofrecida (alimento.txt creado/escrito).")


    @requiere_despierto
    def correr(self):					   
        print("perro corriendo")
        return True
