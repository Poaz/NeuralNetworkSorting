import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
from numpy import genfromtxt


X = np.loadtxt("TraningDataX.txt", delimiter=",")
Y = np.loadtxt("TraningDataY.txt", delimiter=",")
print("Loaded data")
trainingSamplesX = X[:(int)(len(X)*0.75)]
trainingSamplesY = Y[:(int)(len(Y)*0.75)]

testSamplesX = X[(int)(len(X)*0.75):]
testSamplesY = Y[(int)(len(Y)*0.75):]
print("split data")
model = Sequential()
model.add(Dense(256,input_dim=100,activation='relu')) #,activation='relu'
model.add(Dropout(0.1))
model.add(Dense(200,activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(100,activation='relu'))

optimizer = Adam(lr=0.002, decay=0.00002)
model.compile(loss='mean_squared_error', optimizer=optimizer, metrics=['accuracy'])

model.fit(trainingSamplesX,trainingSamplesY, batch_size=128, epochs=25,verbose=1)
acc = model.evaluate(testSamplesX,testSamplesY,batch_size=32,verbose=1)
print(acc)
model.save("model.h5")


predTrain = model.predict(trainingSamplesX[0:10])
for i in range(0,len(predTrain)):
    print("Prediction :", predTrain[i][0:10])
    print("Correct    :",trainingSamplesY[i][0:10])
    print()


print()
print()
print()
print()
print()
print("Test predictions")
predTest = model.predict(testSamplesX[0:10])
for i in range(0,len(predTest)):
    print("Prediction :", predTest[i][0:10])
    print("Correct    :",testSamplesY[i][0:10])
    print()