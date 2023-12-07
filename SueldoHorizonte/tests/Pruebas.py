import unittest
from io import StringIO
from unittest.mock import patch

# Importa tus funciones del código principal
from SueldoHorizonte.src.logica.Calculos import ingreso_datos, calcular_bonificaciones, calcular_descuentos, calcular_sueldo_a_pagar

class TestSueldoHorizonte(unittest.TestCase):

    @patch('builtins.input', side_effect=['Juan', '2000.0', '2', '10', '3.0'])
    def test_ingreso_datos(self, mock_input):
        nombre, sueldo, faltas, tardanza, extras = ingreso_datos()
        self.assertEqual(nombre, 'Juan')
        self.assertAlmostEqual(sueldo, 2000.0)
        self.assertEqual(faltas, 2)
        self.assertEqual(tardanza, 10)
        self.assertAlmostEqual(extras, 3.0)

if __name__ == '__main__':
    unittest.main()
