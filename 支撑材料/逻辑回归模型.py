import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_excel('表单12数据合并汇总.xlsx', index_col=0)
#附件表单3的数据处理
data1 = pd.read_excel('附件.xlsx', index_col=2)
data1=data1.fillna(0)
cols1 = data1.columns[2:]
data1['成分比例累加和']=np.sum(data1[cols1], axis=1)

cols = data.columns[6:]
x_tr = data[['是否风化']+list(cols)].values
y_tr = data['类型是否高钾'].values
#类型预测
pre = data1[data1.columns[1:-1]].values
LogisticRegression.fit(x_tr, y_tr)
pre_y = LogisticRegression.predict(pre)
pre_y