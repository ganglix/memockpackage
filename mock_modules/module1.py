import numpy as np

def repeat_array_twice(arr):
    """it returns a new array that repeats the input array twice

    Parameters
    ----------
    arr : numpy.array
        input array

    Returns
    -------
    numpy.array
        repeated array
    """    
   
    return np.array(list(arr)*2)