from pathlib import Path
import os, sys

class Principal():
    def __init__(self):
        pass

    def mostrar_lista(self):
        """Muestra los tipos de perros disponibles"""
        #directorio actual
        directorio_proyecto = Path('.')
        print("*****tipos de perro:")
        indice = 1
        for archivo_path in directorio_proyecto.glob('*.py'):
            nombre_archivo = archivo_path.name
            
            if nombre_archivo != 'principal.py' and archivo_path.is_file():
                nombre_clase = nombre_archivo.replace('.py', '').capitalize()
                print(f"{indice}: {nombre_clase}")
                indice +=1

    def validar(self,numero_perro):
        pass


    def crear_perro(self):
        salir = False
        while not salir:
            try:
                perro1 = int(input("Elije primer perro: "))
                if 1 <= perro1 <= 5:
                    while True:
                        try:
                            perro2 = int(input("Elije segundo perro: "))
                            if (1 <= perro2 <= 5):
                                if perro2 != perro1:
                                    salir = True
                                    break
                                else:
                                    print(f"perros identicos perro1: {perro1} y perro2 {perro2}")
                            else:
                                print("opcion de 1 a 5")
                        except ValueError:
                                print("2excep de 1 - 5")
                else:
                    print("opcion de 1 a 5")
            except ValueError: 
                print("Debe ser un número de 1 a 5 " )

        print(f"Fuera del ciclo perro1: {perro1} perro2: {perro2}")

p = Principal()
p.mostrar_lista()
p.crear_perro()
