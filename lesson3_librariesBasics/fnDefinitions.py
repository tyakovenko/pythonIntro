import numpy as np

def findUnique (x):
    '''
    find a list of unique items in another list
    :param x: array; dtype = np.array()
    :return: unique array, statement; dtype = np.array(), str
    '''
    words = "the arrays are the same!"
    if not np.array_equal(np.unique(x), x):
        words = "they are not the same"
    return np.unique(x), words

x = np.array([1,2])
xSame = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
xDif = np.array([1, 1, 1, 3, 4, 5, 1, 1, 1, 1])
arr, words = findUnique(xDif)
print(findUnique(xDif))
print(type(arr))