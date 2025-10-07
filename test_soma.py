import unittest
import math
from calculadora import soma

class TestSomaFunction(unittest.TestCase):
    """
    Suíte de testes para a função soma(), baseada nos princípios de
    Teste Funcional Sistêmico.
    """

    def test_soma_inteiros_positivos(self):
        """Testa a soma de dois inteiros positivos (ID 1)."""
        self.assertEqual(soma(5, 10), 15)

    def test_soma_inteiros_negativos(self):
        """Testa a soma de dois inteiros negativos (ID 2)."""
        self.assertEqual(soma(-5, -10), -15)

    def test_soma_sinais_mistos(self):
        """Testa a soma de números com sinais diferentes (ID 3)."""
        self.assertEqual(soma(20, -5), 15)

    def test_soma_sinais_mistos_anulacao(self):
        """Testa a soma de números simétricos que resulta em zero (ID 4)."""
        self.assertEqual(soma(10, -10), 0)

    def test_soma_com_elemento_neutro_zero(self):
        """Testa a propriedade do zero como elemento neutro (ID 5)."""
        self.assertEqual(soma(7, 0), 7)
        self.assertEqual(soma(0, 7), 7)

    def test_soma_ponto_flutuante(self):
        """Testa a soma de números de ponto flutuante (ID 6)."""
        self.assertEqual(soma(2.5, 3.5), 6.0)

    def test_limite_precisao_float(self):
        """Testa a imprecisão da aritmética de ponto flutuante (ID 7)."""
        # Usamos assertAlmostEqual pois 0.1 + 0.2 não é exatamente 0.3 em binário.
        self.assertAlmostEqual(soma(0.1, 0.2), 0.3)

    def test_limite_overflow_float(self):
        """Testa o comportamento de overflow para o tipo float (ID 8)."""
        # A soma de dois números float muito grandes deve resultar em infinito.
        self.assertEqual(soma(1.79e308, 1.0e308), math.inf)

    def test_robustez_tipo_invalido_string(self):
        """Testa a falha esperada ao somar um número com uma string (ID 9)."""
        with self.assertRaises(TypeError):
            soma(10, "texto")

    def test_robustez_entrada_nula(self):
        """Testa a falha esperada ao somar um número com None (ID 10)."""
        with self.assertRaises(TypeError):
            soma(5, None)

if __name__ == '__main__':
    # O verbosity=2 fornece um output mais detalhado.
    unittest.main(verbosity=2)
