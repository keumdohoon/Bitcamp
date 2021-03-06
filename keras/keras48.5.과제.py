import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
##############################과제로 결과값이 1아니면 0으로 나오게 해라##############################
#2진분류  binary classification
#적용해야할 것 2가지, 2진분류를 사용하면 activation을 시그모이드라는 함수를 써야한다. 
#loss를 쓸땐 무조건 mse를 썻지만 2진 분류를 할때는 
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 1. 데이터
x = np.array(range(1, 11))
y = np.array([1,0,1,0,1,0,1,0,1,0])


print("x", x)  #x [1 2 3 4 5 6 7 8 9 10]
print('y', y)  #y [1 0 1 0 1 0 1 0 1 0]

print("x.shape", x.shape) #x.shape (9, )
print("y.shape", y.shape) #y.shape(10,)
x = x.reshape(10,1)
y = y.reshape(10,1)

print("x", x)  
print('y', y)  

#2. 모델링
#model.add(Dense(60, input_dim=60, activation='relu'))
#	model.add(Dense(1, activation='sigmoid'))
model = Sequential()
model.add(Dense(10, input_dim= 1, activation='sigmoid'))
model.add(Dense(10))   
model.add(Dense(20))   
model.add(Dense(40))   
model.add(Dense(110))   
model.add(Dense(100)) 
model.add(Dense(800))   
model.add(Dense(60)) 
model.add(Dense(200))   
model.add(Dense(10)) 
model.add(Dense(1,  activation='sigmoid'))
#마지막에 나오는 활성화 값이 시그모이드를 붙이면 0아니면 1이 나오게 된다. 마지막레이어의 값 곱하기 시그모이드. 
model.summary()


# 3. 컴파일, 훈련

# EarlyStopping
from keras.callbacks import EarlyStopping
es = EarlyStopping(monitor = 'loss', patience=100, mode = 'auto')

#model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#	return model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics = ['accuracy'] )
model.fit(x, y, epochs=1220, batch_size=32, verbose=2)
#0이냐 1이냐 딱딱 떨어지는 숫자를 찾는 것이기에 우리는 여기서 mse가 아닌 딱딱 떨어지는 숫자를 나타내주는  acc를 사용하게 된다. 
#binary_crossentropy 2진분류에서 binarycrossentropy딱 하나밖에 없다. 이걸 외울것. 
#1, 아웃풋에 시그모이드 추가, 2,model.compile에 loss를 binary crossentropy로 바꾸어주고 , metrics를 accuracy로 바꾸어주게된다. 
# tmp = []
# a = np.round(pred[0][0])
# b = np.round(pred[1][0])
# c = np.round(pred[2][0])
# print(a)
# print(b)
# print(c)
# tmp.append([a, b, c])
# print(tmp)
# 4. 평가, 예측
loss, acc = model.evaluate(x, y, batch_size=32)
print(' loss : ', loss)
print('mse:', acc)
#예측
x_pred = np.array([1,2,3])
y_pred = model.predict(x_pred)
print('y_pred :', y_pred)
# sigmoid 함수를 안거친것으로 보여지게 된다. 
y1_pred = np.round(y_pred)     
#sigmoid를 써줘서 모든 값이 0과 1사이인 값으로 나오게 되는데 np.where을 사용해주면, 0.5를 기준으로 더 크거나 같은 값은 1 그리고 이 조건에 충족하지 못하는 값은 0이 된다. 
print('y_pred :', y1_pred)

