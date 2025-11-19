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



p = Principal()
p.mostrar_lista()


class mixto(p1, p2):