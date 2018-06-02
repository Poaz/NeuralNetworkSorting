import numpy as np

def counting_sort(input_arr, exp1):
    n = len(input_arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count
    for i in range(0, n):

        index = (int)(input_arr[i] // exp1)

        count[(index) % 10] += 1

    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (input_arr[i] // exp1)
        output[count[(index) % 10] - 1] = input_arr[i]
        count[(index) % 10] -= 1
        i -= 1

    #Finilalize out array.
    i = 0
    for i in range(0, len(input_arr)):
        input_arr[i] = output[i]


#Radix sort method
def radix_sort(input_arr):
    # Find the max value in the inputted array
    max1 = max(input_arr)

    # Count sort for every digit
    exp = 1
    while max1 // exp > 0:
        counting_sort(input_arr, exp)
        exp *= 10


arr = np.loadtxt("TraningDataX.txt", delimiter=",")
arr = arr.ravel()
arr = arr.astype(int)

radix_sort(arr)

for i in range(len(arr)):
    print(arr[i]),
