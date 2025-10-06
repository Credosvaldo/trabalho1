import unittest
from calculadora import soma, subtracao, multiplicacao, divisao

class TestCalculadora(unittest.TestCase):
    def test_divisao(self):
        self.assertEqual(divisao(10, 2), 5)

        with self.assertRaises(ValueError):
            divisao(10, 0)

#Casos de Teste - Operação: Multiplicação
    def test_T1_positivos(self):
        """T1: Multiplicação de dois números positivos"""
        self.assertEqual(multiplicacao(3, 4), 12)

    def test_T2_negativos(self):
        """T2: Multiplicação de dois números negativos"""
        self.assertEqual(multiplicacao(-2, -3), 6)

    def test_T3_a_zero(self):
        """T3: Multiplicação com o primeiro número igual a zero"""
        self.assertEqual(multiplicacao(0, 5), 0)

    def test_T4_b_zero(self):
        """T4: Multiplicação com o segundo número igual a zero"""
        self.assertEqual(multiplicacao(7, 0), 0)

    def test_T5_positivo_por_negativo(self):
        """T5: Multiplicação de número positivo por número negativo"""
        self.assertEqual(multiplicacao(5, -2), -10)

    def test_T6_negativo_por_positivo(self):
        """T6: Multiplicação de número negativo por número positivo"""
        self.assertEqual(multiplicacao(-3, 2), -6)


if __name__ == "__main__":
    unittest.main()
