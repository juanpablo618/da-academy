import unittest

from matricesEjercicio2 import columnas

class TestCantidadDeColumnasTest(unittest.TestCase):
    
    def test_cantidadDeColumnasTest(self):
        m = [[1,2],[3,4]]
        self.assertAlmostEqual(columnas(m),2)
        
