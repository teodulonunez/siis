from pathlib import Path
import os, sys, importlib

class Principal():
    def __init__(self):
        pass


    def mostrar_lista(self):
        """Muestra los tipos de perros disponibles"""
        #directorio actual
        directorio_proyecto = Path('.')
        print("*****tipos de perro:")
        indice = 1
        lista = []
        for archivo_path in directorio_proyecto.glob('*.py'):
            nombre_archivo = archivo_path.name
            
            if nombre_archivo not in ('principal.py', 'perro.py') and archivo_path.is_file():
                nombre_clase = nombre_archivo.replace('.py', '').capitalize()
                print(f"{indice}: {nombre_clase}")
                lista.append(nombre_clase)
                #print(f"lista {lista}")
                indice +=1
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

        print(f"Fuera del ciclo perro1: {lista[perro1 -1]} perro2: {lista[perro2 -1]}")
        return lista, perro1, perro2
 															 

    def crear_perro(self):
        lista, perro1, perro2 = self.crear_cruces()
        # Importar dinámicamente los módulos
        modulo1 = importlib.import_module(lista[perro1 - 1].lower())
        modulo2 = importlib.import_module(lista[perro2 - 1].lower())

        # Obtener las clases
        clase1 = getattr(modulo1, lista[perro1 - 1])
        clase2 = getattr(modulo2, lista[perro2 - 1])

        # Clase híbrida por composición
        class Cruce:
            def __init__(self):
                self.obj1 = clase1()
                self.obj2 = clase2()

            def __getattr__(self, nombre):
                """Delegar automáticamente métodos a los objetos internos"""
                if hasattr(self.obj1, nombre):
                    return getattr(self.obj1, nombre)
                elif hasattr(self.obj2, nombre):
                    return getattr(self.obj2, nombre)
                else:
                    raise AttributeError(f"{nombre} no existe en el híbrido")

        return Cruce()
						

    def mostrar_menu_acciones(self, perro):
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
                    print("Saliendo del menú de acciones...")
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
perro = p.crear_perro()
p.mostrar_menu_acciones(perro)



# perro.vigilar()     # método de Guardian
# perro.pastorear()   # método de Pastor
# perro.ladrar()      # método heredado de Perro