import numpy as np
import time

arr = np.loadtxt("TraningDataX.txt", delimiter=",")
#arr = arr.ravel()
arr = arr.astype(int)
start_time = time.time()

heap = np.sort(arr, kind='mergesort')

print("--- %s seconds ---" % (time.time() - start_time))