from pathlib import Path
import os, sys, importlib, random
from conexion import Conexion
import logging
import string
# importados para crea la lista de métodos
import guardian
import mascota
import pastor
import trabajo
# Obtiene el logger para este módulo
logger = logging.getLogger(__name__)

class Principal():
    def __init__(self):


        def menu_principal():
            print("-----MENU PRINCIPAL-----")
            lista_metodos = []

            for metodos in dir (Principal):
                #excluir métodos
                if metodos.startswith('__') and metodos.endswith('__') or metodos == 'crear_cruces':
                    continue

                atributo = getattr(Principal, metodos)

                if callable(atributo):
                    lista_metodos.append(metodos)

            return tuple(lista_metodos)
        

        menu_principal = menu_principal()   
        #while True:
        for indice, elementos in enumerate(menu_principal):
            print(f"metodo {indice+1} : {elementos}" )
        
        while True:
            try: # el bloque try debe ser tan pequeño como sea posible solo las lienas que peuden falla o ocultara errores adicionales
                self.resp = int(input("Para salir pulse 0 ***** Elige una opcion: "))
            except Exception as e:
                logging.error(f"opcion: {e}")
                print(f"Opcion no valida")
            if self.resp == 0: 
                break
            if self.resp > len(menu_principal):
                continue

            #guardo el nombre del metodo real seccionado antes se le sumo 1 para usar el 0 como salida
            accion = menu_principal[self.resp-1]
            # ejecutar_accion = getattr(self, accion)
            # ejecutar_accion()
            getattr(self, accion)()#esta linea son las dos lineas anteriores resumidas el () al final ejecuta, esta funcion tiene un return
            #PARA CREAR PERRO SE DEBE INSTANCIAR VERIFICA CON los ultimos métodos 
            break
        

    def mostrar_lista(self):
        """Muestra los tipos de perros disponibles"""
        lista = ["Guardian", "Mascota", "Pastor", "Trabajo"]
        for i, nombre in enumerate(lista, start=1):
            print(f"{i}: {nombre}")
        return lista


    def crear_cruces(self):
        lista = self.mostrar_lista()
        tamano_lista = len(lista)
        salir = False
        while not salir:
            try:
                perro1 = int(input("Elije primer perro: "))
                if 1 <= perro1 <= tamano_lista:
                    while True:
                        try:
                            perro2 = int(input("Elije segundo perro: "))
                            if (1 <= perro2 <= tamano_lista):
                                if perro2 != perro1:
                                    salir = True
                                    break
                                else:
                                    print(f"perros identicos perro1:{perro1} > {lista[perro1 -1]} y perro2: {perro2} > {lista[perro2 -1]}")
                            else:
                                print(f"opcion de 1 a {tamano_lista}")
                        except ValueError:
                                print(f"2excep de 1 - {tamano_lista}")
                else:
                    print(f"opcion de 1 a {tamano_lista}")
            except ValueError: 
                print(f"Debe ser un número de 1 a {tamano_lista}" )

        print(f"Fuera del ciclo perro1: {lista[perro1 -1]} | perro2: {lista[perro2 -1]}")
        return lista, perro1, perro2

    def listar_disponibles(self):														 
        with Conexion("wazuh-server.cm.com.ve", "siis", "siis", "siis") as conn:
            lista = conn.listar()
            for fila in lista:
                print(f"Id: {fila[0]}, nombre: {fila[1]}, raza: {fila[2]}, dueno {fila[3]}")
        return lista

    def actualizar(self):
        print("**************************")
        self.listar_disponibles()
        id     = int(input("id a editar: "))
        nombre = input("nombre del perro: ")
        raza   = input("raza del perro: ")
        dueno  = input("dueño del perro: ")
        with Conexion("wazuh-server.cm.com.ve", "siis", "siis", "siis") as conn:
            conn.actualizar(id, nombre, raza, dueno)


    def eliminar(self):
        while True:
            self.listar_disponibles()
            try:
                id = int(input("SELECCIONA EL ID: "))
            except Exception as e:
                print("la opcion introducida no es valida")
            if id == 0:
                break
            with Conexion("wazuh-server.cm.com.ve", "siis", "siis", "siis") as conn:
                id_disponible = conn.eliminar(id)
            break

    def aleatorio(self):
        def generar_aleatorio(cantidad_default=1, longitud=8):
            for i in range(cantidad_default):
                """genera un perro de forma aleatoria y lo inserta en la BD"""
                longitud = random.randint(1, 8)
                nombre = ''.join(random.choice(string.ascii_letters) for i in range(longitud))
                raza = "aleatorio" + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(longitud))
                dueno = "teo"+''.join(random.choice(string.ascii_letters) for i in range(longitud))
                with Conexion("wazuh-server.cm.com.ve", "siis", "siis", "siis") as conn:
                    conn.insertar(raza, nombre, dueno)

        cantidad = input("Introduce cantidad Por defecto 1: ")
        if cantidad == "":
            #genera por defecto
            print(f"cantidad default 1: ")
            generar_aleatorio()
        else:
            try:
                repeticiones = int(cantidad)
            except Exception as e:
                print(f" {repeticiones} No es un numero se usa valor por defecto")
                generar_aleatorio()
                logging.error(f"Se introdujo {e}, usando valores por defecto")
                logging.info("Insercion por default")
            else:
                generar_aleatorio(repeticiones)
                logging.info(f"Se insertaron {repeticiones} perros")
   


## fin de la sección de funciones principales
    def crear_perro(self):

    # Diccionario de módulos y clases
        lista, perro1, perro2 = self.crear_cruces()
        clases = {
            "Guardian": guardian.Guardian,
            "Mascota": mascota.Mascota,
            "Pastor": pastor.Pastor,
            "Trabajo": trabajo.Trabajo,
        }

        clase1 = clases[lista[perro1 - 1]]
        clase2 = clases[lista[perro2 - 1]]

        class Cruce:
            def __init__(self):
                #se instancia los objetos de las clases padres
                self.nombre = input("nombre del perro:")
                self.dueno = input("tu nombre:")
                self.obj1 = clase1()
                self.obj2 = clase2()
                self.raza = self.obj1.raza+"-"+self.obj2.raza

                porcentaje_obj1 = random.randrange(1,100)
                porcentaje_obj2 = 100 - porcentaje_obj1

                print(f"El perro es {porcentaje_obj1}% de {self.obj1.raza} y {perro2}% de {self.obj2.raza}")

                color_pelo = (self.obj1.color_base, self.obj2.color_base)
                porcentaje_padres = [porcentaje_obj1, porcentaje_obj2]
                self.color_base = random.choices(color_pelo, weights=porcentaje_padres)[0]
                print(f"CLase Cruce color de pelo del perro:  {self.nombre}: {self.color_base}")


            def __getattr__(self, nombre):
                """Delegar automáticamente métodos a los objetos internos"""
                if hasattr(self.obj1, nombre):
                    return getattr(self.obj1, nombre)
                elif hasattr(self.obj2, nombre):
                    return getattr(self.obj2, nombre)
                else:
                    raise AttributeError(f"{nombre} no existe en el híbrido")
                                # Insertar en BD antes de mostrar menú
        
        perro = Cruce()

        with Conexion("wazuh-server.cm.com.ve", "siis", "siis", "siis") as conn:
            conn.insertar(perro.raza, perro.nombre, perro.dueno)
        return perro
		 

    def mostrar_menu_acciones(self):
        perro = self.crear_perro()
        """Muestra un menú con todos los métodos disponibles en el perro híbrido"""
        # Obtener métodos de los dos objetos internos
        metodos_obj1 = [m for m in dir(perro.obj1) if callable(getattr(perro.obj1, m)) and not m.startswith("__")]
        metodos_obj2 = [m for m in dir(perro.obj2) if callable(getattr(perro.obj2, m)) and not m.startswith("__")]

        # Unir y eliminar duplicados
        metodos = list(dict.fromkeys(metodos_obj1 + metodos_obj2))

        print("\n***** Acciones disponibles del perro híbrido *****")
        for i, metodo in enumerate(metodos, start=1):
            print(f"{i}: {metodo}")

        while True:
            try:
                opcion = int(input("Elige una acción (0 para salir): "))
                if opcion == 0:
                    break
                elif 1 <= opcion <= len(metodos):
                    metodo = metodos[opcion - 1]
                    print(f"Ejecutando acción: {metodo}")
                    # Buscar el método en obj1 o obj2
                    if hasattr(perro.obj1, metodo):
                        getattr(perro.obj1, metodo)()
                    elif hasattr(perro.obj2, metodo):
                        getattr(perro.obj2, metodo)()
                else:
                    print("Opción inválida")
            except ValueError:
                print("Debe ser un número válido")

    
p = Principal()
