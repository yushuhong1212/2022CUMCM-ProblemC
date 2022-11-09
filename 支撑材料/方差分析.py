import pandas as pd
import numpy as np

data = pd.read_excel(r"表单12数据合并汇总.xlsx", index_col=0)
col = ['类型是否高钾','二氧化硅(SiO2)',
       '氧化钠(Na2O)', '氧化钾(K2O)', '氧化钙(CaO)', '氧化镁(MgO)', '氧化铝(Al2O3)',
       '氧化铁(Fe2O3)', '氧化铜(CuO)', '氧化铅(PbO)', '氧化钡(BaO)', '五氧化二磷(P2O5)',
       '氧化锶(SrO)', '氧化锡(SnO2)', '二氧化硫(SO2)']
data1 = data[col]

# 方差分析
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

data_melt = data1.melt()
data_melt.columns = ['类型是否高钾', '化学成分']
model = ols('化学成分 ~C(类型是否高钾)', data = data_melt).fit()
anova_table = anova_lm(model, type = 2)
pd.DataFrame(anova_table)

# 进行事后比较分析
print(pairwise_tukeyhsd(data_melt['化学成分'], data_melt['类型是否高钾']))