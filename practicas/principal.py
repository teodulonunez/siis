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
        while True:
            try:
                perro1 = int(input("Elije primer perro: "))
                if 1 <= perro1 <= 5:
                    return perro1
                else:
                    print("opcion de 1 a 5")
            except ValueError: 
                print("Debe ser un número de 1 a 5 " )



        # validar(self, perro1)
        # perro2 = input("Elije segundo perro:")



p = Principal()
#p.mostrar_lista()
p.mostrar_lista()
p.crear_perro()
