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


# Casos de Teste - Operação: Subtração 
    def test_S1_equal_operands(self):
        """S1: Subtração de dois operandos iguais deve resultar em zero"""
        self.assertEqual(subtracao(5, 5), 0)

    def test_S2_floats_precision(self):
        """S2: Subtração com floats (usar assertAlmostEqual para precisão)"""
        self.assertAlmostEqual(subtracao(2.5, 1.1), 1.4, places=7)

    def test_S3_large_numbers(self):
        """S3: Subtração com números grandes"""
        self.assertEqual(subtracao(10**9, 1), 999999999)

    def test_S4_small_minus_large(self):
        """S4: Subtração onde o primeiro operando é menor que o segundo"""
        self.assertEqual(subtracao(1, 100), -99)

    def test_S5_negative_and_float(self):
        """S5: Subtração envolvendo números negativos e floats"""
        self.assertAlmostEqual(subtracao(-2.5, -1.25), -1.25, places=7)

    def test_S6_antisymmetry(self):
        """S6: Propriedade antissimétrica: a - b == -(b - a)"""
        a, b = 7, 3
        self.assertEqual(subtracao(a, b), -subtracao(b, a))

# Casos de Teste - Operação: potencia
    def test_P1_positive_exponents(self):
        """P1: Potência com expoentes positivos"""
        self.assertEqual(potencia(2, 3), 8)

    def test_P2_zero_exponent(self):
        """P2: Qualquer número elevado a zero deve ser 1"""
        self.assertEqual(potencia(5, 0), 1)

    def test_P3_negative_exponent(self):
        """P3: Potência com expoentes negativos"""
        self.assertAlmostEqual(potencia(2, -2), 0.25, places=7)

    def test_P4_fractional_exponent(self):
        """P4: Potência com expoentes fracionários"""
        self.assertAlmostEqual(potencia(9, 0.5), 3.0, places=7)

    def test_P5_negative_base_even_exponent(self):
        """P5: Base negativa com expoente par"""
        self.assertEqual(potencia(-2, 4), 16)

    def test_P6_negative_base_odd_exponent(self):
        """P6: Base negativa com expoente ímpar"""
        self.assertEqual(potencia(-2, 3), -8)

# Casos de Teste - Operação: raiz_quadrada
    def test_R1_positive_number(self):
        """R1: Raiz quadrada de número positivo"""
        self.assertAlmostEqual(raiz_quadrada(16), 4.0, places=7)
    def test_R2_zero(self):
        """R2: Raiz quadrada de zero"""
        self.assertEqual(raiz_quadrada(0), 0)
    def test_R3_negative_number(self):
        """R3: Raiz quadrada de número negativo deve levantar ValueError"""
        with self.assertRaises(ValueError):
            raiz_quadrada(-4)
    def test_R4_fractional_number(self):
        """R4: Raiz quadrada de número fracionário"""
        self.assertAlmostEqual(raiz_quadrada(2.25), 1.5, places=7)
    def test_R5_large_number(self):
        """R5: Raiz quadrada de número grande"""
        self.assertAlmostEqual(raiz_quadrada(10**6), 1000.0, places=7)
    def test_R6_perfect_square(self):
        """R6: Raiz quadrada de número que é um quadrado perfeito"""
        self.assertEqual(raiz_quadrada(49), 7)
    

if __name__ == "__main__":
    unittest.main()
