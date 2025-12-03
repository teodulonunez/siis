import psycopg2
import logging

logging.basicConfig(
    filename='app_errors.log', # Archivo donde se guardarán los logs
    level=logging.INFO,       # Nivel mínimo a registrar (solo errores o superiores)
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class Conexion:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password


    def __enter__(self):
        #Establecer conexion 
        try:
            self.conexion = psycopg2.connect(
                host = self.host,
                database = self.database, 
                user =self.user, 
                password = self.password
                )
            self.cursor = self.conexion.cursor()
            logging.info(f"Conexion ok a BD")
            return self
        except Exception as e:
            logging.error(f"Error la conectar a la BD: {e}")


    def __exit__(self, exc_type, exc_value, traceback):
        #cerrar conexion 
        self.cursor.close()
        self.conexion.close()


    def listar(self):
        query = "SELECT * FROM perros"
        try:
            self.cursor.execute(query)
            resp = self.cursor.fetchall()         
        except Exception as e:
            logging.error(f"Error obteniendo {e}")
            return []
        else:
            return resp #el return es opcional
            

    def insertar(self, nombre, raza, dueno):
        query ="INSERT INTO perros (nombre, raza, dueno) VALUES (%s, %s, %s)"
        try:
            self.cursor.execute(query,(nombre, raza, dueno))
            self.conexion.commit()      
        except Exception as e:
            self.conexion.rollback()
            logging.error("Error Insertando {e}")
        else:
            logging.info("Insertado")

        
    def eliminar(self, id):
        query ="DELETE FROM perros WHERE id =  %s"
        try:
            self.cursor.execute(query, (id,))
            self.conexion.commit()
        except Exception as e:
            self.conexion.rollback()
            logging.error(f"Error borrando {e}")
            return False
        else:
            logging.info(f"Eliminado id {id}")
            return True


    def actualizar(self, id, nombre, raza, dueno):
        query = "UPDATE perros set nombre=%s, raza=%s, dueno=%s WHERE id=%s"
        try:
            self.cursor.execute(query,(nombre, raza, dueno, id))
            self.conexion.commit()
        except Exception as e:
            self.conexion.rollback()
            logging.error("Error modificando {e}")
        else:
            logging.info("Modificado id {id}")

    def id_disponible(self,id):
        query = "SELECT id FROM perros where id =%s"
        try:
            self.cursor.execute(query,(id))
            resp = self.cursor.fetchall()
        except Exception as e:
            self.conexion.rollback()
            logging.error("Error obteniendo ID {id} ,{e}")
        else: 
            return resp
