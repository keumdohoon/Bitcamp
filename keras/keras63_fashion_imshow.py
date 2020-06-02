import numpy as np
import matplotlib.pyplot as plt

from keras.datasets import fashion_mnist


(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
plt.imshow(x_train[0])
plt.show()

print(x_train[0])
print('y_train[0] :', y_train[0])
 #y_train[0] : 9
print(x_train.shape)
 #(60000, 28, 28)
print(x_test.shape)
 #(10000, 28, 28)
print(y_train.shape)
 #(60000,)
print(y_test.shape)
 #(10000,)
