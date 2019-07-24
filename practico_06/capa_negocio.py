#Implementar los metodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio

class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):

        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.datos.buscar(id_socio)

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.datos.buscar_dni(dni_socio)

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        todos=self.datos.todos()
        return todos

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        try:
            if self.regla_1(socio) == True and self.regla_2(socio) == True and self.regla_3() == True:
                self.datos.alta(socio)
                return True
        except DniRepetido as e:
            print(e)
        except LongitudInvalida as e:
            print(e)
        except MaximoAlcanzado as e:
            print(e)
        return False

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        resultado=self.datos.baja(id_socio)
        return resultado

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        try:
            self.regla_2(socio)
            self.datos.modificacion(socio)
        except LongitudInvalida as e:
            print(e)
            return False
        return True

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        dni = self.datos.buscar_dni(socio.dni)
        if dni is not None:
            raise DniRepetido('Ya se encuentra el dni')
            return False
        return True

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        long_nombre = len(socio.nombre)
        long_apellido = len(socio.apellido)
        if long_nombre> self.MIN_CARACTERES and long_nombre <self.MAX_CARACTERES:
            if long_apellido > self.MIN_CARACTERES and long_apellido < self.MAX_CARACTERES:
                return True
            else:
                raise LongitudInvalida("Apellido debe tener entre "+str(self.MIN_CARACTERES+1)+" y "+ str(self.MAX_CARACTERES-1))
        else:
            raise LongitudInvalida("Nombre debe tener entre "+str(self.MIN_CARACTERES+1)+" y "+ str(self.MAX_CARACTERES-1))
        return False

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        todos = self.datos.todos()
        if len(todos) == self.MAX_SOCIOS:
            raise MaximoAlcanzado("Se ha alcanzado el máximo de socios")
            return False
        return True
