import sys
import unittest

sys.path.insert(0,'/home/deepcompute/my_work/ci_and_cd/programs/')

from sorting import Sorting
class TestingSort(unittest.TestCase):

        def setUp(self):
            self.test_Sorting = Sorting()

        def test_sort_dict_values(self):
            self.assertEqual([1, 2, 4],self.test_Sorting.sort_dict_values({"a" : 4, "b" : 2, "c" : 1}))
if __name__ == '__main__':
    unittest.main()

