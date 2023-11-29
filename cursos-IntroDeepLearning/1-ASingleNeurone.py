import pandas as pd

red_wine = pd.read_csv('../dl-course-data/red-wine.csv')
red_wine.head()

rows, columns = red_wine.shape
print(f'The dataframe has {rows} rows and {columns} columns.')
#red_wine.shape (1, 12)# (rows, columns)
# YOUR CODE HERE
input_shape = [11]

print(input_shape)

################################################3
#2) Define a linear model

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Dense(units=1, input_shape=input_shape)
])

################################################3
#3) Look at the weights

w, b = model.weights
model.get_weights()

################################################
#4) Optional plot the output of an untrained linear model

import tensorflow as tf
import matplotlib.pyplot as plt

model = keras.Sequential([
    layers.Dense(1, input_shape=[1]),
])

x = tf.linspace(-1.0, 1.0, 100)
y = model.predict(x)

plt.figure(dpi=100)
plt.plot(x, y, 'k')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.xlabel("Input: x")
plt.ylabel("Target y")
w, b = model.weights # you could also use model.get_weights() here
plt.title("Weight: {:0.2f}\nBias: {:0.2f}".format(w[0][0], b[0]))
plt.show()
