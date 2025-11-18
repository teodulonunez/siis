class Pincipal():
    def __init__(self):
        pass

    def trabajar(self):
        
        opt_trabajo = """
        ----------------------------------
        ¿Cuál será el trabajo?
            1. Ladrar
            2. Correr
            3. Vigilar
            4. Otro
        Para salir usar cualquier otra tecla
        ----------------------------------
        """
        
        # 1. Definimos el diccionario de acciones
        # La llave es la opción de input y el valor es el método de la clase (self.metodo) se llama sin parentesis por que se quiere el metodo no
        # la ejecucion del metodo
        acciones = {
            '1': self.ladrar,
            '2': self.correr,
            '3': self.vigilar,
            '4': self.otro_trabajo
        }
        
        while True:
            # Mostramos el menú y pedimos la respuesta, eliminando espacios en blanco
            resp = input(opt_trabajo).strip()
            
            # 2. Usamos .get() para buscar la acción. Si la llave no existe, get() devuelve None.
            accion_a_ejecutar = acciones.get(resp)
            
            if accion_a_ejecutar:
                # 3. Si la acción existe es true, la ejecutamos (llamamos a la función/método) en la linea donde se defincio accion_a_ejecutar
                # se igualo al metodo obtenido del diccionario
                accion_a_ejecutar()
            else:
                # 4. Si la opción no está en el diccionario, salimos
                print("\nSaliendo del menú de trabajo.")
                break