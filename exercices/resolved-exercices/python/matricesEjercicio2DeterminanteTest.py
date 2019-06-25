import unittest

from matricesEjercicio2 import determinante

class TestDeterminanteMatriz(unittest.TestCase):
    
    def test_determinante(self):
        m = [[1,2],[3,4]]
        self.assertAlmostEqual(determinante(m),-2.0)
        
