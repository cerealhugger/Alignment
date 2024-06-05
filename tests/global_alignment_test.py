import unittest
from global_alignment import *


class GlobalAlignmentTest(unittest.TestCase):
   def test_initialize_matrix(self):
       result = GlobalAlignment("AGCT","CGAT")
       result._init_matrix()
       expected_first_row = [' ', '-','A', 'G', 'C', 'T']
       expected_first_col = [' ', '_', 'C', 'G', 'A', 'T']

       self.assertEqual(
           [cell if isinstance(cell, str) else cell.val for cell in result.matrix[0]],
           expected_first_row)
       self.assertEqual(
           [row[0] if isinstance(row[0], str) else row[0].val for row in result.matrix],
           expected_first_col)

   def test_matrix_filling(self):
       seq1 = "AGCT"
       seq2 = "GCAT"
       alignment = GlobalAlignment(seq1, seq2)
       alignment._init_matrix()
       alignment._fill_matrix()

       # Checking a few key scores
       self.assertEqual(alignment.matrix[2][3].val, -1)  # score for aligning G with G
       self.assertEqual(alignment.matrix[3][4].val, 0)  # score for aligning C with C
       self.assertEqual(alignment.matrix[5][5].val, -1)  # score for aligning T with T
   def test_full_alignment(self):
       seq1 = "AGCT"
       seq2 = "GCAT"
       alignment = GlobalAlignment(seq1,seq2)
       alignment._init_matrix()
       alignment._fill_matrix()
       alignment._traceback()
       self.assertEqual(''.join(alignment.aligned_seq1), 'AGC-T')
       self.assertEqual(''.join(alignment.aligned_seq2), '-GCAT')

if __name__ == '__main__':
    unittest.main()
