#导入相关库
import pandas as pd
import numpy as np
from sklearn import svm

#导入合并后的数据集
data = pd.read_excel(r"表单12数据合并汇总.xlsx")

#划分两类数据集，风化文物饰品的数据和未风化文物饰品数据
fenghua = data[data['表面风化']==1]
weifenghua = data[data['表面风化']==0]
cols = ['类型是否高钾']+list(df.columns[6:])
fenghua = fenghua[cols]
weifenghua = weifenghua[cols]
#支持向量回归SVR模型
svr = svm.SVR(kernel='linear')

#模型训练
cf = [0 for i in range(len(cols))]
for i in range(len(cols)):
    for j in range(5):
        index = list(fenghua.index)
        np.random.shuffle(index)
        svr.fit(fenghua.loc[index[:25]].values, weifenghua.values[:, i])
        cf[i] += svr.coef_/5
for i in range(15):
    print(fenghua.columns[i], '的模型系数',cf[i])