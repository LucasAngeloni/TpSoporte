# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3

def crear_tabla():
    """Crea tabla personas en base de datos mibase"""
    db=sqlite3.connect('mibase.db')
    cursor=db.cursor()
    sentencia='CREATE TABLE IF NOT EXISTS personas([idPersona] INTEGER PRIMARY KEY AUTOINCREMENT, [nombre] text(30), [fechaNacimiento] datetime, [dni] integer, [altura] integer)'
    cursor.execute(sentencia)
    db.commit()
    db.close()

def borrar_tabla():
    """Borra tabla personas en base de datos mibase"""
    db=sqlite3.connect('mibase.db')
    cursor=db.cursor()
    sentencia='DROP TABLE IF EXISTS personas'
    cursor.execute(sentencia)
    db.commit()
    db.close()

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper

def get_nombre_tabla():
    """Retorna el nombre de la tabla personas si es que existe, sino retorna None"""
    db = sqlite3.connect('mibase.db')
    cursor=db.cursor()
    sentencia2="SELECT name FROM sqlite_master WHERE TYPE='table' AND name='personas'"
    nombre = cursor.execute(sentencia2).fetchone()
    if nombre != None:
        nombre = nombre[0]
    db.close()
    return nombre

crear_tabla()
assert get_nombre_tabla() == 'personas'
borrar_tabla()
assert get_nombre_tabla() == None

