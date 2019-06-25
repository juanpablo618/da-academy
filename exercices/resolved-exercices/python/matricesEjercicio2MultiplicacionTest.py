import unittest

from matricesEjercicio2 import multiplicaMatriz

class TestmultiplicaMatriz(unittest.TestCase):
    
    def test_multiplicaMatriz(self):
        j =[[1,2,-3],[4,0,-2]]
        u =[[3,1],[2,4],[-1,5]]

        self.assertAlmostEqual(multiplicaMatriz(j,u),[[10, -6], [14, -6]])
        
