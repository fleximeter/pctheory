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
    
    def test_mx(self):
        """
        Tests twelve tone matrix creation
        """
        # Matrix from https://musictheory.pugetsound.edu/mt21c/section-195.html
        # (Note: a few corrections had to be made because of mistakes in that matrix.)
        row = pcseg.make12("[01675243A9B8]")
        self.assertTrue(pcseg.is_row(row))
        self.assertTrue(RowTestCase.assert_row(row))
        mx = [
            pcseg.make12("[01675243A9B8]"),
            pcseg.make12("[B056413298A7]"),
            pcseg.make12("[6701B8A94352]"),
            pcseg.make12("[56B0A7983241]"),
            pcseg.make12("[781209BA5463]"),
            pcseg.make12("[AB4530218796]"),
            pcseg.make12("[89231A0B6574]"),
            pcseg.make12("[9A342B107685]"),
            pcseg.make12("[238974650B1A]"),
            pcseg.make12("[349A8576102B]"),
            pcseg.make12("[12786354BA09]"),
            pcseg.make12("[45AB96872130]"),
        ]
        ttmx = pcseg.TwelveToneMatrix(row)
        for i in range(len(mx)):
            self.assertEqual(ttmx._mx[i], mx[i])
        self.assertEqual(ttmx.labels_top, ["T0I", "T1I", "T6I", "T7I", "T5I", "T2I", "T4I", "T3I", "T10I", "T9I", "T11I", "T8I"])
        self.assertEqual(ttmx.labels_bottom, ["T0RI", "T1RI", "T6RI", "T7RI", "T5RI", "T2RI", "T4RI", "T3RI", "T10RI", "T9RI", "T11RI", "T8RI"])
        self.assertEqual(ttmx.labels_left, ["T0", "T11", "T6", "T5", "T7", "T10", "T8", "T9", "T2", "T3", "T1", "T4"])
        self.assertEqual(ttmx.labels_right, ["T0R", "T11R", "T6R", "T5R", "T7R", "T10R", "T8R", "T9R", "T2R", "T3R", "T1R", "T4R"])
    
        # Test retrieval
        self.assertEqual(ttmx.get_column(2), pcseg.make12("[650B1423897A]"))
        self.assertEqual(ttmx.get_row(2), pcseg.make12("[6701B8A94352]"))

class InvarianceMatrixTestCase(unittest.TestCase):
    """
    Tests invariance matrices
    """
    def test_imx(self):
        """
        Simple I invariance matrix tests
        """
        # This example is from https://ecmc.rochester.edu/rdm/pdflib/IV.12tt.pdf
        p = pcseg.make12("[038749BA2561]")
        q = pcseg.make12("[8730B495261A]")
        imx = pcseg.InvarianceMatrix(q, p, 'I')
        mx = [
            pcseg.make12("[8730B495261A]"),
            pcseg.make12("[BA6327085941]"),
            pcseg.make12("[43B87051A296]"),
            pcseg.make12("[32A76B409185]"),
            pcseg.make12("[0B7438196A52]"),
            pcseg.make12("[54098162B3A7]"),
            pcseg.make12("[762BA3841509]"),
            pcseg.make12("[651A927304B8]"),
            pcseg.make12("[A95216B74830]"),
            pcseg.make12("[1085492A7B63]"),
            pcseg.make12("[21965A3B8074]"),
            pcseg.make12("[984105A6372B]"),
        ]
        for i in range(len(mx)):
            self.assertEqual(imx._mx[i], mx[i])
    
    def test_tmx(self):
        """
        Simple T invariance matrix tests
        """
        # This example is from https://ecmc.rochester.edu/rdm/pdflib/IV.12tt.pdf
        p = pcseg.make12("[038749BA2561]")
        q = pcseg.make12("[8730B495261A]")
        tmx = pcseg.InvarianceMatrix(p, p, 'T')
        #print(tmx)
        mx = [
            pcseg.make12("[038749BA2561]"),
            pcseg.make12("[90541687B23A]"),
            pcseg.make12("[470B813269A5]"),
            pcseg.make12("[581092437AB6]"),
            pcseg.make12("[8B430576A129]"),
            pcseg.make12("[36BA70215894]"),
            pcseg.make12("[14985A0B3672]"),
            pcseg.make12("[25A96B104783]"),
            pcseg.make12("[A1652798034B]"),
            pcseg.make12("[7A32B4659018]"),
            pcseg.make12("[6921A3548B07]"),
            pcseg.make12("[B27638A91450]"),
        ]
        for i in range(len(mx)):
            self.assertEqual(tmx._mx[i], mx[i])

if __name__ == "__main__":
    unittest.main()