import unittest
from FlizzBuzz import *

class Test_FlizzBuzz(unittest.TestCase):
    
    def setUp(self)
        self.instance=FizzBuzz()



    def test_affiche_sans_param(self):
        with self.subtest(self)
             self.assertEqual(self.instance.affiche(100),)
        with self.subtest(self):
            self.assertEqual(self.instance.affiche(3))

        self.assertEqual(self.instance.affiche(3))

if __name__ == '__main__':
    unittest main()