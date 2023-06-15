# import sys
# sys.path.insert(0, './')
# from mock_modules import module1 as m1

import module1 as m1
def repeat_array_four_times(arr):
    """repeat_array_four_times return an array that repeats the input arr for four times

    Parameters
    ----------
    arr : numpy.array
        input array

    Returns
    -------
    numpy.array
        out put array
    """    
    arr_twice = m1.repeat_array_twice(arr)
    arr_four_times = m1.repeat_array_twice(arr_twice)
    return arr_four_times
