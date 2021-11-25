# 표 형식의 데이터를 파일로 쓰기
import pandas as pd

df_WH = pd.DataFrame({'Weight': [62,67,55,74],
                      'Height': [165,177,160,180]},
                      index = ['ID_1','ID_2','ID_3','ID_4'])

df_WH.index.name = 'User'

print(df_WH)

bmi = df_WH['Weight'] / (df_WH['Height']/100)**2
print(bmi)

df_WH['BMI'] = bmi
print(df_WH)

df_WH.to_csv('./hyoju/ch14_numpy/save_DataFrame.csv')

df_pr = pd.DataFrame({'판매가격': [2000,3000,5000,10000],
                      '판매량': [32,53,40,25]},
                      index = ['P1001','P1002','P1003','P1004'])

df_pr.index.name = '제품번호'
print(df_pr)

file_name = './hyoju/ch14_numpy/save_DataFrame_utf-8.txt'
df_pr.to_csv(file_name,sep = " ", encoding = "utf-8")