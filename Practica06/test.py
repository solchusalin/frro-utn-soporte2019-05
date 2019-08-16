import unittest

from ejercicio01 import Socio
from capa_negocio import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 3)

        # ejecuto la logica
        socio = Socio(dni=1234567, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 4)

    def test_regla_1(self):
        #dni repetido
        repetido = Socio(dni=1234567, nombre='Juan', apellido='Perez')
        self.assertRaises(DniRepetido, self.ns.regla_1, repetido)

        #dni nuevo
        nuevo = Socio(dni=40115115, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_1(nuevo))

    def test_regla_2_nombre_menor_3(self):
        # nombre mayor a 3 caracteres
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Ju', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        # nombre menor a 15 caracteres
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juan Jose Ignacio', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # apellido mayor a 3 caracteres
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Pe')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        # apellido menor a 15 caracteres
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perez Martinez Infante')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        self.assertTrue(self.ns.regla_3())

    def test_baja(self):
        #no existe el id
        idInvalido = 10
        self.assertFalse(self.ns.baja(idInvalido))

        #el id existe
        idValido = 2
        self.assertTrue(self.ns.baja(idValido))

    def test_buscar(self):
        #no encuentra el id
        id = 10
        self.assertIsNone(self.ns.buscar(id))

        #encuentra el id
        id = 1
        self.assertIsNotNone(self.ns.buscar(id))

    def test_buscar_dni(self):
        #encuentra el dni
        dni = 1234567
        self.assertIsNotNone(self.ns.buscar_dni(dni))

        #no encuentra el dni
        dni = 4444444
        self.assertIsNone(self.ns.buscar_dni(dni))

    def test_todos(self):
        self.assertEqual(len(self.ns.todos()), 3)

    def test_modificacion(self):
        #modificacion ok
        valido = Socio(id=1, dni=123456, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.modificacion(valido))

        #longitud nombre invalida
        invalido = Socio(id=1, dni=123456, nombre='Juan Jose Ignacio', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.modificacion, invalido)
