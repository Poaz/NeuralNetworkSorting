from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Embedding
from keras.layers import LSTM
import numpy as np


max_features = 100

class MainGenerator(object):

    def __init__(self, features, labels, batch_size):
        self.features = features
        self.labels = labels
        self.batch_size = batch_size
        self.currentStep = 0

    def generator(self):

        features = self.features
        labels = self.labels
        # Create empty arrays to contain batch of features and labels#
        batch_features = np.zeros((self.batch_size, 200, 100))
        batch_labels = np.zeros((200, 100))
        #features = features.values
        #labels = labels.values
        while True:
            for i in range(0, self.batch_size):
                batch_features[i] = features[i+self.currentStep]
                batch_labels[i] = labels[i+self.currentStep]
                self.currentStep += 1
                if((features.shape[0]-250) == self.currentStep):
                    self.currentStep = 0
            yield batch_features, batch_labels


model = Sequential()
model.add(LSTM(256, input_shape=(200, 100), return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(128))
model.add(Dropout(0.2))
model.add(Dense(100, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

X = np.loadtxt("TraningDataX.txt", delimiter=",")
Y = np.loadtxt("TraningDataY.txt", delimiter=",")

print("Loaded data")
trainingSamplesX = X[:(int)(len(X)*0.75)]
trainingSamplesY = Y[:(int)(len(Y)*0.75)]

testSamplesX = X[(int)(len(X)*0.75):]
testSamplesY = Y[(int)(len(Y)*0.75):]
print("split data")

model.fit_generator(MainGenerator(trainingSamplesX, trainingSamplesY, 200).generator(), steps_per_epoch= 200, epochs=2)
score = model.evaluate_generator(MainGenerator(testSamplesX, testSamplesY, 200).generator(), steps=200)

model.save('LSTM_Sort.HDF5')
