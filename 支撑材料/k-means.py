#导入相关库
import pandas as pd
import numpy as np
from sklearn.cluster import k_means

#导入合并后的数据集
data = pd.read_excel(r"表单12数据合并汇总.xlsx")

cols = data.columns[6:]
KMS = k_means(data[cols], 2)
KMS

accuracy = (KMS[1]==data['类型是否高钾']).sum()/len(data)*100
accuracy

#求出高钾玻璃和铅钡玻璃类型划分中心
category_1 = pd.DataFrame(KMS[0],columns = cols, index = ['铅钡玻璃中心','高钾玻璃中心'])
category_1

#划分高钾玻璃亚类
gaojia = data[data['类型是否高钾']==1]
category_2 = k_means(gaojia[gaojia.columns[6:]], 2)
category_2 = pd.DataFrame(data=category_2[0], columns=[gaojia.columns[6:]], index=['高钾玻璃亚类1','高钾玻璃亚类2'])
category_2

#划分铅钡玻璃亚类
qianbei = data[data['类型是否高钾']==0]
category_3 = k_means(qianbei[qianbei.columns[6:]], 3)
category_3 = pd.DataFrame(data=category_3[0], columns=[qianbei.columns[6:]], index=['铅钡玻璃亚类1','铅钡玻璃亚类2','铅钡玻璃亚类3'])
category_3

#计算整体轮廓系数
from sklearn.metrics import silhouette_score
Silhouette_Coefficient1 = silhouette_score(gaojia[gaojia.columns[6:]], category_3[1])
Silhouette_Coefficient1

Silhouette_Coefficient2 = silhouette_score(qianbei[qianbei.columns[6:]], category_3[1])
Silhouette_Coefficient2