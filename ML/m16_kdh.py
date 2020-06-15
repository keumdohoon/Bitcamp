import pandas as pd
import numpy as np

from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential, Model
import numpy as np
import pandas as pd
from keras.layers import Dense, Conv2D, Dropout, Flatten,Input
from keras.layers import MaxPooling2D
from keras.wrappers.scikit_learn import KerasClassifier, KerasRegressor # 항상 분류와 회기가 존재한다 ㅎ
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import MinMaxScaler,StandardScaler

# 1. 데이터
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape)
print(x_test.shape)

# x_train = x_train.reshape(x_train.shape[0],28, 28, 1)/255
# x_test = x_test.reshape(x_test.shape[0],28, 28, 1)/255

x_train = x_train.reshape(x_train.shape[0],28*28)/255
x_test = x_test.reshape(x_test.shape[0],28*28)/255

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

print(y_train.shape)

# 2. model 모델 자체를 진짜 함수로 만든다?

def build_model(drop=0.1, optimizer='adam'):
    input1 = Input(shape=(28*28,),name='input1')
    x = Dense(512, activation='relu', name='hidden1')(input1)
    x = Dropout(drop)(x)
    x = Dense(256, activation='relu', name='hidden2')(x)
    x = Dropout(drop)(x)
    x = Dense(128, activation='relu', name='hidden3')(x)
    output = Dense(10,activation='softmax',name='output')(x)
    model = Model(inputs=input1,outputs=output)
    model.compile(optimizer=optimizer,metrics=['acc'],loss='categorical_crossentropy')

    return model

def create_hyperparameters():
    batchs = [256]
    optimizer = ['rmsprop','adam', 'adadelta']
    dropout = [0.5,0.4,0.5]
    
    return {'model__batch_size' : batchs,'model__optimizer' : optimizer, 'model__drop': dropout}

# 케라스를 그냥 쓰면 안된다? sklearn형식으로 wrap한다 gridsearch, randomsearch를 사용하기 위해서 

model = KerasClassifier(build_fn=build_model) # 사이킷런에서 쓸수 있도록 wrapping했다 

hyperparameters = create_hyperparameters()

pipe = Pipeline([('scaler', MinMaxScaler()),('model',model)])
# pipe = make_pipeline(MinMaxScaler(),model)

# print(f"pipe.get_params():{pipe.get_params()}")

model = RandomizedSearchCV(pipe, hyperparameters, cv=5)  # -> 첫번째 인자에 모델이 들어가고 파라미터, kfold

try :
    model.fit(x_train,y_train)
except:
    print("Error")

# print(model.best_estimator_)
print(model.best_params_)
# print(model.score(x_test,y_test))