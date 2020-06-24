#아이리스 모델


import numpy as np
from sklearn.datasets import load_boston, load_breast_cancer, load_iris
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier, XGBRegressor
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score, r2_score
from lightgbm import LGBMClassifier

### 데이터 ###
x, y = load_iris(return_X_y=True)
print(x.shape)      # (150, 4)
print(y.shape)      # (150,)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8,
                 shuffle = True, random_state = 66)


### 기본 모델 ###
model = LGBMClassifier(objective='multi:softmax', n_estimators=300, learning_rate=0.1, n_jobs=-1)
model.fit(x_train, y_train)
score = model.score(x_test, y_test)
print('acc :', score)

#== Default acc : 0.9 ==#


### feature engineering ###
thresholds = np.sort(model.feature_importances_)
print(thresholds)
'''
[574 594 634 915]
'''
models=[]
res = np.array([])

for thresh in thresholds:
    selection = SelectFromModel(model, threshold=thresh, prefit=True)

    select_x_train = selection.transform(x_train)
    select_x_test = selection.transform(x_test)
    model2 = LGBMClassifier(objective='multiclass',n_estimators=300, learning_rate=0.1, n_jobs=-1)
    model2.fit(select_x_train, y_train, verbose=False, eval_metric=['multi_logloss','multi_error'],
                eval_set=[(select_x_train, y_train), (select_x_test, y_test)],
                early_stopping_rounds=20)
    
    y_pred = model2.predict(select_x_test)
    acc = accuracy_score(y_test, y_pred)
    models.append(model2)                   # 모델을 배열에 저장
    print('===models')
    print(models)                           # 모델 4번 도는 것 확인
    print('===thresh, acc')
    print(thresh, acc)
    res = np.append(res, acc)               # 결과값을 전부 배열에 저장
print(res.shape)                            # (4,)
print(type(models))                         # list 형식
print(type(res))                            # numpy 형식
best_idx = res.argmax()                     # 결과값 최대값의 index 저장
print(best_idx)
acc = res[best_idx]                         # 위 인덱스 기반으로 점수 호출
total_col = x_train.shape[1] - best_idx     # 전체 컬럼 계산
model = models[best_idx]

import pickle                               # 파이썬 제공 라이브러리
pickle.dump(model, open(f"./model/lgbm_save/iris--{acc}--{total_col}.pickle.dat", "wb"))    # wb 라는 형식으로 저장을 하겠다
print("저장됐다.")


