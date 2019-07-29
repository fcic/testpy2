from pandas import Series, DataFrame
import pandas as pd

#1
# obj = Series([1,-2,3,-4])
# obj = Series([1,-2,3,-4],index=['a','b','c','d'])
# print(obj)
# a    1
# b   -2
# c    3
# d   -4
# dtype: int64

#2
data_1row ={'id':'fcic','age':30}
data_Nrow  =[{ "id":"fcic" ,     "age":70},{"id":"ooobbb","age":31} ,{"id":"peter","age":60}] 
data_Nrow2={'id':['fcic','ooobbb','peter'],'age':[30,31,60]}
# print(data_Nrow2)

#3
#两种格式结果是一样的
# df=DataFrame(data_Nrow2,columns=['id','age'])
# df=DataFrame(data_Nrow,columns=['id','age'])
df=DataFrame(data_Nrow)
df=df.sort_values('age')
#        id  age
# 0    fcic   30
# 1  ooobbb   31
# 2   peter   60
df=df.append({'id':'Mark','age':35},True)
df['NewCol']=[11,22,33,44]
# print(df)
#        id  age  NewCol
# 0  ooobbb   31      11
# 1   peter   60      22
# 2    fcic   70      33
# 3    Mark   35      44


def  json2xls(json):
    # print(DataFrame(json))
    DataFrame(json).to_excel('./json2xls.xls','sheetfcic');

# json2xls(data_Nrow)

#testerror 
# a=pd.read_json([{ "id":"fcic" ,     "age":70},{"id":"ooobbb","age":31} ,{"id":"peter","age":60}] )
# print(a)