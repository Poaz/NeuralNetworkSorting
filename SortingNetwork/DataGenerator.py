import numpy as np;
import random

numberListLength = 100
listLength = 100000

randomNumbers = np.array([[(int)(random.randrange(0,100))/100 for j in range(numberListLength)] for i in range(listLength)])
print("Done with number generation")
sortedNumbers = np.array([sorted(randomNumbers[i]) for i in range(len(randomNumbers))])
print("Done with sorting")

np.savetxt("TraningDataX.txt",randomNumbers,delimiter=",",newline="\n")
np.savetxt("TraningDataY.txt",sortedNumbers,delimiter=",",newline="\n")