from insertion_sort import insertion_sort
from merge_sort import merge_sort
from merge_sort import merge
import unittest

class SortingTestCase(unittest.TestCase):
	
	def test_insertion_sort(self):

		input = [2, 4, 1, 5, 3]
		output = [1, 2, 3, 4, 5]
		insertion_sort(input)
		self.assertListEqual(input, output)

	def test_merge(self):
		
		input = [11, 22, 33, 2 ,3 ,4]
		p = 2
		q = 2
		r = 5
		output = [11, 22, 2, 3, 4, 33]
		merge(input, p, q, r)
		self.assertListEqual(input, output)

	def test_merge_sort(self):

		input = [5, 4, 3, 2, 1]
		p = 0
		r = 4
		output = [1, 2, 3, 4, 5]
		merge_sort(input, p, r)
		self.assertListEqual(input, output)
	

if __name__ == "__main__":
	unittest.main()
