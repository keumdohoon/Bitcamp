#cnn모델
# 'sparse_categorical_crossentropy'
#d위에 sparse를 사용하게 되면 원핫 인코딩 과정을 위에서 해주지 않아도 잘 돌아간다 어떻게 보면 원핫 인코딩의 일종인것으로 보인다 .
from keras.datasets import cifar100
from keras.utils import np_utils
from keras.models import Sequential, Model
from keras.layers import Dense, LSTM, Conv2D, Input
from keras.layers import Flatten, MaxPooling2D, Dropout
import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping, ModelCheckpoint,  TensorBoard
from keras.datasets import cifar10

from keras.optimizers import Adam
import matplotlib.pyplot as plt
 #그래프를 그려주는 것을  plt라고 하겠다


(x_train, y_train), (x_test, y_test) = cifar10.load_data()

print(x_train[0])
print('y_train[0] :', y_train[0]) #y_train[0] : [19]

print(x_train.shape)  #(50000, 32, 32, 3)
print(x_train.shape)  #(50000, 32, 32, 3)
print(y_train.shape)  #(50000, 1)
print(y_test.shape)   #(10000, 1)

plt.imshow(x_train[0])
plt.show()


# 데이터 전처리#one hot encoding
# y_train = np_utils.to_categorical(y_train)
# y_test = np_utils.to_categorical(y_test)
print(y_train.shape)  #(50000, 100)
print(y_test.shape)   #(10000, 100) 




x_train = x_train.reshape(50000, 32, 32, 3).astype('float32')/ 255.0
x_test = x_test.reshape(10000, 32, 32, 3).astype('float32')/ 255.0


#2. 모델
model = Sequential()
model.add(Conv2D(32, kernel_size=3, padding='same', activation='relu', input_shape = (32, 32, 3)))
model.add(Conv2D(32, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='same'))

model.add(Conv2D(64, kernel_size=3, padding='same', activation='relu'))
model.add(Conv2D(64, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='same'))


model.add(Conv2D(128, kernel_size=3, padding='same', activation='relu'))
model.add(Conv2D(128, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='same'))


model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.summary()

#3. 훈련
model.compile(optimizer=Adam(1e-4), loss='sparse_categorical_crossentropy', metrics=['acc'])
                                        #sparse categorical 은 원핫인코ㅇ딩을 대신해주는 것이다. 


hist = model.fit(x_train, y_train, 
                epochs = 45, validation_split= 0.3,
                 batch_size=32, verbose = 1) 

loss = model.evaluate(x_test, y_test, batch_size = 32)

#그리기
import matplotlib.pyplot as plt


#hist는 핏에서 나온 결과치
his.dict = hist.history

#4, 예측
loss_acc = model.evaluate(x_test, y_test)

loss = hist.history['loss']
val_loss = hist.history['val_loss']
acc = hist.history['acc']
val_acc= hist.history['val_acc']
print("loss : {loss}", loss)
print("acc : {acc}", acc)
print("val_acc: ", val_acc)
print("loss_acc: ", loss_acc)


plt.subplot(2,1,1)
plt.plot(hist.history['loss'], marker ='.', c='red', label ='loss')
plt.plot(hist.history['val_loss'], marker='.', c='blue', label= 'val_loss')

plt.grid()
plt.title('loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(loc='upper right')


plt.subplot(2,1,2)
plt.plot(hist.history['acc'], marker ='.', c='red', label ='acc')
plt.plot(hist.history['val_acc'], marker='.', c='blue', label= 'val_acc')
plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
plt.grid()
plt.title('acc')
plt.ylabel('acc')
plt.xlabel('epoch')
plt.legend(['acc', 'val_acc'])
plt.show()
'''
tb_hist = TensorBoard(log_dir='graph', histogram_freq=0, write_graph=True, write_images=True)

#3. 훈련
model.compile(loss = 'categorical_crossentropy', optimizer = "rmsprop", metrics = ['acc'])
early_stopping = EarlyStopping(monitor='loss', patience=30, mode='auto' )

hist = model.fit(x_train, y_train, epochs = 45, validation_split= 0.2, batch_size=42, callbacks=[early_stopping])
'''





plt.figure(figsize=(9,5))




#loss_acc:  [2.7696992603302, 0.3425999879837036]
#과적합 처리방식 3가지
#1. dropout
#2. 훈련데이터를 늘린다
#3. 피쳐를 늘린다.
# 4. 레귤러라리제이션 