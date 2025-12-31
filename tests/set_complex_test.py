import unittest
from pctheory import pcseg
from pctheory.pcset import SetClass
from pctheory.pitch import PitchClass
from pctheory import set_complex

class SetComplexTestCase(unittest.TestCase):
    """
    Tests set complexes
    """
    def test_sc_placeholder(self):
        """
        PLACEHOLDER test for set complexes
        This placeholder test exists to make sure the set complex functionality executes without breaking.
        Need to add actual tests later.
        """
        sc = SetClass("5-4")
        skcomplex = set_complex.get_k12(sc)
        skhcomplex = set_complex.get_kh12(sc)

if __name__ == "__main__":
    unittest.main()