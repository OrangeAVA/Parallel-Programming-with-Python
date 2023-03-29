import time
import math
import numpy as np
from multiprocessing.pool import Pool

def func(value):
    result = math.sqrt(value)
    print("The value %s and the elaboration is %s" %(value, result) )
    time.sleep(value)
    return result

if __name__ == '__main__':
    with Pool() as pool:
        data = np.array([10,3,6,1,4,5,2,9,7,3,4,6])
        results = pool.map(func, data, chunksize=4)
        print("The main process is going on...")
        for result in results:
            print("This is the result: %s" %result)
    print("END Program")  

