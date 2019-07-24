#Implementar los casos de prueba descriptos.

import unittest

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        # valida regla
        valido = Socio(dni=12345679, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_1(valido))
        self.ns.alta(valido)

        # mismo socio despues de agregarlo
        invalido = Socio(dni=12345679, nombre='Juan', apellido='Perez')
        self.assertRaises(DniRepetido, self.ns.regla_1, invalido)

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Josecarlosjuanricardo', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Per')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perezgomezcenturionricardo')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        self.assertTrue(self.ns.regla_3)
        for i in range(200):
            self.ns.alta(Socio(dni=i, nombre='Juan', apellido='Perez'))

        self.assertRaises(MaximoAlcanzado, self.ns.regla_3)

    def test_baja(self):
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        assert(len(self.ns.todos()))==1

        self.assertTrue(self.ns.baja(valido.id_socio))
        assert(len(self.ns.todos()))==0

        self.assertFalse(self.ns.baja(valido.id_socio))

    def test_buscar(self):
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)

        assert self.ns.buscar(valido.id_socio) == valido

    def test_buscar_dni(self):
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)

        assert self.ns.buscar_dni(valido.dni) == valido

    def test_todos(self):
        assert len(self.ns.todos()) == 0
        for i in range(20):
            self.ns.alta(Socio(dni=i, nombre='Juan', apellido='Perez'))

        assert len(self.ns.todos()) == 20

    def test_modificacion(self):
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)

        self.assertTrue(self.ns.modificacion(Socio(id_socio=1,dni=12345678, nombre='Juana', apellido='Perez')))

        #Falla la regla 2 por el nombre
        self.assertFalse(self.ns.modificacion(Socio(id_socio=1,dni=12345678, nombre='Jua', apellido='Perez')))

        #Falla la regla 2 por el apellido
        self.assertFalse(self.ns.modificacion(Socio(id_socio=1,dni=12345678, nombre='Juana', apellido='Per')))
