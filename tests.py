import unittest
from calculadora import soma, subtracao, multiplicacao, divisao

class TestCalculadora(unittest.TestCase):
    def test_divisao(self):
        self.assertEqual(divisao(10, 2), 5)

        with self.assertRaises(ValueError):
            divisao(10, 0)


if __name__ == "__main__":
    unittest.main()
