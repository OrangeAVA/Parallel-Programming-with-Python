from scoop import futures
import math
import numpy as np
import random

def func(value):
    result = math.sqrt(value)
    print("The value %s and the elaboration is %s" %(value, result))
    return result

if __name__ == "__main__":
    data = np.array([10,3,6,1,4,8,25,9])
    result = sum(futures.map(func, data))
    print("This is the reduction result: %s" %result)
