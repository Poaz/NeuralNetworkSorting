from keras.optimizers import SGD, Adam
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.utils import to_categorical
from sklearn.metrics import confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import itertools
import keras.backend as k
import time




from keras.models import load_model
model = load_model('model.h5')
arr = np.loadtxt("TraningDataX.txt", delimiter=",")
start_time = time.time()
model.predict(arr)
print("--- %s seconds ---" % (time.time() - start_time))