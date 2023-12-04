import unittest
from src.logica.Bonificaccion import calcular_bonificaciones, calcular_remuneracion_computable
class PruebaBonificaciones(unittest.TestCase):
    def test_calculo_total_bonificacion(self):
        # Arrange
        horas_extras = 0  # por 0 horas extra
        bonificacion_suplementaria = 30.90
        bonificacion_movilidad = 1000
        resultado_esperado = 1030.90

        resultado_actual = calcular_bonificaciones(horas_extras + bonificacion_suplementaria + bonificacion_movilidad)

        self.assertEqual(resultado_esperado, resultado_actual)

    def test_calculo_remuneracion_computable(self):
        # Arrange
        sueldo_base = 1030
        bonificacion_movilidad = 1000
        bonificacion_suplementaria = 30.90
        resultado_esperado = 2060.90

        resultado_actual = calcular_remuneracion_computable(sueldo_base + bonificacion_movilidad + bonificacion_suplementaria)

        self.assertEqual(resultado_esperado, resultado_actual)

if __name__ == '__main__':
    unittest.main()
