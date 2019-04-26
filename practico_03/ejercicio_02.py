# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime
import sqlite3

from practico_03.ejercicio_01 import reset_tabla


def agregar_persona(nombre, nacimiento, dni, altura):
    db=sqlite3.connect('mibase.db')
    cursor=db.cursor()
    sentencia = "INSERT into personas(nombre,fechaNacimiento,dni,altura)" \
                "VALUES(?,?,?,?)"
    tdatos = (nombre,nacimiento,dni,altura)
    cursor.execute(sentencia,tdatos)
    db.commit()
    id = cursor.lastrowid
    db.close()
    return id

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.date(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()