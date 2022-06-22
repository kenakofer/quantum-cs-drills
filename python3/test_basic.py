import unittest
import mycomplex.mycomplex as mc

class TestMyComplexNumbers(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(mc.add_one(3), 4)
        self.assertEqual(mc.add_one(-1), 0)

if __name__ == '__main__':
    unittest.main()