# 1. 모듈 임포트
from keras.models import Sequential, Model
from keras.layers import Dense, LSTM, Input
from keras.callbacks import EarlyStopping
from keras.utils import to_categorical

# from sklearn.preprocessing import OneHotEncoder
import numpy as np

# 1-1. 객체 생성
es = EarlyStopping(monitor = 'loss', mode = 'min', patience = 10)
# enc = OneHotEncoder()


# 2. 데이터
x = np.array(range(1, 11))
y = np.array([1, 1, 2, 3, 4, 5,  2, 3, 4, 5])#.reshape(-1, 1)

# enc.fit(y)
# y = enc.transform(y).toarray()
y = to_categorical(y)
y = y[:, 1:]
print(x)
print(x.shape)
print(y)
print(y.shape)


# 3. 모델 구성
input1 = Input(shape = (1, ))
dense1 = Dense(100, activation = 'relu')(input1)
dense2 = Dense(200, activation = 'relu')(dense1)
dense3 = Dense(50, activation = 'relu')(dense2)
dense4 = Dense(40, activation = 'relu')(dense3)

output1 = Dense(10)(dense4)
output2 = Dense(5, activation = 'softmax')(output1)

model = Model(inputs = input1, outputs = output2)

model.summary()


# 4. 컴파일 및 훈련
model.compile(loss = 'categorical_crossentropy',
              optimizer = 'adam', metrics = ['accuracy'])
model.fit(x, y, epochs = 100, batch_size = 1)


# 5. 평가 및 예측
loss, acc = model.evaluate(x, y, batch_size = 1)
print("loss : ", loss)
print("acc : ", acc)

x_pred = np.array([1, 2, 3])
y_pred = model.predict(x_pred)
# y_pred = np.argmax(y_pred, axis = 1).reshape(-1, )
# y_pred = enc.transform(y_pred)
y_pred = to_categorical(y_pred)
print("y_pred : \n", y_pred)