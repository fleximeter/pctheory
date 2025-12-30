import unittest
from pctheory import pcset
from pctheory.pcset import SetClass
from pctheory.pitch import PitchClass

class PcSetTestCase(unittest.TestCase):
    """
    Tests mod 12 pcsets.
    """
    def test_creation(self):
        """
        Tests pcset creation
        """
        sc = SetClass("[0134]")
        self.assertEqual(sc.name_prime, "[0134]")
        self.assertEqual(pcset.make_pcset12(0, 1, 3, 4), sc.pcset)

if __name__ == "__main__":
    unittest.main()