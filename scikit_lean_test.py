# 必要なライブラリーのインポート
import pandas as pd
import numpy as np
from sklearn.datasets import load_boston

# データセットの読込み
boston = load_boston()

# データフレームの作成
# 説明変数の格納
df = pd.DataFrame(boston.data, columns = boston.feature_names)

# 目的変数の追加
df['MEDV'] = boston.target

# データの中身を確認
#print(df.head())

# 必要なライブラリーのインポート
import seaborn as sns

# 多変量連関図
sns.pairplot(df, size=1.0)