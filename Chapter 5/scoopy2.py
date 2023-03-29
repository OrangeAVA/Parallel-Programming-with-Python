from scoop import futures
import math
import numpy as np

def func(value):
    result = math.sqrt(value)
    print("The value %s and the elaboration is %s" %(value, result))
    return result

if __name__ == "__main__":
    data = np.array([10,3,6,1,4,8,25,9])
    results = list(futures.map(func, data))
    for result in results:
      print("This is the result: %s" %result)

