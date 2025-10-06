import unittest
from calculadora import soma, subtracao, multiplicacao, divisao

class TestCalculadora(unittest.TestCase):
    def test_divisao(self):
        self.assertEqual(divisao(10, 2), 5)

        with self.assertRaises(ValueError):
            divisao(10, 0)

#Casos de Teste - Operação: Multiplicação
    def test_multiplicacao_positivos(self):
        self.assertEqual(multiplicacao(3, 4), 12)

    def test_multiplicacao_com_zero(self):
        self.assertEqual(multiplicacao(0, 5), 0)

    def test_multiplicacao_negativos(self):
        self.assertEqual(multiplicacao(-2, -3), 6)

    def test_multiplicacao_positivo_negativo(self):
        self.assertEqual(multiplicacao(5, -2), -10)


if __name__ == "__main__":
    unittest.main()
