import time
import math
import numpy as np
from concurrent.futures import ProcessPoolExecutor

def func(value):
    result = math.sqrt(value)
    print("The value %s and the elaboration is %s" %(value, result) )
    time.sleep(value)
    return result

if __name__ == '__main__':
    with ProcessPoolExecutor(10) as executor:
        data = np.array([10,3,6,1])
        for result in executor.map(func, data):
           print("This is the result: %s" %result)        
    print("END Program")  

