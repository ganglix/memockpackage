# dev add path
# import sys
# import os
# parent_dir = os.path.abspath(os.getcwd())
# sys.path.append(parent_dir)

# import mock_modules as mm
# mm.module1
# AttributeError: module 'mock_modules' has no attribute 'module1'


# from mock_modules import module1 as m1
# res = m1.repeat_array_twice([1])
# print(res) # [1 1]


# import mock_modules.module1 as m1
# res = m1.repeat_array_twice([1])
# print(res) # [1 1]

import mock_modules.module2 as m2
res = m2.repeat_array_four_times([1])
print(res) # [1 1]


