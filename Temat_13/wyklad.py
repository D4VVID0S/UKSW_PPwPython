''' keras CNN example '''
import numpy as np
np.random.seed(123) # dla reprodukcji
from keras.models import Sequential # sekwencyjne sieci neuronowe
from keras.layers import Dense, Dropout, Activation, Flatten # usual layers
from keras.layers import Convolution2D, MaxPooling2D # To train on image data
from keras.utils import np_utils # some utilities

''' Ladowanie bazy danych do uczenia sieci '''
from keras.datasets import mnist
# Load pre-shuffled MNIST data into train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(X_train.shape) # 60k samples, each is a 28x28 black-and-white image
# (60000, 28, 28)

# X_train to dane do treningu, y_train to poprawne wyniki dla tych danych
# X_test to dane testujace siec, y_test to pozadany wynik

import matplotlib.pyplot as plt
plt.imshow(X_train[0])

''' Preprocessing inputu '''
# tensorflow must know how many channes there are, so the last dimension
# should be the number of channels (int this case, one)
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
print(X_train.shape)
# (60000, 28, 28, 1)
X_train = X_train.astype('float32') # input data must be float32
X_test = X_test.astype('float32')
X_train = X_train/255 # input data must be in range from 0 to 1
X_test = X_test/255

print(y_train[:10])
# [5 0 4 1 9 2 1 3 1 4] # y_train tells which digit is showed in every picture
# Convert 1-dimensional class arrays to 10-dimensional class matrices
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)
print(y_train.shape) # (60000, 10)

''' Architektura sieci '''
model = Sequential()
# defining input layer. input_shape should be the shape of 1 sample.
# here it’s (28, 28, 1) = (width, height, channels) of each digit image. model.add(Convolution2D(32, (3,3), activation='relu', input_shape=(28,28,1))) # 32 convolution filters, each of them is a 3x3 matrix
print( model.output_shape )
# (None, 26, 26, 32) corresponds to (samples, new_rows, new_cols, filters)
# model will output all samples, convoluted into 26x26 array using 32 filters
# adding more layers
model.add(Convolution2D(32,(3,3),activation='relu')) # regularization max(x,0)
model.add(MaxPooling2D(pool_size=(2,2))) # way to reduce number of parameters in our model by sliding a 2×2 pooling filter across the previous layer and taking the max of the 4 values in the 2×2 filter
model.add(Dropout(0.25)) # killing some neurons

model.add(Flatten()) # flattens the input (1 channel)
model.add(Dense(128, activation='relu')) # 128 is the output size
# keras automatically matches layer input/output sizes
model.add(Dropout(0.5)) # killing excessive neurons again
model.add(Dense(10, activation='softmax')) # normalize the output
# to a probability distribution over predicted output classes