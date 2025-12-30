import unittest
from pctheory import pcset
from pctheory.pcset import SetClass
from pctheory.pitch import PitchClass
from pctheory import transformations
from pctheory.transformations import UTO

class UTOTestCase(unittest.TestCase):
    """
    Tests mod 12 UTOs.
    """
    def test_creation(self):
        """
        Tests making UTOs
        """
        u = UTO()
        self.assertEqual(u.T, 0)
        self.assertEqual(u.M, 1)
        u = UTO(5, 11)
        self.assertEqual(u.T, 5)
        self.assertEqual(u.M, 11)
        u = UTO("T5")
        self.assertEqual(u.T, 5)
        self.assertEqual(u.M, 1)
        u = UTO("T7I")
        self.assertEqual(u.T, 7)
        self.assertEqual(u.M, 11)
        u = UTO("T7M11")
        self.assertEqual(u.T, 7)
        self.assertEqual(u.M, 11)
        u = UTO("T2M")
        self.assertEqual(u.T, 2)
        self.assertEqual(u.M, 5)
        u = UTO("T2M5")
        self.assertEqual(u.T, 2)
        self.assertEqual(u.M, 5)
        u = UTO("T3MI")
        self.assertEqual(u.T, 3)
        self.assertEqual(u.M, 7)
        u = UTO("T3M7")
        self.assertEqual(u.T, 3)
        self.assertEqual(u.M, 7)
    
    def test_transform(self):
        """
        Tests applying UTO transformations
        """
        self.assertEqual(UTO("T5")(pcset.make_pcset12(2, 4, 9, 10)), pcset.make_pcset12(7, 9, 2, 3))
        self.assertEqual(UTO("T5M1")(pcset.make_pcset12(2, 4, 9, 10)), pcset.make_pcset12(7, 9, 2, 3))
        self.assertEqual(UTO("T5I")(pcset.make_pcset12(2, 4, 9, 10)), pcset.make_pcset12(3, 1, 8, 7))
        self.assertEqual(UTO("T5M11")(pcset.make_pcset12(2, 4, 9, 10)), pcset.make_pcset12(3, 1, 8, 7))
        self.assertEqual(UTO("T5M")(pcset.make_pcset12(2, 4, 9, 10)), pcset.make_pcset12(3, 1, 2, 7))
        self.assertEqual(UTO("T5M5")(pcset.make_pcset12(2, 4, 9, 10)), pcset.make_pcset12(3, 1, 2, 7))
        self.assertEqual(UTO("T5MI")(pcset.make_pcset12(2, 4, 9, 10)), pcset.make_pcset12(7, 9, 8, 3))
        self.assertEqual(UTO("T5M7")(pcset.make_pcset12(2, 4, 9, 10)), pcset.make_pcset12(7, 9, 8, 3))

    def test_inverse(self):
        """
        Tests UTO inverse computation
        """
        self.assertEqual(UTO("T4").inverse(), UTO("T8"))
        self.assertEqual(UTO("T3").inverse(), UTO("T9"))
        self.assertEqual(UTO("T6").inverse(), UTO("T6"))
        self.assertEqual(UTO("T3I").inverse(), UTO("T3I"))
        self.assertEqual(UTO("T5I").inverse(), UTO("T5I"))
        self.assertEqual(UTO("T2M5").inverse(), UTO("T2M5"))
        self.assertEqual(UTO("T5M5").inverse(), UTO("T11M5"))
        self.assertEqual(UTO("T3M7").inverse(), UTO("T3M7"))
        self.assertEqual(UTO("T8M7").inverse(), UTO("T4M7"))
    
    def test_comparison(self):
        """
        Tests UTO comparison
        """
        self.assertEqual(UTO("T4"), UTO(4))
        self.assertEqual(UTO("T4M1"), UTO(4))
        self.assertEqual(UTO("T4M"), UTO(4, 5))
        self.assertEqual(UTO("T4M5"), UTO(4, 5))
        self.assertEqual(UTO("T3M7"), UTO(3, 7))
        self.assertEqual(UTO("T3MI"), UTO(3, 7))
        self.assertEqual(UTO("T4M11"), UTO(4, 11))
        self.assertEqual(UTO("T4I"), UTO(4, 11))
        self.assertNotEqual(UTO("T4"), UTO("T4I"))
        self.assertNotEqual(UTO("T6"), UTO("T5"))
    
    def test_repr(self):
        """
        Tests UTO to string capability
        """
        self.assertEqual(str(UTO(4, 1)), "T4")
        self.assertEqual(repr(UTO(4, 1)), "T4")
        self.assertEqual(str(UTO(2, 11)), "T2M11")
        self.assertEqual(repr(UTO(2, 11)), "T2M11")

    def test_cycles(self):
        """
        Tests UTO cycle computation
        """
        self.assertEqual(UTO("T4").cycles(), ((0, 4, 8), (1, 5, 9), (2, 6, 10), (3, 7, 11)))
        self.assertEqual(UTO("T5").cycles(), ((0, 5, 10, 3, 8, 1, 6, 11, 4, 9, 2, 7),))
        self.assertEqual(UTO("T2").cycles(), ((0, 2, 4, 6, 8, 10), (1, 3, 5, 7, 9, 11)))
        self.assertEqual(UTO("T2I").cycles(), ((0, 2), (1,), (3, 11), (4, 10), (5, 9), (6, 8), (7,)))
        self.assertEqual(UTO("T9I").cycles(), ((0, 9), (1, 8), (2, 7), (3, 6), (4, 5), (10, 11)))

if __name__ == "__main__":
    unittest.main()