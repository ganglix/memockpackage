
import sys
import os
parent_dir = os.path.abspath(os.getcwd())
sys.path.append(parent_dir)

import numpy as np
import unittest
from mock_modules.module2 import repeat_array_four_times

class Module2TestCase(unittest.TestCase):
    def test_repeat_array_four_times(self):
        # Test case 1: Testing with a simple input array
        input_array = np.array([1, 2, 3])
        expected_output = np.array([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])  # Expected output is the input array repeated four times

        actual_output = repeat_array_four_times(input_array)

        # Asserting that the actual output matches the expected output
        self.assertTrue(np.array_equal(actual_output, expected_output))

if __name__ == '__main__':
    unittest.main()
