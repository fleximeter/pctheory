import unittest
from pctheory import pcset, pcseg
from pctheory.pcset import SetClass
from pctheory.pitch import PitchClass
from pctheory import transformations
from pctheory.transformations import OTO, UTO

class OTO12TestCase(unittest.TestCase):
    """
    Tests mod 12 OTOs.
    """
    def test_creation(self):
        """
        Tests making OTOs
        """
        o = OTO()
        self.assertEqual(o.T, 0)
        self.assertEqual(o.R, False)
        self.assertEqual(o.M, 1)
        o = OTO(5, True, 11)
        self.assertEqual(o.T, 5)
        self.assertEqual(o.R, True)
        self.assertEqual(o.M, 11)
        o = OTO("T5")
        self.assertEqual(o.T, 5)
        self.assertEqual(o.R, False)
        self.assertEqual(o.M, 1)
        o = OTO("T5R")
        self.assertEqual(o.T, 5)
        self.assertEqual(o.R, True)
        self.assertEqual(o.M, 1)
        o = OTO("T5RI")
        self.assertEqual(o.T, 5)
        self.assertEqual(o.R, True)
        self.assertEqual(o.M, 11)
        o = OTO("T5RM11")
        self.assertEqual(o.T, 5)
        self.assertEqual(o.R, True)
        self.assertEqual(o.M, 11)
        o = OTO("T5I")
        self.assertEqual(o.T, 5)
        self.assertEqual(o.R, False)
        self.assertEqual(o.M, 11)
        o = OTO("T5M11")
        self.assertEqual(o.T, 5)
        self.assertEqual(o.R, False)
        self.assertEqual(o.M, 11)
        o = OTO("T5RM5")
        self.assertEqual(o.T, 5)
        self.assertEqual(o.R, True)
        self.assertEqual(o.M, 5)
        o = OTO("T5RM")
        self.assertEqual(o.T, 5)
        self.assertEqual(o.R, True)
        self.assertEqual(o.M, 5)
        o = OTO("T5RM7")
        self.assertEqual(o.T, 5)
        self.assertEqual(o.R, True)
        self.assertEqual(o.M, 7)
        o = OTO("T5RMI")
        self.assertEqual(o.T, 5)
        self.assertEqual(o.R, True)
        self.assertEqual(o.M, 7)
        with self.assertRaises(ValueError):
            OTO("T22")
        with self.assertRaises(ValueError):
            OTO("T2RR")
        with self.assertRaises(ValueError):
            OTO("T2MIX")
        with self.assertRaises(TypeError):
            OTO(5, 4, 9)
    
    def test_comparison(self):
        """
        Tests OTO comparison
        """
        self.assertEqual(OTO("T5RI"), OTO(5, True, 11))
        self.assertEqual(OTO("T5R"), OTO(5, True, 1))
        self.assertEqual(OTO("T5"), OTO(5, False, 1))
        self.assertEqual(OTO("T5I"), OTO(5, False, 11))
        self.assertNotEqual(OTO("T5RI"), OTO(5, False, 11))

    def test_repr(self):
        """
        Tests OTO to string capability
        """
        self.assertEqual(str(OTO(4, False, 1)), "T4")
        self.assertEqual(repr(OTO(4, True, 1)), "T4R")
        self.assertEqual(str(OTO(2, False, 11)), "T2M11")
        self.assertEqual(repr(OTO(2, True, 11)), "T2RM11")

    def test_transform(self):
        """
        Tests applying OTO transformations
        """
        self.assertEqual(OTO("T5")(pcseg.make_pcseg12(2, 4, 9, 10)), pcseg.make_pcseg12(7, 9, 2, 3))
        self.assertEqual(OTO("T5R")(pcseg.make_pcseg12(2, 4, 9, 10)), pcseg.make_pcseg12(3, 2, 9, 7))
        self.assertEqual(OTO("T5RI")(pcseg.make_pcseg12(2, 4, 9, 10)), pcseg.make_pcseg12(7, 8, 1, 3))
        self.assertEqual(OTO("T5RM11")(pcseg.make_pcseg12(2, 4, 9, 10)), pcseg.make_pcseg12(7, 8, 1, 3))
        self.assertEqual(OTO("T5RM")(pcseg.make_pcseg12(2, 4, 9, 10)), pcseg.make_pcseg12(7, 2, 1, 3))
        self.assertEqual(OTO("T5RM5")(pcseg.make_pcseg12(2, 4, 9, 10)), pcseg.make_pcseg12(7, 2, 1, 3))

    def test_corpus(self):
        """
        Tests for retrieving the OTO corpus
        """
        corpus = transformations.get_otos12()
        self.assertEqual(len(corpus), 12 * 8)
        for name, oto in corpus.items():
            self.assertEqual(oto, OTO(name))

    def test_find_otos(self):
        """
        Tests the OTO finder
        """
        # Find complete transformations
        self.assertEqual(transformations.find_otos(pcseg.make_pcseg12(1, 2, 4, 0), pcseg.make_pcseg12(5, 6, 8, 4)), {OTO("T4")})
        self.assertEqual(transformations.find_otos(pcseg.make_pcseg12(1, 2, 3, 2, 1), pcseg.make_pcseg12(2, 3, 4, 3, 2)), {OTO("T1"), OTO("T1R")})
        self.assertEqual(transformations.find_otos(pcseg.make_pcseg12(1, 2, 3, 9, 10, 11), pcseg.make_pcseg12(4, 5, 6, 0, 1, 2)), {OTO("T3"), OTO("T3RI")})
        self.assertEqual(transformations.find_otos(pcseg.make_pcseg12(0, 3, 0, 6, 0, 3, 0), pcseg.make_pcseg12(1, 4, 1, 7, 1, 4, 1)),
            {OTO("T1"), OTO("T1R"), OTO("T1M5"), OTO("T1RM5")})
        self.assertEqual(transformations.find_otos(pcseg.make_pcseg12(0, 2, 8, 2, 4), pcseg.make_pcseg12(3, 5, 11, 5, 7)),
            {OTO("T3"), OTO("T3M7"), OTO("T7RM5"), OTO("T7RM11")})
        
        # Find incomplete transformations
        self.assertEqual(transformations.find_otos(pcseg.make_pcseg12(1, 2, 4, 0), pcseg.make_pcseg12(5, 6)), {OTO("T4"), OTO("T7RI")})
        self.assertEqual(transformations.find_otos(pcseg.make_pcseg12(1, 2, 4, 0), pcseg.make_pcseg12(4, 6)), {OTO("T2"), OTO("T8RI"), OTO("T8RM5"), OTO("T2M7")})

class UTO12TestCase(unittest.TestCase):
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
        with self.assertRaises(ValueError):
            UTO("T22")
        with self.assertRaises(ValueError):
            UTO("T2R")
        with self.assertRaises(ValueError):
            UTO("T2MIX")
        with self.assertRaises(TypeError):
            UTO(5, 'a')
    
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

    def test_corpus(self):
        """
        Tests for retrieving the UTO corpus
        """
        corpus = transformations.get_utos12()
        self.assertEqual(len(corpus), 12 * 4)
        for name, uto in corpus.items():
            self.assertEqual(uto, UTO(name))
    
    def test_left_multiply(self):
        """
        Tests left-multiplication of UTOs
        """
        self.assertEqual(transformations.left_multiply_utos(UTO("T5"), UTO("T8")), UTO("T1"))
        self.assertEqual(transformations.left_multiply_utos([UTO("T5"), UTO("T8")]), UTO("T1"))
        self.assertEqual(transformations.left_multiply_utos(UTO("T5"), UTO("T8I")), UTO("T1I"))
        self.assertEqual(transformations.left_multiply_utos([UTO("T5"), UTO("T8I")]), UTO("T1I"))
        self.assertEqual(transformations.left_multiply_utos(UTO("T4I"), UTO("T4I")), UTO("T0"))
        self.assertEqual(transformations.left_multiply_utos([UTO("T4I"), UTO("T4I")]), UTO("T0"))
        self.assertEqual(transformations.left_multiply_utos(UTO("T5I"), UTO("T8I")), UTO("T9"))
        self.assertEqual(transformations.left_multiply_utos([UTO("T5I"), UTO("T8I")]), UTO("T9"))
        self.assertEqual(transformations.left_multiply_utos(UTO("T5I"), UTO("T2"), UTO("T8I")), UTO("T7"))
        self.assertEqual(transformations.left_multiply_utos([UTO("T5I"), UTO("T2"), UTO("T8I")]), UTO("T7"))
    
    def test_find_utos(self):
        """
        Tests the UTO finder
        """
        # Find complete transformations
        self.assertEqual(transformations.find_utos(pcset.make_pcset12(3, 4, 8, 9), pcset.make_pcset12(5, 6, 10, 11)), 
            {UTO("T2"), UTO("T2M11"), UTO("T2M5"), UTO("T2M7")})
        self.assertEqual(transformations.find_utos(pcset.make_pcset12(3, 7, 8, 9), pcset.make_pcset12(1, 2, 3, 7)), 
            {UTO("T10M11")})
        self.assertEqual(transformations.find_utos(pcset.make_pcset12(1, 2, 3), pcset.make_pcset12(4, 5, 6)), 
            {UTO("T3"), UTO("T7M11")})
        self.assertEqual(transformations.find_utos(pcset.make_pcset12(1, 2, 5, 6, 9, 10), pcset.make_pcset12(3, 4, 7, 8, 11, 0)), 
            {UTO("T2"), UTO("T6"), UTO("T10"), UTO("T1M11"), UTO("T5M11"), UTO("T9M11"),
            UTO("T2M5"), UTO("T6M5"), UTO("T10M5"), UTO("T1M7"), UTO("T5M7"), UTO("T9M7")})
        self.assertEqual(transformations.find_utos(pcset.make_pcset12(3, 7, 8, 9), pcset.make_pcset12(1, 0, 3, 7)), 
            set())
        
        # Find incomplete transformations
        self.assertEqual(transformations.find_utos(pcset.make_pcset12(3, 7, 8, 9), pcset.make_pcset12(4, 8)), 
            {UTO("T1"), UTO("T11M11"), UTO("T5M5"), UTO("T7M7")})
        self.assertEqual(transformations.find_utos(pcset.make_pcset12(3, 6, 4, 7), pcset.make_pcset12(5, 8)), 
            {UTO("T1"), UTO("T2"), UTO("T0M11"), UTO("T11M11"), UTO("T2M5"), UTO("T9M5"), UTO("T4M7"), UTO("T11M7")})

if __name__ == "__main__":
    unittest.main()