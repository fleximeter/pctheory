import unittest
from pctheory import pcset
from pctheory.pitch import Pitch, PitchClass

class PitchClassTestCase(unittest.TestCase):
    """
    Unit tests for PitchClass
    """
    def test_creation_mod12(self):
        """
        Tests basic mod 12 pitch class creation.
        In particular, tests mod for positive and negative numbers outside the range.
        """
        pc1 = PitchClass()
        self.assertEqual(pc1.pc, 0)
        self.assertEqual(pc1.mod, 12)
        self.assertEqual(pc1.pc_str, '0')
        pc1 = PitchClass(5)
        self.assertEqual(pc1.pc, 5)
        self.assertEqual(pc1.mod, 12)
        self.assertEqual(pc1.pc_str, '5')
        pc1 = PitchClass(0, 12)
        self.assertEqual(pc1.pc, 0)
        self.assertEqual(pc1.mod, 12)
        self.assertEqual(pc1.pc_str, '0')
        pc1 = PitchClass(5, 12)
        self.assertEqual(pc1.pc, 5)
        self.assertEqual(pc1.mod, 12)
        self.assertEqual(pc1.pc_str, '5')
        pc1 = PitchClass(12)
        self.assertEqual(pc1.pc, 0)
        self.assertEqual(pc1.mod, 12)
        self.assertEqual(pc1.pc_str, '0')
        pc1 = PitchClass(12, 12)
        self.assertEqual(pc1.pc, 0)
        self.assertEqual(pc1.mod, 12)
        self.assertEqual(pc1.pc_str, '0')
        pc1 = PitchClass(15)
        self.assertEqual(pc1.pc, 3)
        self.assertEqual(pc1.mod, 12)
        self.assertEqual(pc1.pc_str, '3')
        pc1 = PitchClass(15, 12)
        self.assertEqual(pc1.pc, 3)
        self.assertEqual(pc1.mod, 12)
        self.assertEqual(pc1.pc_str, '3')
        pc1 = PitchClass(-1)
        self.assertEqual(pc1.pc, 11)
        self.assertEqual(pc1.mod, 12)
        self.assertEqual(pc1.pc_str, 'B')
        pc1 = PitchClass(-4)
        self.assertEqual(pc1.pc, 8)
        self.assertEqual(pc1.mod, 12)
        self.assertEqual(pc1.pc_str, '8')
        pc1 = PitchClass(-10)
        self.assertEqual(pc1.pc, 2)
        self.assertEqual(pc1.mod, 12)
        self.assertEqual(pc1.pc_str, '2')
        pc1 = PitchClass(-33)
        self.assertEqual(pc1.pc, 3)
        self.assertEqual(pc1.mod, 12)
        self.assertEqual(pc1.pc_str, '3')
    
    def test_creation_mod24(self):
        """
        Tests basic mod 24 pitch class creation.
        In particular, tests mod for positive and negative numbers outside the range.
        """
        pc1 = PitchClass(0, 24)
        self.assertEqual(pc1.pc, 0)
        self.assertEqual(pc1.mod, 24)
        self.assertEqual(pc1.pc_str, '00')
        pc1 = PitchClass(5, 24)
        self.assertEqual(pc1.pc, 5)
        self.assertEqual(pc1.mod, 24)
        self.assertEqual(pc1.pc_str, '05')
        pc1 = PitchClass(24, 24)
        self.assertEqual(pc1.pc, 0)
        self.assertEqual(pc1.mod, 24)
        self.assertEqual(pc1.pc_str, '00')
        pc1 = PitchClass(27, 24)
        self.assertEqual(pc1.pc, 3)
        self.assertEqual(pc1.mod, 24)
        self.assertEqual(pc1.pc_str, '03')
        pc1 = PitchClass(-1, 24)
        self.assertEqual(pc1.pc, 23)
        self.assertEqual(pc1.mod, 24)
        self.assertEqual(pc1.pc_str, '23')
        pc1 = PitchClass(-4, 24)
        self.assertEqual(pc1.pc, 20)
        self.assertEqual(pc1.mod, 24)
        self.assertEqual(pc1.pc_str, '20')
        pc1 = PitchClass(-25, 24)
        self.assertEqual(pc1.pc, 23)
        self.assertEqual(pc1.mod, 24)
        self.assertEqual(pc1.pc_str, '23')
        pc1 = PitchClass(-50, 24)
        self.assertEqual(pc1.pc, 22)
        self.assertEqual(pc1.mod, 24)
        self.assertEqual(pc1.pc_str, '22')

    def test_math_mod12(self):
        """
        Tests mod 12 math operations
        """
        # Addition
        self.assertEqual(PitchClass(5) + 3, PitchClass(8))
        self.assertEqual(PitchClass(5) + PitchClass(3), PitchClass(8))
        self.assertEqual(PitchClass(5) + 7, PitchClass(0))
        self.assertEqual(PitchClass(5) + PitchClass(7), PitchClass(0))
        self.assertEqual(PitchClass(5) + 18, PitchClass(11))
        self.assertEqual(PitchClass(5) + PitchClass(18), PitchClass(11))
        self.assertEqual(PitchClass(5) + -9, PitchClass(8))
        self.assertEqual(PitchClass(5) + PitchClass(-9), PitchClass(8))

        # Subtraction
        self.assertEqual(PitchClass(5) - 4, PitchClass(1))
        self.assertEqual(PitchClass(5) - PitchClass(4), PitchClass(1))
        self.assertEqual(PitchClass(5) - 0, PitchClass(5))
        self.assertEqual(PitchClass(5) - PitchClass(0), PitchClass(5))
        self.assertEqual(PitchClass(5) - 13, PitchClass(4))
        self.assertEqual(PitchClass(5) - PitchClass(13), PitchClass(4))
        self.assertEqual(PitchClass(5) - -9, PitchClass(2))
        self.assertEqual(PitchClass(5) - PitchClass(-9), PitchClass(2))
        self.assertEqual(PitchClass(5) - 23, PitchClass(6))

        # Multiplication
        self.assertEqual(PitchClass(5) * 2, PitchClass(10))
        self.assertEqual(PitchClass(5) * PitchClass(2), PitchClass(10))
        self.assertEqual(PitchClass(5) * 1, PitchClass(5))
        self.assertEqual(PitchClass(5) * PitchClass(1), PitchClass(5))
        self.assertEqual(PitchClass(5) * 5, PitchClass(1))
        self.assertEqual(PitchClass(5) * PitchClass(5), PitchClass(1))
        self.assertEqual(PitchClass(4) * 5, PitchClass(8))
        self.assertEqual(PitchClass(4) * PitchClass(5), PitchClass(8))
        self.assertEqual(PitchClass(5) * 7, PitchClass(11))
        self.assertEqual(PitchClass(5) * PitchClass(7), PitchClass(11))
        self.assertEqual(PitchClass(2) * 7, PitchClass(2))
        self.assertEqual(PitchClass(2) * PitchClass(7), PitchClass(2))
        self.assertEqual(PitchClass(5) * 11, PitchClass(7))
        self.assertEqual(PitchClass(5) * PitchClass(11), PitchClass(7))
        self.assertEqual(PitchClass(8) * 11, PitchClass(4))
        self.assertEqual(PitchClass(8) * PitchClass(11), PitchClass(4))
        self.assertEqual(PitchClass(5) * -1, PitchClass(7))
        self.assertEqual(PitchClass(5) * PitchClass(-1), PitchClass(7))
        self.assertEqual(PitchClass(8) * -1, PitchClass(4))
        self.assertEqual(PitchClass(8) * PitchClass(-1), PitchClass(4))
        self.assertEqual(PitchClass(5) * 23, PitchClass(7))
        self.assertEqual(PitchClass(5) * PitchClass(23), PitchClass(7))
        self.assertEqual(PitchClass(5) * -22, PitchClass(10))
        self.assertEqual(PitchClass(5) * PitchClass(-22), PitchClass(10))
    
    def test_comparison_mod12(self):
        """
        Tests pitch class comparison
        """
        self.assertTrue(PitchClass(5) == PitchClass(5))
        self.assertTrue(PitchClass(14) == PitchClass(14))
        self.assertTrue(PitchClass(-5) == PitchClass(-5))
        self.assertTrue(PitchClass(5) <= PitchClass(5))
        self.assertTrue(PitchClass(5) <= PitchClass(7))
        self.assertTrue(PitchClass(5) <= PitchClass(-1))
        self.assertTrue(PitchClass(5) < PitchClass(7))
        self.assertTrue(PitchClass(5) < PitchClass(-1))
        self.assertTrue(PitchClass(5) >= PitchClass(5))
        self.assertTrue(PitchClass(5) >= PitchClass(3))
        self.assertTrue(PitchClass(5) >= PitchClass(13))
        self.assertTrue(PitchClass(5) > PitchClass(3))
        self.assertTrue(PitchClass(5) > PitchClass(13))
        self.assertTrue(PitchClass(5) != PitchClass(4))

class PitchTestCase(unittest.TestCase):
    """
    Unit tests for Pitch
    """
    def test_creation_mod12(self):
        """
        Tests basic mod 12 pitch creation.
        """
        p1 = Pitch()
        self.assertEqual(p1.p, 0)
        self.assertEqual(p1.pc, 0)
        self.assertEqual(p1.mod, 12)
        self.assertEqual(p1.pc_str, '0')
        p1 = Pitch(5)
        self.assertEqual(p1.p, 5)
        self.assertEqual(p1.pc, 5)
        self.assertEqual(p1.mod, 12)
        self.assertEqual(p1.pc_str, '5')
        p1 = Pitch(0, 12)
        self.assertEqual(p1.p, 0)
        self.assertEqual(p1.pc, 0)
        self.assertEqual(p1.mod, 12)
        self.assertEqual(p1.pc_str, '0')
        p1 = Pitch(5, 12)
        self.assertEqual(p1.p, 5)
        self.assertEqual(p1.pc, 5)
        self.assertEqual(p1.mod, 12)
        self.assertEqual(p1.pc_str, '5')
        p1 = Pitch(12)
        self.assertEqual(p1.p, 12)
        self.assertEqual(p1.pc, 0)
        self.assertEqual(p1.mod, 12)
        self.assertEqual(p1.pc_str, '0')
        p1 = Pitch(12, 12)
        self.assertEqual(p1.p, 12)
        self.assertEqual(p1.pc, 0)
        self.assertEqual(p1.mod, 12)
        self.assertEqual(p1.pc_str, '0')
        p1 = Pitch(15)
        self.assertEqual(p1.p, 15)
        self.assertEqual(p1.pc, 3)
        self.assertEqual(p1.mod, 12)
        self.assertEqual(p1.pc_str, '3')
        p1 = Pitch(15, 12)
        self.assertEqual(p1.p, 15)
        self.assertEqual(p1.pc, 3)
        self.assertEqual(p1.mod, 12)
        self.assertEqual(p1.pc_str, '3')
        p1 = Pitch(-1)
        self.assertEqual(p1.p, -1)
        self.assertEqual(p1.pc, 11)
        self.assertEqual(p1.mod, 12)
        self.assertEqual(p1.pc_str, 'B')
        p1 = Pitch(-4)
        self.assertEqual(p1.p, -4)
        self.assertEqual(p1.pc, 8)
        self.assertEqual(p1.mod, 12)
        self.assertEqual(p1.pc_str, '8')
        p1 = Pitch(-10)
        self.assertEqual(p1.p, -10)
        self.assertEqual(p1.pc, 2)
        self.assertEqual(p1.mod, 12)
        self.assertEqual(p1.pc_str, '2')
        p1 = Pitch(-33)
        self.assertEqual(p1.p, -33)
        self.assertEqual(p1.pc, 3)
        self.assertEqual(p1.mod, 12)
        self.assertEqual(p1.pc_str, '3')

    def test_math_mod12(self):
        """
        Tests mod 12 math operations
        """
        # Addition
        self.assertEqual(Pitch(5) + 3, Pitch(8))
        self.assertEqual(Pitch(5) + Pitch(3), Pitch(8))
        self.assertEqual(Pitch(5) + 7, Pitch(12))
        self.assertEqual(Pitch(5) + Pitch(7), Pitch(12))
        self.assertEqual(Pitch(5) + 18, Pitch(23))
        self.assertEqual(Pitch(5) + Pitch(18), Pitch(23))
        self.assertEqual(Pitch(5) + -9, Pitch(-4))
        self.assertEqual(Pitch(5) + Pitch(-9), Pitch(-4))

        # Subtraction
        self.assertEqual(Pitch(5) - 4, Pitch(1))
        self.assertEqual(Pitch(5) - Pitch(4), Pitch(1))
        self.assertEqual(Pitch(5) - 0, Pitch(5))
        self.assertEqual(Pitch(5) - Pitch(0), Pitch(5))
        self.assertEqual(Pitch(5) - 13, Pitch(-8))
        self.assertEqual(Pitch(5) - Pitch(13), Pitch(-8))
        self.assertEqual(Pitch(5) - -9, Pitch(14))
        self.assertEqual(Pitch(5) - Pitch(-9), Pitch(14))
        self.assertEqual(Pitch(5) - 23, Pitch(-18))

        # Multiplication
        self.assertEqual(Pitch(5) * 2, Pitch(10))
        self.assertEqual(Pitch(5) * Pitch(2), Pitch(10))
        self.assertEqual(Pitch(5) * 1, Pitch(5))
        self.assertEqual(Pitch(5) * Pitch(1), Pitch(5))
        self.assertEqual(Pitch(5) * 5, Pitch(25))
        self.assertEqual(Pitch(5) * Pitch(5), Pitch(25))
        self.assertEqual(Pitch(4) * 5, Pitch(20))
        self.assertEqual(Pitch(4) * Pitch(5), Pitch(20))
        self.assertEqual(Pitch(5) * 7, Pitch(35))
        self.assertEqual(Pitch(5) * Pitch(7), Pitch(35))
        self.assertEqual(Pitch(5) * -1, Pitch(-5))
        self.assertEqual(Pitch(5) * Pitch(-1), Pitch(-5))
        self.assertEqual(Pitch(8) * -1, Pitch(-8))
        self.assertEqual(Pitch(8) * Pitch(-1), Pitch(-8))

    def test_comparison_mod12(self):
        """
        Tests pitch comparison
        """
        self.assertTrue(Pitch(5) == Pitch(5))
        self.assertTrue(Pitch(14) == Pitch(14))
        self.assertTrue(Pitch(-5) == Pitch(-5))
        self.assertTrue(Pitch(5) <= Pitch(5))
        self.assertTrue(Pitch(5) <= Pitch(7))
        self.assertTrue(Pitch(5) < Pitch(7))
        self.assertTrue(Pitch(5) >= Pitch(5))
        self.assertTrue(Pitch(5) >= Pitch(3))
        self.assertTrue(Pitch(5) > Pitch(3))
        self.assertTrue(Pitch(5) != Pitch(4))

if __name__ == "__main__":
    unittest.main()