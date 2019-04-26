# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from practico_03.ejercicio_01 import borrar_tabla, crear_tabla
import sqlite3

def crear_tabla_peso():
    db=sqlite3.connect('mibase.db')
    cursor=db.cursor()
    sentencia="""CREATE TABLE IF NOT EXISTS personas_peso([idPersona] INTEGER, [fecha] datetime, [peso] integer,
              PRIMARY KEY(idPersona,fecha) FOREIGN KEY(idPersona) REFERENCES personas(idPersona))"""
    cursor.execute(sentencia)
    db.commit()
    db.close()

def borrar_tabla_peso():
    db=sqlite3.connect('mibase.db')
    cursor=db.cursor()
    sentencia='DROP TABLE IF EXISTS personas_peso'
    cursor.execute(sentencia)
    db.commit()
    db.close()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper

def get_nombre_tabla():
    """Retorna el nombre de la tabla personas si es que existe, sino retorna None"""
    db = sqlite3.connect('mibase.db')
    cursor=db.cursor()
    sentencia2="SELECT name FROM sqlite_master WHERE TYPE='table' AND name='personas_peso'"
    nombre = cursor.execute(sentencia2).fetchone()
    if nombre != None:
        nombre = nombre[0]
    db.close()
    return nombre

crear_tabla_peso()
assert get_nombre_tabla() == 'personas_peso'
borrar_tabla_peso()
assert get_nombre_tabla() == None