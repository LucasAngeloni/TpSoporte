# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
import sqlite3

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    db=sqlite3.connect('mibase.db')
    cursor=db.cursor()
    sentencia = 'DELETE FROM personas WHERE idPersona = ?'
    tdatos = (id_persona,)
    cursor.execute(sentencia,tdatos)
    db.commit()
    filas_afectadas = cursor.rowcount
    db.close()
    if filas_afectadas == 0:
        return False
    return True

@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()