
import sys
import os
parent_dir = os.path.abspath(os.getcwd())
sys.path.append(parent_dir)

import numpy as np
import unittest
from mock_modules.module1 import repeat_array_twice

class Module1TestCase(unittest.TestCase):
    def test_repeat_array(self):
        # Test case 1: Testing with a simple input array
        input_array = np.array([1, 2, 3])
        expected_output = np.array([1, 2, 3, 1, 2, 3])  # Expected output is the input array repeated twice
        self.assertTrue(np.array_equal(repeat_array_twice(input_array), expected_output))

        # Test case 2: Testing with an empty input array
        input_array = np.array([])
        expected_output = np.array([])  # Expected output is an empty array
        self.assertTrue(np.array_equal(repeat_array_twice(input_array), expected_output))

        # Test case 3: Testing with a larger input array
        input_array = np.array([5, 10, 15, 20])
        expected_output = np.array([5, 10, 15, 20, 5, 10, 15, 20])  # Expected output is the input array repeated twice
        self.assertTrue(np.array_equal(repeat_array_twice(input_array), expected_output))

if __name__ == '__main__':
    unittest.main()
