import unittest

from matricesEjercicio2 import filas

class TestCantidadDeFilasTest(unittest.TestCase):
    
    def test_cantidadDeFilasTest(self):
        m = [[1,2],[3,4]]
        self.assertAlmostEqual(filas(m),2)