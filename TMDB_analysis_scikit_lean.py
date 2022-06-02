#線形回帰分析

import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# データフレームの作成
movie = pd.read_csv('movie.csv')

#インスタンス
linear_regression = LinearRegression()

#説明変数
X = movie[["budget"]].values

#Y 目的変数
Y = movie[["revenue"]].values
print(X)
print(Y)


# ライブラリーのインポート
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 学習データと評価データを作成
x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2, random_state=1)

#データを標準化
sc = StandardScaler()
sc.fit(x_train) #学習用データで標準化
x_train_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)


#学習
linear_regression.fit(x_train_std, y_train)  


# スコア計算のためのライブラリ
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error

# 回帰　
pred_lr = linear_regression.predict(x_test_std)

# 評価
# 決定係数(R2)
r2_lr = r2_score(y_test, pred_lr)

# 平均絶対誤差(MAE)
mae_lr = mean_absolute_error(y_test, pred_lr)

print("R2 : %.3f" % r2_lr)
print("MAE : %.3f" % mae_lr)


 # 説明変数の係数を出力
print('coefficient = ', linear_regression.coef_[0])
# 切片を出力
print('intercept = ', linear_regression.intercept_) 

coefficient =  9.10210898118
intercept =  -34.6706207764


plt.scatter(pred_lr, y_test, color = 'blue')         # 説明変数と目的変数のデータ点の散布図をプロット
plt.plot(X, linear_regression.predict(X), color = 'red') # 回帰直線をプロット

plt.title('movie_analysis')               # 図のタイトル
plt.xlabel('budget') # x軸のラベル
plt.ylabel('revenue')    # y軸のラベル
plt.grid()                                 # グリッド線を表示

plt.show()                                 # 図の表示



"""
# ライブラリーのインポート
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 学習データと評価データを作成
x_train, x_test, y_train, y_test = train_test_split(df.iloc[:, 0:13], df.iloc[:, 13],
                                                    test_size=0.2, random_state=1)

#データを標準化
sc = StandardScaler()
sc.fit(x_train) #学習用データで標準化
x_train_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)
"""