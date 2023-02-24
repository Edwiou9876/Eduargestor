import csv
import helpers
import config
import copy
import unittest
import database as db

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('15J','Juan','Perez'),
            db.Cliente('23H', 'Alvaro','Velez'),
            db.Cliente('45P', 'Daniel', 'Parra')
        ]

    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar('15J')
        cliente_inexistente = db.Clientes.buscar('99X')

        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)

    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('42K','Juan','Uribe')
        self.assertEqual(len(db.Clientes.lista),4)
        self.assertEqual(nuevo_cliente.dni,'42K')
        self.assertEqual(nuevo_cliente.nombre,'Juan')
        self.assertEqual(nuevo_cliente.apellido,'Uribe')
    
    def test_modificar_cliente(self):
        cliente_a_buscar = copy.copy(db.Clientes.buscar('15J'))
        cliente_modificado = db.Clientes.modificar('15J','Ana','Perez')

        self.assertEqual(cliente_a_buscar.nombre, 'Juan')
        self.assertEqual(cliente_modificado.nombre,'Ana')

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('23H')
        cliente_rebuscado = db.Clientes.buscar('23H')
        self.assertEqual(cliente_borrado.dni,'23H')
        self.assertIsNone(cliente_rebuscado)

    def test_dni_valido(self):
        self.assertFalse(helpers.dni_validacion('F35',db.Clientes.lista))
        self.assertTrue(helpers.dni_validacion('35F',db.Clientes.lista))

    def test_escritura_csv(self):
        db.Clientes.borrar("23H")
        db.Clientes.borrar("15J")
        db.Clientes.modificar("45P",'Mariana',"Garcia")

        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            dni, nombre, apellido = next(reader)

        self.assertEqual(dni,'45P')
        self.assertEqual(nombre,'Mariana')
        self.assertEqual(apellido,'Garcia')

