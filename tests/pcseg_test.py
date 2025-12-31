import unittest
from pctheory import pcseg
from pctheory.pcset import SetClass
from pctheory.pitch import PitchClass

class PcSegTestCase(unittest.TestCase):
    """
    Tests mod 12 pitch class segments
    """
    def test_make_seg(self):
        """
        Tests segment creation
        """
        self.assertEqual(pcseg.make_pcseg12(1, 0, 11, 9, 11), [PitchClass(1), PitchClass(0), PitchClass(11), PitchClass(9), PitchClass(11)])
        self.assertEqual(pcseg.make_pcseg12(3, 2, 4, 9, 11), [PitchClass(3), PitchClass(2), PitchClass(4), PitchClass(9), PitchClass(11)])
    
    def test_operations(self):
        """
        Tests operations on pcsegs
        """
        self.assertEqual(pcseg.transpose(pcseg.make_pcseg12(4, 2, 1, 3, 9, 8), 3), pcseg.make_pcseg12(7, 5, 4, 6, 0, 11))
        self.assertEqual(pcseg.transpose(pcseg.make_pcseg12(4, 2, 1, 3, 9, 8), 13), pcseg.make_pcseg12(5, 3, 2, 4, 10, 9))
        self.assertEqual(pcseg.transpose(pcseg.make_pcseg12(4, 2, 1, 3, 9, 8), -13), pcseg.make_pcseg12(3, 1, 0, 2, 8, 7))
        self.assertEqual(pcseg.invert(pcseg.make_pcseg12(4, 2, 1, 3, 9, 8)), pcseg.make_pcseg12(8, 10, 11, 9, 3, 4))
        self.assertEqual(pcseg.multiply(pcseg.make_pcseg12(4, 2, 1, 3, 9, 8), 1), pcseg.make_pcseg12(4, 2, 1, 3, 9, 8))
        self.assertEqual(pcseg.multiply(pcseg.make_pcseg12(4, 2, 1, 3, 9, 8), 11), pcseg.make_pcseg12(8, 10, 11, 9, 3, 4))
        self.assertEqual(pcseg.multiply(pcseg.make_pcseg12(4, 2, 1, 3, 9, 8), 5), pcseg.make_pcseg12(8, 10, 5, 3, 9, 4))
        self.assertEqual(pcseg.retrograde(pcseg.make_pcseg12(4, 2, 1, 3, 9, 8)), pcseg.make_pcseg12(8, 9, 3, 1, 2, 4))
        self.assertEqual(pcseg.rotate(pcseg.make_pcseg12(4, 2, 1, 3, 9, 8), 2), pcseg.make_pcseg12(9, 8, 4, 2, 1, 3))
        self.assertEqual(pcseg.rotate(pcseg.make_pcseg12(4, 2, 1, 3, 9, 8), 6), pcseg.make_pcseg12(4, 2, 1, 3, 9, 8))
        self.assertEqual(pcseg.rotate(pcseg.make_pcseg12(4, 2, 1, 3, 9, 8), 7), pcseg.make_pcseg12(8, 4, 2, 1, 3, 9))
        self.assertEqual(pcseg.rotate(pcseg.make_pcseg12(4, 2, 1, 3, 9, 8), -2), pcseg.make_pcseg12(1, 3, 9, 8, 4, 2))
        self.assertEqual(pcseg.rotate(pcseg.make_pcseg12(4, 2, 1, 3, 9, 8), -7), pcseg.make_pcseg12(2, 1, 3, 9, 8, 4))

class RowTestCase(unittest.TestCase):
    """
    Tests row functionality
    """
    def assert_row(row):
        """
        Checks if something is a row
        """
        if len(row) == 12:
            uniset = {PitchClass(i) for i in range(12)}
            if set(row) == uniset:
                return True
            else:
                return False
        else:
            return False

    def test_row_creation(self):
        """
        Tests row creation
        """
        for _ in range(20):
            row = pcseg.generate_random_pcseg12(12, True)
            self.assertTrue(RowTestCase.assert_row(row))
        for _ in range(20):
            row = pcseg.generate_random_all_interval_row()
            self.assertTrue(RowTestCase.assert_row(row))
            diffs = [(row[i].pc - row[i-1].pc) % 12 for i in range(1, 12)]
            self.assertEqual(set(diffs), {i for i in range(1, 12)})
        for _ in range(20):
            row = pcseg.generate_random_ten_trichord_row()
            self.assertTrue(RowTestCase.assert_row(row))
            scs = [SetClass(set(row[i:i+3])).name_prime for i in range(10)]
            self.assertEqual(len(set(scs)), 10)
        for _ in range(20):
            row = pcseg.generate_random_all_trichord_row()
            self.assertTrue(RowTestCase.assert_row(row))
            row = row + row[:2]
            scs = [SetClass(set(row[i:i+3])).name_prime for i in range(12)]
            self.assertEqual(len(set(scs)), 12)
        for _ in range(20):
            row = pcseg.generate_random_all_trichord_babbitt_row()
            self.assertTrue(RowTestCase.assert_row(row))
            scs = set([SetClass(set(row[i:i+3])).name_prime for i in range(10)])
            self.assertEqual(len(scs), 10)
            self.assertTrue("[036]" not in scs)
            self.assertTrue("[048]" not in scs)

if __name__ == "__main__":
    unittest.main()