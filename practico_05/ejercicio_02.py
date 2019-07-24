# Implementar los metodos de la capa de datos de socios.
import os
from aifc import Error

from sqlalchemy import create_engine,exc
from sqlalchemy.orm import sessionmaker
from practico_05.ejercicio_01 import Base,Socio

class DatosSocio(object):

    def __init__(self):

        engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        self.crear_tabla()

    def crear_tabla(self):
        try:
            Socio.__table__.create()
        except:
            pass

    def borrar_tabla(self):
        try:
            Socio.__table__.drop()
        except:
            pass

    def buscar(self, id_socio):
        x = self.session.query(Socio).filter(Socio.id_socio == id_socio).first()
        return x

    def buscar_dni(self, dni_socio):
        x = self.session.query(Socio).filter(Socio.dni == dni_socio).first()
        return x

    def todos(self):
        return self.session.query(Socio).all()

    def borrar_todos(self):
        try:
            self.session.query(Socio).delete()
            self.session.commit()
        except exc.SQLAlchemyError:
            print("No se pudo borrar a los socios")
        else:
            return True

    def alta(self, socio):
        self.session.add(socio)
        self.session.commit()
        return socio

    def baja(self, id_socio):
        #if x != None:
        try:
            self.session.delete(self.session.query(Socio).get(id_socio))
            self.session.commit()
        except:
            return False
        return True
        #return False

    def modificacion(self, socio):
        x = self.session.query(Socio).get(socio.id_socio)
        if x is None:
            return None
        x.dni = socio.dni
        x.nombre = socio.nombre
        x.apellido = socio.apellido
        self.session.commit()
        return x


def pruebas():
    # alta
    datos = DatosSocio()
    try:
        datos.borrar_tabla()
    except:
        pass
    finally:
        datos.crear_tabla()
        socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
        assert socio.id_socio > 0

        # baja
        assert datos.baja(socio.id_socio) == True

        # buscar
        socio_2 = datos.alta(Socio(dni=22345671, nombre='Carlos', apellido='Perez'))
        assert datos.buscar(socio_2.id_socio) == socio_2

        # buscar dni
        socio_2 = datos.alta(Socio(dni=22345670, nombre='Carlos', apellido='Perez'))
        assert datos.buscar_dni(socio_2.dni) == socio_2

        # modificacion
        socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
        socio_3.nombre = 'Moria'
        socio_3.apellido = 'Casan'
        socio_3.dni = 13264587
        datos.modificacion(socio_3)
        socio_3_modificado = datos.buscar(socio_3.id_socio)
        assert socio_3_modificado.id_socio == socio_3.id_socio
        assert socio_3_modificado.nombre == 'Moria'
        assert socio_3_modificado.apellido == 'Casan'
        assert socio_3_modificado.dni == 13264587

        # todos
        assert len(datos.todos()) == 3

        # borrar todos
        datos.borrar_todos()
        assert len(datos.todos()) == 0
        datos.borrar_tabla()



if __name__ == '__main__':
    pruebas()
