#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/gist/whan0623/2d30fd4dbfedb2c05e4c700db78bea96/part1_.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # 판다스 자료구조 #
# - 시리즈(Series)
# - 데이터프레임(DataFrame)
# 

# ## 시리즈(Series) ##

# ### 시리즈(Series) 만들기 ###

# In[ ]:


import pandas as pd

data = {'name': '홍길동', 'kor': 80, 'eng':90, 'mat':70}
print(data)

s1 = pd.Series(data)

print("\n", type(data), type(s1))
print("\n", s1)


# ### 인덱스 구조 ###

# In[ ]:


import pandas as pd

data2 = ['홍길동', 80, 90, 70]
print(data2)

s2 = pd.Series(data2)

print("\n", type(data2), type(s2))
print("\n", s2)


# In[ ]:


print(s2.index)
print(s2.values)


# In[ ]:


print("\n", s1.index)
print("\n", s1.values)


# ### 원소 선택 ###

# In[ ]:


print(s2[1], s2[0])
print(s1[1], s1[0])
print(s1['kor'], s1['name'])


# In[ ]:


print("\n", s2[1:3])
print("\n", s1[1:3])
print("\n", s1['kor':'mat'])


# 

# ## 데이터프레임(DataFrame) ##

# ### 데이터프레임(DataFrame) 만들기 ##

# In[ ]:


import pandas as pd

data3 = {'name':['hong', 'gil', 'dong'], 'kor':[90,95,85], 'eng':[88,89,98], 'mat':[78, 76, 67]}
print(data3)

df3 = pd.DataFrame(data3)
print("\n", type(data3), type(df3))
print("\n", df3)


# ### 행(index) 인덱스/열(column) 이름 설정

# In[ ]:


import pandas as pd

data4 = [['hong', 'gil', 'dong'], [90,95,85], [88,89,98], [78, 76, 67]]
print(data4)

df4 = pd.DataFrame(data4)
print("\n", type(data4), type(df4))
print("\n", df4)


# In[ ]:


import pandas as pd

data5 = [['hong', 90, 88, 78], ['gil', 95, 89, 76], ['dong', 85, 98, 67]]
print(data5)

df5 = pd.DataFrame(data5)
print("\n", type(data5), type(df5))
print("\n", df5)


# In[ ]:


df5.index = [202100001, 202100002, 202100003]
print(df5)

df5.columns = ['name', 'kor', 'eng', 'mat']
print("\n", df5)


# In[ ]:


import pandas as pd

data6 = [['hong', 90, 88, 78], ['gil', 95, 89, 76], ['dong', 85, 98, 67]]
print(data6)

df6 = pd.DataFrame(data6, 
                   index = [202100001, 202100002, 202100003],
                   columns = ['name', 'kor', 'eng', 'mat'])
print("\n", type(data6), type(df6))
print("\n", df6)


# In[ ]:


df7 = df6.rename(index={202100003:202100008})
print(df7)
print("\n", df6)


# In[ ]:


df7 = df6.rename(columns={'name':'이름'})
print(df7)
print("\n", df6)


# In[ ]:


# inplace=True
df7 = df6.rename(columns={'name':'이름'}, inplace=True)
print(df7)
print("\n", df6)


# ### 행/열 삭제 ###
# - drop(행, axis=0)
# - drop(열, axis=1)

# In[ ]:


import pandas as pd

data7 = [['hong', 90, 88, 78], ['gil', 95, 89, 76], ['dong', 85, 98, 67]]
print(data7)

df7 = pd.DataFrame(data7, 
                   index = [202100001, 202100002, 202100003],
                   columns = ['name', 'kor', 'eng', 'mat'])
print("\n", df7)
#df7.drop(202100002, inplace=True)
#df7.drop([202100002, 202100003], inplace=True)
#df7.drop('kor', axis=1, inplace=True)
df7.drop(['kor', 'eng'], axis=1, inplace=True)
print("\n", df7)


# ### 행선택 ###
# - loc : 인덱스 이름 기준으로 행 선택
# - iloc : 정수형 위치 인덱스를 사용하여 행 선택

# In[ ]:


import pandas as pd

data7 = [['hong', 90, 88, 78], ['gil', 95, 89, 76], ['dong', 85, 98, 67]]
print(data7)

df7 = pd.DataFrame(data7, 
                   index = [202100001, 202100002, 202100003],
                   columns = ['name', 'kor', 'eng', 'mat'])
print("\n", df7)

st = df7.loc[202100002]
print("\n", st)

st2 = df7.iloc[1]
print("\n", st2)

st = df7.loc[[202100002, 202100003]]
print("\n", st)

st2 = df7.iloc[[1,2]]
print("\n", st2)


# ### 열 선택 ###
# - [] 사용
# - . 사용 : 열이름이 문자일 때만 사용 가능

# In[ ]:


import pandas as pd

data7 = [['hong', 90, 88, 78], ['gil', 95, 89, 76], ['dong', 85, 98, 67]]
print(data7)

df7 = pd.DataFrame(data7, 
                   index = [202100001, 202100002, 202100003],
                   columns = ['name', 'kor', 'eng', 'mat'])
print("\n", df7)

k = df7['kor']
print("\n", k)

k = df7[['kor', 'eng']]
print("\n", k)

e = df7.eng
print("\n", e)


# ### (행, 열) 선택
# - .loc[행, 열]
# - .loc[[행1,행2], [열1, 열2]]

# In[ ]:


import pandas as pd

data7 = [['hong', 90, 88, 78], ['gil', 95, 89, 76], ['dong', 85, 98, 67]]
print(data7)

df7 = pd.DataFrame(data7, 
                   index = [202100001, 202100002, 202100003],
                   columns = ['name', 'kor', 'eng', 'mat'])
print("\n", df7)

#c = df7.loc[202100002]
#c = df7.loc[202100002, 'name']
#c = df7.loc[202100002, ['name', 'kor']]
#c = df7.loc[[202100002, 202100003], ['name', 'eng']]
c = df7.loc[[202100002, 202100003], 'name':'eng']
print("\n", c)


# ### 열 추가 ###

# In[ ]:


import pandas as pd

data7 = [['hong', 90, 88, 78], ['gil', 95, 89, 76], ['dong', 85, 98, 67]]
print(data7)

df7 = pd.DataFrame(data7, 
                   index = [202100001, 202100002, 202100003],
                   columns = ['name', 'kor', 'eng', 'mat'])
print("\n", df7)

df7['sci'] = [88,77,66]
print("\n", df7)


# ### 행추가 ###

# In[ ]:


import pandas as pd

data7 = [['hong', 90, 88, 78], ['gil', 95, 89, 76], ['dong', 85, 98, 67]]
print(data7)

df7 = pd.DataFrame(data7, 
                   index = [202100001, 202100002, 202100003],
                   columns = ['name', 'kor', 'eng', 'mat'])
print("\n", df7)

df7.loc[202100004] = ['soon', 90,90,90]

print("\n", df7)


# ### 원소값 변경 ###

# In[ ]:


import pandas as pd

data7 = [['hong', 90, 88, 78], ['gil', 95, 89, 76], ['dong', 85, 98, 67]]
print(data7)

df7 = pd.DataFrame(data7, 
                   index = ['202100001', '202100002', '202100003'],
                   columns = ['name', 'kor', 'eng', 'mat'])

print("\n", df7)
#df7.loc['202100002', 'eng'] = 30
#df7.iloc[1,2] = 30

#df7.loc['202100002']['eng'] = 30    # 변경되지 않음
#df7.iloc[1][2] = 30                 # 변경되지 않음

df7.set_index('name', inplace=True)
df7.loc['gil']['eng'] = 30

print("\n", df7)


# ### 행 열의 위치 바꾸기 ###
# - transpose()

# In[ ]:


import pandas as pd

data = [['hong', 90, 88, 78], ['gil', 95, 89, 76], ['dong', 85, 98, 67]]
print(data)

df = pd.DataFrame(data, 
                   index = [202100001, 202100002, 202100003],
                   columns = ['name', 'kor', 'eng', 'mat'])
print("\n", df)
print("\n", df.T)
df.transpose()
print("\n", df)
#df = df.transpose()
df = df.T
print("\n", df)


# # 인덱스 활용 #

# ### 특정 열을 행 인덱스로 설정 ###
# - df.set_index('열이름' or ['열이름'])

# In[ ]:


import pandas as pd

data = [['hong', 90, 88, 78], ['gil', 95, 89, 76], ['dong', 85, 98, 67]]
print(data)

df = pd.DataFrame(data, 
                   index = [202100001, 202100002, 202100003],
                   columns = ['name', 'kor', 'eng', 'mat'])
print("\n", df)
#df = df.set_index('name')
df = df.set_index(['name', 'kor'])
print("\n", df)


# ### 행 인덱스 재배열 ###
# - df.reindex( 새로운 인덱스 배열)

# In[ ]:


import pandas as pd

data = [['hong', 90, 88, 78], ['gil', 95, 89, 76], ['dong', 85, 98, 67]]
print(data)

df = pd.DataFrame(data, 
                   index = [202100001, 202100002, 202100003],
                   columns = ['name', 'kor', 'eng', 'mat'])
print("\n", df)
df = df.reindex([202100003, 202100002, 202100001, 202100004 ])
print("\n", df)


# ### 행 인덱스 초기화 ###
# - df.reset_index()

# In[ ]:


import pandas as pd

data = [['hong', 90, 88, 78], ['gil', 95, 89, 76], ['dong', 85, 98, 67]]
print(data)

df = pd.DataFrame(data, 
                   index = [202100001, 202100002, 202100003],
                   columns = ['name', 'kor', 'eng', 'mat'])
print("\n", df)
df = df.reset_index()
print("\n", df)


# ### 행 인덱스를 기준으로 데이터프레임 정렬 ###
# df.sort_index()

# In[ ]:


import pandas as pd

data = [['hong', 90, 88, 78], ['gil', 95, 89, 76], ['dong', 85, 98, 67]]
print(data)

df = pd.DataFrame(data, 
                   index = [202100001, 202100002, 202100003],
                   columns = ['name', 'kor', 'eng', 'mat'])
print("\n", df)
df = df.sort_index(ascending=False)
print("\n", df)


# ### 데이터 값 기준으로 데이터프레임 정렬 ###
# df.sort_values()

# In[ ]:


import pandas as pd

data = [['hong', 90, 88, 78], ['gil', 95, 89, 76], ['dong', 85, 98, 67]]
print(data)

df = pd.DataFrame(data, 
                   index = [202100001, 202100002, 202100003],
                   columns = ['name', 'kor', 'eng', 'mat'])
print("\n", df)
df = df.sort_values(by='kor', ascending=False)
print("\n", df)


# # 산술연산 #

# ## 시리즈 연산 ##

# ### 시리즈 vs 숫자###
# - series 사칙연산(+, -, *, /) 숫자

# In[ ]:


import pandas as pd

s = pd.Series({'kor': 80, 'eng':90, 'mat':70})
print(s)

t = s / 10
print("\n", t)


# ### 시리즈 vs 시리즈 ###
# - series 사칙연산(+, -, *, /) series

# In[ ]:


import pandas as pd

s1 = pd.Series({'kor': 80, 'eng':90, 'mat':70})
s2 = pd.Series({'eng':70, 'mat':90, 'kor': 50, 'sci':100})
print(s1)
print("\n", s2)

t = s1 + s2
print("\n", t)


# ### NaN이 있는 시리즈 연산 ###

# In[ ]:


import numpy as np
import pandas as pd

s1 = pd.Series({'kor': 80, 'eng':90, 'mat':70})
s2 = pd.Series({'eng': np.nan, 'mat':90, 'kor': 50, 'sci':100})
print(s1)
print(s2)

add = s1 + s2
print('\n', add)

sub = s1 - s2
print('\n', sub)

mul = s1 * s2
print('\n', mul)

div = s1 / s2
print('\n', div)

df = pd.DataFrame([add, sub, mul, div],
                  index=['add', 'sub', 'mul', 'div'])
print('\n', df)


# ### 연산 메소드 ###
# - series.add(series, fill_value=0)
# - series.sub(series, fill_value=0)
# - series.mul(series, fill_value=0)
# - series.div(series, fill_value=0)

# In[ ]:


import numpy as np
import pandas as pd

s1 = pd.Series({'kor': 80, 'eng':90, 'mat':70})
s2 = pd.Series({'eng': np.nan, 'mat':90, 'kor': 50, 'sci':100})
print(s1)
print(s2)

add = s1.add(s2, fill_value=0)
sub = s1.sub(s2, fill_value=0)
mul = s1.mul(s2, fill_value=0)
div = s1.div(s2, fill_value=0)

print('\n', add)
print('\n', sub)
print('\n', mul)
print('\n', div)

df = pd.DataFrame([add, sub, mul, div],
                  index=['add', 'sub', 'mul', 'div'])
print('\n', df)


# ## 데이터프레임 연산 ##

# ### 데이터프레임 vs 숫자
# - df 사칙연산(+, -, *, /) 숫자

# In[ ]:


import pandas as pd

data = [[90, 88, 78], [95, 89, 76], [85, 98, 67]]
print(data)

df = pd.DataFrame(data, 
                   index = [202100001, 202100002, 202100003],
                   columns = ['kor', 'eng', 'mat'])
print(df)
df = df * 10
print('\n', df)


# ### 데이터프레임 vs 숫자
# - df 사칙연산(+, -, *, /) df

# In[ ]:


import pandas as pd

df1 = pd.DataFrame([[90, 88, 78], [95, 89, 76], [85, 98, 67]], 
                   index = [202100001, 202100002, 202100003],
                   columns = ['kor', 'eng', 'mat'])

df2 = pd.DataFrame([[2, 3, 4], [5, 6, 7], [7, 9, 1]], 
                   index = [202100001, 202100002, 202100004],
                   columns = ['kor', 'eng', 'mat'])

print(df1)
print("\n", df2)

df = df1 * df2
print('\n', df)


# In[ ]:


import pandas as pd

df1 = pd.DataFrame([[90, 88, 78], [95, 89, 76], [85, 98, 67]], 
                   index = [202100001, 202100002, 202100003],
                   columns = ['kor', 'eng', 'mat'])

df2 = pd.DataFrame([[2, 3, 4], [5, 6, 7], [7, 9, 1]], 
                   index = [202100001, 202100002, 202100004],
                   columns = ['kor', 'eng', 'mat'])

print(df1)
print("\n", df2)

df = df1.add(df2, fill_value=0)
print('\n', df)

print('\n', df.head(2))
print('\n', df.tail(2))

