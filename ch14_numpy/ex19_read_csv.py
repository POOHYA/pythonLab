#    데이터 파일을 읽고 쓰기
import pandas as pd

print(pd.read_csv('./hyoju/ch14_numpy/sea_rain1.csv'))

print(pd.read_csv('./hyoju/ch14_numpy/sea_rain1.csv', index = '연도'))