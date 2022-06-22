import unittest
from mycomplex.mycomplex import MyComplex as MC

class TestMyComplexNumbers(unittest.TestCase):

    def test_repr(self):
        self.assertEqual(str(MC()), "0 + 0i")
        self.assertEqual(str(MC(2, 1.1)), "2 + 1.1i")
        self.assertEqual(str(MC(0, -0.0001)), "0 - 0.0001i")

    def test_eq(self):
        m = MC(2,3)
        self.assertEqual(m,m)
        self.assertEqual(MC(), MC())
        self.assertEqual(MC(2,-3), MC(2,-3))
        self.assertEqual(MC(2.8, 3.1), MC(2.8, 3.1))
        self.assertNotEqual(MC(2.8, 3.2), MC(2.8, 3.1))
        self.assertNotEqual(MC(2.9, 3.1), MC(2.8, 3.1))
        self.assertNotEqual(MC(0,1), MC(0,1.000001))


    def test_add(self):
        self.assertEqual(MC(2,3) + MC(-2.1, 4) , MC(-0.1, 7))
        self.assertEqual(MC(2,3) + MC(4, 0) , MC(6.0, 3))
        self.assertEqual(MC(2,3) + MC(4, 0) , MC(4, 0) + MC(2,3))
        self.assertEqual(MC() + MC() , MC(0, 0))
        self.assertEqual(MC(2,3) + 3, MC(5,3))
        self.assertNotEqual(MC() + MC() , MC(0, 2))
        self.assertNotEqual(MC() + MC() , MC(2, 0))
        self.assertNotEqual(MC(2,2) + 4, MC(2,6))

    def test_radd(self):
        self.assertEqual(3 + MC(2,3), MC(5,3))
        self.assertEqual(2 + MC(2,3) + 5, MC(9,3))
        self.assertEqual(2 + MC(2,3) + 5, 5 + MC(2,3) + 2)
        self.assertNotEqual(3 + MC(2,2), MC(2,5))

    def test_iadd(self):
        m = MC()
        n = m
        m += 10
        self.assertEqual(m, MC(10, 0))
        self.assertNotEqual(m, n)
        m += MC(-12.1, -12)
        self.assertEqual(m, MC(-2.1, -12))

    def test_mul(self):
        self.assertEqual(MC(2,3) * MC() , MC())
        self.assertEqual(MC() * MC(-4, -1) , MC())
        self.assertEqual(MC() * MC(), MC(0, 0))
        self.assertEqual(MC(1,0) * MC(0,1), MC(0, 1))
        self.assertEqual(MC(0,1) * MC(0,1), MC(-1, 0))
        self.assertEqual(MC(0,-1) * MC(-1,0), MC(0, 1))
        self.assertEqual(MC(1,2) * MC(3,4), MC(-5, 10))
        self.assertEqual(MC(1,1) * MC(2,1) * MC(1,3), MC(-8, 6))
        self.assertEqual(MC(1.1,2) * MC(2,5) * MC(100.2,-7.86), MC(100.2,-7.86) * MC(2,5) * MC(1.1,2))

        self.assertEqual(MC(1.1,2) * -3.5, MC(-3.85, -7))
        self.assertEqual(MC(1.1,2) * 0, MC())

    def test_rmul(self):
        self.assertEqual(-3.5 * MC(1.1,2), MC(-3.85, -7))
        self.assertEqual(0 * MC(1.1,2), MC())
        self.assertEqual(2 * MC(3,-4) * 11.1, MC(66.6, -88.8))

    def test_sub(self):
        self.assertEqual(MC(2,3) - MC(-2.1, 4) , MC(4.1, -1))
        self.assertEqual(MC(2,3) - MC(4, 0) , MC(-2, 3))
        self.assertEqual(MC() - MC() , MC(0, 0))
        self.assertEqual(MC() - 4 , MC(-4, 0))
        self.assertEqual(4 - MC(2.9,3), MC(1.1, -3))

    def test_conj(self):
        self.assertEqual(~MC(2.9,3), MC(2.9, -3))
        self.assertEqual(~MC(), MC())

    def test_inverse(self):
        self.assertEqual(MC(2,0).inverse(), MC(.5,0))
        self.assertEqual(MC(0,4).inverse(), MC(0,-.25))
        self.assertEqual(MC(3,4).inverse(), MC(3/25,-4/25))

    def test_truediv(self):
        m = MC(123.456, -7890.123)
        self.assertEqual(m / 1, m)
        self.assertEqual(m / MC(1,0), m)
        self.assertEqual(m / m, MC(1,0))
        self.assertEqual(m / m / m, 1 / m)
        self.assertEqual(MC(-30, -40) / MC(10,10), MC(-3.5, -0.5))

if __name__ == '__main__':
    unittest.main()