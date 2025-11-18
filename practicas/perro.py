import random
from pathlib import Path

# --- FUNCIÓN GLOBAL DE VERIFICACIÓN DE ESTADO ---
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
    def wrapper(self, *args, **kwargs):
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
            # En el código original se asignaba a 'manchas', pero no se usaba después
            # manchas = self.color_seg 
            print("Color base", self.color_base, "manchas", self.color_seg, "tamaño", self.tamano)
        else:
            print("Color base", self.color_base, "SIN manchas", "tamaño", self.tamano)


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
    
    
# # --- EJEMPLO DE USO ---
# perro1 = Perro()
# print("estado inicial:", perro1.estado)

# print("\n--- Ladrando (Despierto) ---")
# perro1.ladrar()

# print("\n--- Durmiendo ---")
# perro1.dormir()

# print("\n--- Comiendo (Dormido, requiere despertar) ---")
# # Al llamar a comer, se ejecuta el decorador, que llama a verificar_estado.
# # verificar_estado pedirá input al usuario.
# perro1.comer() 

# print("\n--- Corriendo (Recién despierto) ---")
# perro1.correr()

# print("\n--- Ofrecer comida (Recién despierto) ---")
# perro1.ofrecer_comida()

# print("estado final:", perro1.estado)