from guardian import Guardian
from pastor import Pastor
from perro import requiere_despierto
import time, datetime, random

class Trabajo(Guardian, Pastor):
    def __init__(self):
        super().__init__()
        self.raza = "trabajo"
        #instanciar los padres para obtener atributos, estos se definene en el contructor solo se puede acceder a ellos al instanciar
        guardian = Guardian()
        pastor = Pastor()
        porcentaje_guardian = random.randrange(1,100)
        porcentaje_pastor = 100 - porcentaje_guardian
        print(f"El perro es {porcentaje_guardian}% de guardian y {porcentaje_pastor}% de pastor")
        color_pelo = (guardian.color_base, pastor.color_base)
        porcentaje_padres = [porcentaje_guardian, porcentaje_pastor]

        self.estado = True
        self.color_base = random.choices(color_pelo, weights=porcentaje_padres)[0]
        self.tamano = "mediano"
        self.pelo_op = "largo"
        
        print("Perro de trabajo color",self.color_base,"tamaño",self.tamano, "pelo:",self.pelo_op)


    @requiere_despierto    
    def verificar_horario(self):
        #if self.verificar_estado():
    # Obtiene la hora y el día actual del sistema y determina  si está dentro del horario laboral (Lunes a Viernes, 8:00 a 17:00).
        ahora = datetime.datetime.now()
        
# Obtener día de la semana: Lunes es 0, Domingo es 6
        dia_semana = ahora.weekday() 
        
# Obtener solo la hora para la comparación
        hora_actual = ahora.time()
        
# Definición de los límites
        hora_inicio = datetime.time(8, 0, 0)  # 08:00:00
        hora_fin = datetime.time(17, 0, 0)    # 17:00:00 (las 5 PM)
        
# 1. Comprobar si es un día de semana (Lunes=0 a Viernes=4)
        es_dia_laboral = dia_semana >= 0 and dia_semana <= 4
        
# 2. Comprobar si la hora está dentro del rango (incluye las 8:00, excluye las 17:00 exactas)
        esta_en_horario = hora_actual >= hora_inicio and hora_actual < hora_fin
        
        print(f"Hora actual: {ahora.strftime('%A, %H:%M:%S')}")
        print("---------------------------------------")
        
        if es_dia_laboral and esta_en_horario:
                print("ESTADO: Horario laboral (¡A trabajar!)")
                return True
        else:
                print("ESTADO: Horario NO laboral (¡A descansar!)")
                return False
    
    
    def trabajar(self):
        #verifica que el metodo prerequisito verificar horario regreze true
        if self.verificar_horario():
                resp = int(input("unidades de trabajo:"))
                print("Barra de avance: ", end="") 
    
        for i in range(resp):
# i comienza en 0 Imprimimos el asterisco en la misma línea usando end=''Usamos flush=True para forzar la impresión inmediatamente.
            print("*", end="", flush=True) 
            time.sleep(0.1)
        # Agregamos un salto de línea después de que el ciclo termina
        print("\n¡Proceso Completado!")