import unittest
from bubble_sort import bubble_sort, bubble_sort2

class TestBubbleSort(unittest.TestCase):
    def test_method(self):
        self.assertEqual('rome'.upper(), 'ROME')
    
    def test_sort(self):
        self.assertEqual(bubble_sort([9,8,7,6,5,4,3,2,1]), [1,2,3,4,5,6,7,8,9])

    def test_sort_2(self):
        self.assertEqual(bubble_sort2([9,8,7,6,5,4,3,2,1]), [1,2,3,4,5,6,7,8,9])


if __name__ == '__main__':
    unittest.main()