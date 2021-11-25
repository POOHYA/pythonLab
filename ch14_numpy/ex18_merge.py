# 특정 열을 기준으로 통합하기
import pandas as pd
from pandas.core.reshape.merge import merge

df_A_B = pd.DataFrame({'판매월':['1월','2월','3월','4월'],
                       '제품A':[100,150,200,130],
                       '제품B':[90,100,140,170]})


print(df_A_B)

df_C_D = pd.DataFrame({'판매월':['1월','2월','3월','4월'],
                       '제품C':[112,141,203,134],
                       '제품D':[90,110,140,170]})

print(df_C_D)

print(df_A_B.merge(df_C_D))


df_left = pd.DataFrame({'key': ['A','B','D'],'left':[1,2,3]})
print(df_left)

df_right = pd.DataFrame({'key': ['A','B','C'],'right':[4,5,6]})
print(df_right)


print(df_left.merge(df_right, how='left', on='key'))


print(df_left.merge(df_right, how='outer', on='key'))

