import time
import math
import os
import numpy as np
from concurrent.futures import ProcessPoolExecutor

def func(value):
    result = math.sqrt(value)
    pid = os.getpid()
    print("[Pid:%s] The value %s and the elaboration is %s" %(pid, value, result) )
    time.sleep(value)
    return result

if __name__ == '__main__':
    with ProcessPoolExecutor(10) as executor:
        data = np.array([10,3,6,1,4,5,2,9,7,3,4,6])
        for result in executor.map(func, data, chunksize=4):
           print("This is the result: %s" %result)        
    print("END Program")  

